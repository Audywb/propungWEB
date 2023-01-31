from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
from django.contrib.auth.models import Group,User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.contrib import messages
from django.conf import settings

from promo.forms import SignUpForm, registerForm
from promo.models import Category,Promotion,Recom,Slides,Cart,CartItem,Product,Order,OrderItem,Registers,OrderPartner,OrderDetail
import stripe
import datetime

# Create your views here.

def check_user(user: User):
    return not user.is_staff and not user.is_superuser


def check_staff(user: User):
    return user.is_staff


def check_admin(user: User):
    return user.is_superuser

@login_required
def member(request):
    if request.user.is_superuser:
        return redirect('Home')
    elif request.user.is_staff:
        return redirect('partnerinfo')
    elif not request.user.is_staff and not request.user.is_superuser:
        return redirect('Home')
    else:
        return redirect('Home')

def Home(request):
    slides = None
    slides = Slides.objects.all()
    recom = None
    recom = Recom.objects.all()
    promotions = None
    promotions = Promotion.objects.all()
    return render(request,'promo/recompd.html',{'promotions':promotions,'recom':recom,'slides':slides})

# def Login(request):
#     return render(request,'promo/login.html')

def Promo(request):
    promotions = None
    promotions = Promotion.objects.all()
    return render(request,'promo/Promotion.html',{'promotions':promotions})

def partner(request):
    return render(request,'promo/partner.html')

def contact(request):
    return render(request,'promo/contact.html')


#SignUP
def register(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            #บันทึกข้อมูล User
            form.save()
            #บันทึก Group Customer
            #ดึง Username มาใช้
            username = form.cleaned_data.get('username')
            #ดึงข้อมูลยูเซอร์จากฐานข้อมูล
            signUpUser = User.objects.get(username=username)
            #จัด Group
            customer_group = Group.objects.get(name="Customer")
            customer_group.user_set.add(signUpUser)
            messages.success(request, "ยินดีต้อนรับสู่ครอบครัว Pro Pung")
            return redirect('login')

    else :
        form=SignUpForm()
    return render(request,'promo/register.html',{'form':form})

# Login
def loginform(request):
    if request.user.is_authenticated:
        return redirect('Home')
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None :
                login(request,user)
                return redirect('Home')
            else :
                return redirect('register')
    else :
        form = AuthenticationForm()
    return render(request, 'promo/login.html',{'form':form})

def signOutView(request):
    logout(request)
    return redirect('Home')

@login_required
@user_passes_test(check_user, login_url='/Home')
def registerParner(request):
    if request.method=='POST':
        form=registerForm(request.POST)
        if form.is_valid():
            #บันทึกข้อมูล User
            form.save()
            messages.success(request, "คุณส่งแบบฟอร์มสมัครสมาชิกสำเร็จ รอการติดต่อกลับผ่านทางอีเมลล์")
            return redirect('registerParner')

    else :
        form=registerForm()

    return render(request,'promo/registerPartner.html',{'form':form})


#หน้าฝากหิ้ว

def preorder(request):
    preorders = None
    preorders = Product.objects.all()
    return render(request,'promo/pre-order0.html',{'preorders':preorders})

def showproduct(request,category_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e :
          raise e
    return render(request,'info/pre_product.html',{'product':product})

    # return render(request,'info/pre_product.html')

def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

@login_required
def addCart(request,product_id):
    #ดึงสินค้าที่เราซื้อมาใช้งาน
    product=Product.objects.get(id=product_id)
    #สร้างตะกร้าสินค้า
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

    try:
        #ซื้อรายการสินค้าซ้ำ
        cart_item=CartItem.objects.get(product=product,cart=cart)
        if cart_item.quantity<cart_item.product.stock :
            #เปลี่ยนจำนวนรายการสินค้า
            cart_item.quantity+=1
            #บันทึก/อัพเดทค่า
            cart_item.save()
    except CartItem.DoesNotExist:
        #ซื้อรายการสินค้าครั้งแรก
        #บันทึกลงฐานข้อมูล
        cart_item=CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1
        )
        cart_item.save()
    return redirect('preorder')

@login_required
@user_passes_test(check_user, login_url='/Home')
def cartdetail(request):
    total = 0
    counter = 0
    cart_items = None
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request)) #ดึงตะกร้ามา
        cart_items=CartItem.objects.filter(cart=cart, active=True) #ดึงข้อมูลสินค้าในตะกร้า
        for item in cart_items:
            total+=(item.product.price*item.quantity)
            counter+=item.quantity
    except Exception as e :
        pass
    stripe.api_key=settings.SECRET_KEY
    stripe_total=int(total*100)
    description="Payment Online"
    data_key=settings.PUBLIC_KEY
    if request.method=="POST":
        try :
            token=request.POST['stripeToken']
            email=request.POST['stripeEmail']
            name=request.POST['stripeBillingName']
            address=request.POST['stripeBillingAddressLine1']
            city=request.POST['stripeBillingAddressCity']
            postcode=request.POST['stripeShippingAddressZip']
            customer=stripe.Customer.create(
                email=email,
                source=token
            )
            charge=stripe.Charge.create(
                amount=stripe_total,
                currency='thb',
                description=description,
                customer=customer.id
            )
            #บันทึกข้อมูลใบสั่งซื้อ
            order=Order.objects.create(
                name=name,
                address=address,
                city=city,
                postcode=postcode,
                total=total,
                email=email,
                token=token
            )
            order.save()

            #บันทึกรายการสั่งซื้อ
            for item in cart_items :
                order_item=OrderItem.objects.create(
                    product=item.product.name,
                    quantity=item.quantity,
                    price=item.product.price,
                    order=order
                )
                order_item.save()
                #ลดจำนวน Stock
                product=Product.objects.get(id=item.product.id)
                product.stock=int(item.product.stock-order_item.quantity)
                product.save()
                item.delete()

            #บันทึกคนรับหิ้ว
            partners = None
            partners = Registers.objects.filter(active=True).order_by("id")[0]
            partner = partners
            partners.active = False
            partners.save()

            first_name = partner.first_name
            last_name = partner.last_name
            username = partner.username
            email = partner.email
            Phone_namber = partner.Phone_namber
            Prompt_Pay = partner.Prompt_Pay
            ID_card = partner.ID_card
            address = partner.address
            ZIP_code = partner.ZIP_code

            orderpartner=OrderPartner.objects.create(
                        first_name = first_name,
                        last_name = last_name,
                        username = username,
                        email = email,
                        Phone_namber = Phone_namber,
                        Prompt_Pay = Prompt_Pay,
                        ID_card = ID_card,
                        address = address,
                        ZIP_code = ZIP_code,
                        orderId = str(order)
                    )
            orderpartner.save()

            return redirect('thankyou')

        except stripe.error.CardError as e :
            return False , e
    

    return render(request,'info/cartdetail.html',
    dict(cart_items=cart_items,total=total,counter=counter,
    data_key=data_key,
    stripe_total=stripe_total,
    description=description))

@login_required
def removeCart(request,product_id):
    #ทำงานกับตะกร้าสินค้า A
    cart=Cart.objects.get(cart_id=_cart_id(request))
    #ทำงานกับสินค้าที่จะลบ 1
    product=get_object_or_404(Product,id=product_id)
    cartItem=CartItem.objects.get(product=product,cart=cart)
    #ลบรายการสินค้า 1 ออกจากตะกร้า A โดยลบจาก รายการสินค้าในตะกร้า (CartItem)
    cartItem.delete()
    return redirect('cartdetail')

@login_required
@user_passes_test(check_user, login_url='/Home')
def orderHistory(request):
    if request.user.is_authenticated:
        email=str(request.user.email)
        orders=Order.objects.filter(email=email)
    return render(request,'info/orders.html',{'orders':orders,})

@login_required
@user_passes_test(check_user, login_url='/Home')
def viewOrder(request,order_id):

    if request.user.is_authenticated:
        email=str(request.user.email)
        order=Order.objects.get(email=email,id=order_id)
        orderitem=OrderItem.objects.filter(order=order)
        # print(order)
        orderIdP = order

    orderPartner = OrderPartner.objects.filter(active=True,orderId=str(orderIdP)).order_by("id")[0]
    # print(orderPartner.orderId)
    return render(request,'info/viewOrder.html',{'order': order, 'order_items': orderitem,'orderPartner':orderPartner})

@login_required
def thankyou(request):
    return render(request,'promo/thankyou.html')

@login_required
@user_passes_test(check_staff, login_url='/Home')
def partner_info(request):
    if request.user.is_staff:
        email=str(request.user.email)
        ordersP=OrderPartner.objects.filter(email=email, active=True)
        orders = Order.objects.all()
        OrderItems = OrderItem.objects.all()

    return render(request,'info/partner_order.html',{'orders':ordersP,'order':orders,'OrderItem':OrderItems})

def search(request):
    preorders=Product.objects.filter(name__contains=request.GET['title'])
    return render(request,'promo/pre-order0.html',{'preorders':preorders})
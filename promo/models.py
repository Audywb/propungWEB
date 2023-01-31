from django.db import models
import uuid
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(max_length=255,unique=True)

    def __str__(self):
        return self.name

    class Meta :
        ordering=('name',)
        verbose_name='หมวดหมู่สินค้า'
        verbose_name_plural="ข้อมูลประเภทสินค้า"

    def get_url(self):
        return reverse('preorder',args=[self.slug])

class Promotion(models.Model):
    name = models.CharField(max_length=255,unique=False) #ชื่อโปรโมชั่น
    slug = models.SlugField(max_length=255,unique=False) #ชื่อเล่นโปรโมชั่น
    description = models.TextField(blank=True) #รายละเอียดสินค้า
    partner_link = models.TextField(blank=True) #ร้านค้าที่ร่วมโปรโมชั่น
    period = models.CharField(max_length=255,unique=False) #ระยะเวลาโปรโมชั่น
    price = models.IntegerField(primary_key=True) # ราคาสินค้าใส่ได้ 20 ตัว
    category = models.ForeignKey(Category,on_delete=models.CASCADE) #on_delete CASCADE เวลาลบข้อมูลจะลบทั้งสองตาราง
    image = models.ImageField(upload_to="promotion",blank=True) # อัพโหลดรูปไว้โฟลเดอร์ product
    logo = models.ImageField(upload_to="promotion",blank=True) # อัพโหลดLOGOไว้โฟลเดอร์ product
    created = models.DateTimeField(auto_now_add=True) #เวลาอัพโหลด
    updated = models.DateTimeField(auto_now=True) #เวลาอัพเดต

    def __str__(self):
        return self.name

    class Meta :
        ordering=('name',)
        verbose_name='สินค้า'
        verbose_name_plural="ข้อมูลสินค้าโปรโมชั่น"

class Pre_order(models.Model):
    name = models.CharField(max_length=255,unique=False) #ชื่อโปรโมชั่น
    slug = models.SlugField(max_length=255,unique=False) #ชื่อเล่นโปรโมชั่น
    description = models.TextField(blank=True) #รายละเอียดสินค้า
    partner_link = models.TextField(blank=True) #ร้านค้าที่ร่วมโปรโมชั่น
    period = models.CharField(max_length=255,unique=False) #ระยะเวลาโปรโมชั่น
    price = models.IntegerField(primary_key=True) # ราคาสินค้าใส่ได้ 20 ตัว
    stock=models.IntegerField(default=1)
    category = models.ForeignKey(Category,on_delete=models.CASCADE) #on_delete CASCADE เวลาลบข้อมูลจะลบทั้งสองตาราง
    available=models.BooleanField(default=True)
    image = models.ImageField(upload_to="preorder",blank=True) # อัพโหลดรูปไว้โฟลเดอร์ product
    logo = models.ImageField(upload_to="preorder",blank=True) # อัพโหลดLOGOไว้โฟลเดอร์ product
    created = models.DateTimeField(auto_now_add=True) #เวลาอัพโหลด
    updated = models.DateTimeField(auto_now=True) #เวลาอัพเดต

    def __str__(self):
        return self.name

    class Meta :
        ordering=('name',)
        verbose_name='สินค้ารับหิ้ว'
        verbose_name_plural="ข้อมูลสินค้าหน้ารับหิ้ว"

    def get_url(self):
        return reverse('showproduct',args=[self.category.slug,self.slug])

class Product(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    period = models.CharField(max_length=255,unique=False, default='สาขาที่ขาย') #ระยะเวลาโปรโมชั่น
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="product",blank=True)
    image2=models.ImageField(upload_to="product",blank=True)
    image3=models.ImageField(upload_to="product",blank=True)
    logo = models.ImageField(upload_to="preorder",blank=True) # อัพโหลดLOGOไว้โฟลเดอร์ product
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta :
        ordering=('name',)
        verbose_name='สินค้า'
        verbose_name_plural="ข้อมูลสินค้าหน้ารับหิ้ว"

    def get_url(self):
        return reverse('showproduct',args=[self.category.slug,self.slug])

class Recom(models.Model):
    name = models.CharField(max_length=255,unique=False) #ชื่อโปรโมชั่น
    slug = models.SlugField(max_length=255,unique=False) #ชื่อเล่นโปรโมชั่น
    description = models.TextField(blank=True) #รายละเอียดสินค้า
    partner_link = models.TextField(blank=True) #ร้านค้าที่ร่วมโปรโมชั่น
    period = models.CharField(max_length=255,unique=False) #ระยะเวลาโปรโมชั่น
    price = models.IntegerField(primary_key=True) # ราคาสินค้าใส่ได้ 20 ตัว
    category = models.ForeignKey(Category,on_delete=models.CASCADE) #on_delete CASCADE เวลาลบข้อมูลจะลบทั้งสองตาราง
    image = models.ImageField(upload_to="recom",blank=True) # อัพโหลดรูปไว้โฟลเดอร์ product
    logo = models.ImageField(upload_to="recom",blank=True) # อัพโหลดLOGOไว้โฟลเดอร์ product
    created = models.DateTimeField(auto_now_add=True) #เวลาอัพโหลด
    updated = models.DateTimeField(auto_now=True) #เวลาอัพเดต

    def __str__(self):
        return self.name

    class Meta :
        ordering=('name',)
        verbose_name='สินค้าแนะนำ'
        verbose_name_plural="ข้อมูลสินค้าแนะนำ"

class Slides(models.Model):
    name = models.CharField(max_length=255,unique=False) #ชื่อสไลด์
    slug = models.SlugField(max_length=255,unique=False) #ชื่อเล่นสไลด์
    link = models.TextField(blank=True)
    image = models.ImageField(upload_to="slides",blank=True) # อัพโหลดรูปไว้โฟลเดอร์ slides
    created = models.DateTimeField(auto_now_add=True) #เวลาอัพโหลด
    updated = models.DateTimeField(auto_now=True) #เวลาอัพเดต

    def __str__(self):
        return self.name

    class Meta :
        ordering=('name',)
        verbose_name='ภาพสไลด์'
        verbose_name_plural="ข้อมูลภาพสไลด์"

#ตระกร้าสินค้า
class Cart(models.Model):
    cart_id=models.CharField(max_length=255,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    
    class Meta:
        db_table='cart'
        # ordering=('date_added',)
        verbose_name='ตะกร้าสินค้า'
        verbose_name_plural="ข้อมูลตะกร้าสินค้า"

class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField() #จำนวนสินค้าที่เพิ่มลงตระกร้า
    active=models.BooleanField(default=True)

    class Meta:
        db_table='cartItem'
        verbose_name='รายการสินค้าในตะกร้า'
        verbose_name_plural="ข้อมูลรายการสินค้าในตะกร้า"
    
    def sub_total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return self.product.name

class Order(models.Model):
    name=models.CharField(max_length=255,blank=True)
    address=models.CharField(max_length=255,blank=True)
    city=models.CharField(max_length=255,blank=True)
    postcode=models.CharField(max_length=255,blank=True)
    total=models.DecimalField(max_digits=10,decimal_places=2)
    email=models.EmailField(max_length=250,blank=True)
    token=models.CharField(max_length=255,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta :
        db_table='Order'
        ordering=('id',)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product=models.CharField(max_length=250)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta :
        db_table='OrderItem'
        ordering=('order',)

    def sub_total(self):
        return self.quantity*self.price
    
    def __str__(self):
        return self.product

class Registers(models.Model):
    first_name = models.CharField(max_length=100,unique=False)
    last_name = models.CharField(max_length=100,unique=False)
    username = models.CharField(max_length=100,unique=True)
    email = models.CharField(max_length=250,unique=True)
    Phone_namber = models.CharField(max_length=12,unique=True)
    Prompt_Pay = models.CharField(max_length=13,unique=True,default="0123456789999")
    ID_card = models.CharField(max_length=13,unique=True)
    address = models.TextField()
    ZIP_code = models.CharField(max_length=6)
    active=models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True) #เวลาอัพโหลด
    updated = models.DateTimeField(auto_now=True) #เวลาอัพเดต

    def __str__(self):
        return self.username

    class Meta :
        verbose_name='สมาชิกรับหิ้ว'
        verbose_name_plural="ข้อมูลสมาชิกรับหิ้ว"

class OrderPartner(models.Model):
    first_name = models.CharField(max_length=100,unique=False)
    last_name = models.CharField(max_length=100,unique=False)
    username = models.CharField(max_length=100,unique=False)
    email = models.CharField(max_length=250,unique=False)
    Phone_namber = models.CharField(max_length=12,unique=False)
    Prompt_Pay = models.CharField(max_length=13,unique=False,default="0123456789999")
    ID_card = models.CharField(max_length=13,unique=False)
    address = models.TextField()
    ZIP_code = models.CharField(max_length=6)
    active=models.BooleanField(default=True)
    orderId = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True) #เวลาอัพโหลด
    updated = models.DateTimeField(auto_now=True) #เวลาอัพเดต

    def __str__(self):
        return self.username

    class Meta :
        ordering=('orderId',)
        verbose_name='รายการรับหิ้ว'
        verbose_name_plural="รายการรับหิ้ว"

class OrderDetail(models.Model):
    partneruser = models.CharField(max_length=100,unique=False)
    partneremail = models.CharField(max_length=250,unique=True)
    name=models.CharField(max_length=255,blank=True)
    address=models.CharField(max_length=255,blank=True)
    city=models.CharField(max_length=255,blank=True)
    postcode=models.CharField(max_length=255,blank=True)
    total=models.DecimalField(max_digits=10,decimal_places=2)
    email=models.EmailField(max_length=250,blank=True)
    token=models.CharField(max_length=255,blank=True)
    product=models.CharField(max_length=250)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta :
        db_table='OrderDetail'
        ordering=('id',)

    def __str__(self):
        return str(self.id)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES = (
('Abuja', 'Nigeria'),
('Accra', 'Ghana'),
('Addis Abba', 'Ethiopia'),
('Algiers', 'Algeria'),
('Antananarivo', 'Madagascar'),
('Asmera', 'Eritrea'),
('Bamako', 'Mali'),
('Bangu', ' Central African Republic'),
('Banjul', 'Gambia'),
('Bissau', 'Guinea-Bissau'),
('Brazzaville', ' Republic of the Congo'),
('Bujumbura', ' Burundi'),
('Cairo', 'Egypt'),
('Conakry', ' Guinea'),
('Dakar', ' Senegal'),
('Dar es Salaam', ' Tanzania'),
('Djibouti City', ' Djibouti'),
('Freetown', 'Sierra Leone'),
('Gaborone', 'Botswana'),
('Harare', 'Zimbabwe'),
('Juba', ' South Sudan'),
('Kampala', ' Uganda'),
('Khartoum', ' Sudan'),
('Kigali', 'Rwanda'),
('Kinshasa', ' Democratic Republic of the Congo'),
('Libreville', ' Gabon'),
('Lilongwe', ' Malawi'),
('Lome', ' Togo'),
('Luanda', ' Angola'),
('Lusaka', ' Zambia'),
('Malabo', ' Equatorial Guinea'),
('Maputo', ' Mozambique'),
('Maseru', 'Lesotho'),
('Mbabane', ' Swaziland'),
('Mogadishu', ' Somalia'),
('Monrovia', ' Liberia'),
('Moroni', 'Comoros'),
('Nairobi', ' Kenya'),
('N’Djamena', ' Chad'),
('Niamey', ' Niger'),
('Nouakchott', ' Mauritania'),
('Ouagadougou', ' Burkina Faso'),
('Port Louis', ' Mauritius'),
('Pretoria', ' South Africa'),
('Porto Novo', ' Benin'),
('Praia', ' Cape Verde'),
('Rabat', ' Morocco'),
('Tripoli', ' Libya'),
('Tunis', ' Tunisia'),
('Victoria', ' Seychelles'),
('Windhoek', ' Namibia'),
('Yamoussoukro', ' Cote d’Ivoire'),
('Yaoundé', ' Cameroon'),
 )

CATEGORY_CHOICES = (
    ('CR', 'Curd'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'MilkShake'),
    ('PN', 'Paneer'),
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),
    ('IC', 'Ice-Creams'),
    )

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def _str_(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    def _str_(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
       return self.quantity * self.product.discounted_price

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the way', 'On the way'),
    ('Delivered', 'Delivered'),
    ('Pending', 'Pending'),
)

class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
    paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default='pending')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE,default="")
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

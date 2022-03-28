from datetime import datetime
from turtle import title
from django.db import models

# Create your models here.
choice_type=[
    ('f','Furnished'),
    ('uf','Unfurnished')
]
condition_choice=[
            ('N','New'),
            ('U','Used'),
        ]
Construction_State=[
    ('gf','Ground Floor'),
    ('g+1','Ground+1'),
    ('g+2','Ground+2')
]
electronic_type=[
        ('computer & accessories', 'Computer & Accessories'),
        ('mobile & acessories','Mobile & Acessories'),
        ('tablets','Tablets'),
        ('tv & video','Tv & Video'),
        ('cameras','Cameras'),
        ('headphones','Headphones'),
        ('video games','Video Games'),
        ('bluetooth & wireless speakers','Bluetooth & Wireless Speakers'),
        ('generator, ups & power solution','Generator, UPS & Power Solution'),
        ('acs & coolers', 'ACs & Coolers'),
        ('refrigerators & freezers', 'Refrigerators & Freezers'),
        ('washing machine & dryers','Washing Machine & Dryers')
]
Cars_Brand= [
    ('volvo', 'Volvo'),
    ('saab', 'Saab'),
    ('mercedes', 'Mercedes'),
    ('audi', 'Audi'),
    ]
Choices=[
    ('rent','Rent'),
    ('sale','Sale')
]
AvailableSize_choices=[
    ('S','Small'),
    ('M','Medium'),
    ('L','Large'),
    ('XL','Extra Large'),
    ('36','36'),
    ('38','38'),
    ('39','39'),
    ('40','40'),
]
type_choices=[
    ('electronics repair','Electronics Repair'),
    ('tution','Tution'),
    ('driver','Driver'),
    ('others','Others'),
]
class Vehicles(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    Description=models.CharField(max_length=255)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    photo=models.ImageField(upload_to="\static")
    manufacturing_Company=models.CharField(max_length=50)
    model =models.CharField(max_length=50)
    manufacturing_year=models.CharField(max_length=50)
    condition=models.CharField(max_length=10,choices=condition_choice)
    created_at=models.DateTimeField(default=datetime.now)
    #sparepart=models.ForeignKey(SpareParts,on_delete=models.CASCADE)
class SpareParts(models.Model):
    id=models.AutoField(primary_key=True) 
    vehcile=models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    Description=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    photo=models.ImageField(upload_to="\static")
    manufacturing_Company=models.CharField(max_length=50)
    Brand =models.CharField(max_length=10, choices=Cars_Brand, default='Volvo')
    condition=models.CharField(max_length=10,choices=condition_choice)
    created_at=models.DateTimeField(default=datetime.now)
class Electronics(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    Description=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    photo=models.ImageField(upload_to="\static")
    manufacturing_Company=models.CharField(max_length=50)
    type=models.CharField(max_length=100, choices=electronic_type, default='Computer & Accessories')
    condition=models.CharField(max_length=10,choices=condition_choice)
    created_at=models.DateTimeField(default=datetime.now)
class HomeDecor(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    Description=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    photo=models.ImageField(upload_to="\static")
    manufacturing_Company=models.CharField(max_length=50)
    condition=models.CharField(max_length=10,choices=condition_choice)
    created_at=models.DateTimeField(default=datetime.now)
class House_Apartments(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    Description=models.CharField(max_length=255)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    photo=models.ImageField(upload_to="\static")
    no_of_bedrooms=models.IntegerField()
    no_of_bathrooms=models.IntegerField()
    For=models.CharField(max_length=10, choices=Choices, default='Rent')
    construction_state=models.CharField(max_length=30,choices=Construction_State)
    created_at=models.DateTimeField(default=datetime.now)
class Shops_Office(models.Model):
    id=models.AutoField(primary_key=True)
    house_apartment=models.ForeignKey(House_Apartments,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    Description=models.CharField(max_length=255)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    photo=models.ImageField(upload_to="\static")
    no_of_floors=models.IntegerField()
    type=models.CharField(max_length=20, choices=choice_type)
    For=models.CharField(max_length=10, choices=Choices, default='Rent')
    created_at=models.DateTimeField(default=datetime.now)
class Land_Plots(models.Model):
    id=models.AutoField(primary_key=True)
    shop_office=models.ForeignKey(Shops_Office, on_delete=models.CASCADE)
    house_apartment=models.ForeignKey(House_Apartments, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    Description=models.CharField(max_length=255)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    photo=models.ImageField(upload_to="\static")
    plot_area=models.IntegerField()
    For=models.CharField(max_length=10, choices=Choices, default='Rent')
    created_at=models.DateTimeField(default=datetime.now)
class Clothing_Beauty_Health(models.Model):
    title=models.CharField(max_length=50)
    Description=models.CharField(max_length=255)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    photo=models.ImageField(upload_to="\static")
    brand=models.CharField(max_length=50)
    available_sizes=models.CharField(max_length=30,choices=AvailableSize_choices)
    created_at=models.DateTimeField(default=datetime.now)
class Books_Sports_Hobbies(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    Description=models.CharField(max_length=255)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    photo=models.ImageField(upload_to="\static")
    author=models.CharField(max_length=50)
    publisher=models.CharField(max_length=50)
    isbn=models.IntegerField()
    created_at=models.DateTimeField(default=datetime.now)
class Services(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    Description=models.CharField(max_length=255)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    type=models.CharField(max_length=30,choices=type_choices,default='Electronics Repair')
    created_at=models.DateTimeField(default=datetime.now)
class PostClassifiedJob(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    ShortDescription=models.CharField(max_length=100)    
    photo=models.ImageField(upload_to="\static")
    LongDescription=models.CharField(max_length=255)
    created_at=models.DateTimeField(default=datetime.now)    
class Blogs_Articles(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    ShortDescription=models.CharField(max_length=100)    
    photo=models.ImageField(upload_to="\static")
    LongDescription=models.CharField(max_length=255)
    created_at=models.DateTimeField(default=datetime.now)
class NFT(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    current_price= models.DecimalField(max_digits=10, decimal_places=2)
    price_type=models.CharField(max_length=20)
    photo=models.ImageField(upload_to="\static")
    nft_link=models.CharField(max_length=50)
    nft_profile_link=models.CharField(max_length=70)
    details=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=datetime.now)





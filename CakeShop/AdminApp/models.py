from django.db import models

# Create your models here.
class Category(models.Model):
    Category_name=models.CharField(max_length=20)

    def __str__(self):
        return self.Category_name

class meta:
    db_table= "Category"

class Product(models.Model):
    size=models.FloatField(default=1)
    price=models.FloatField(default=200)
    p_name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    image=models.ImageField(default='abc.jpg',upload_to='Images')
    quantity=models.IntegerField()
    cat=models.ForeignKey(to='Category',on_delete=models.CASCADE)

    class Meta:
        db_table="Product"   
        
          
class UserInfo(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=20)

    class Meta:
        db_table="UserInfo"

class PaymentMaster(models.Model):
    cardnumber=models.CharField(max_length=30)
    cvv=models.CharField(max_length=3)
    balance=models.FloatField(default=1000)
    expiry=models.CharField(max_length=20)

    class Meta:
        db_table="PaymentMaster"
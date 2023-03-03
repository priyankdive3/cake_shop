from django.contrib import admin
from .models import Category,Product,UserInfo,PaymentMaster
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=("Category_name",)

class ProductAdmin(admin.ModelAdmin):
    list_display=("size","p_name","quantity","image","price","description","cat")

class UserInfoAdmin(admin.ModelAdmin):
    list_display=("username","email","password")

class PaymentMasterAdmin(admin.ModelAdmin):
    list_display=("cardnumber","cvv","balance","expiry")

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(PaymentMaster,PaymentMasterAdmin)

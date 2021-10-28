from django.db import models

# Create your models here.

class Product(models.Model):
    name =models.CharField(max_length=127,unique=True,blank=False,null=False)
    weight=models.DecimalField(max_digits=6,decimal_places=3,blank=False,null=False )
    price=models.PositiveIntegerField(blank=False,null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
# Create your models here.
USER=settings.AUTH_USER_MODEL

class HotelSave(models.Model):
    user            =models.ForeignKey(USER,on_delete=models.CASCADE)
    hotel           =models.ForeignKey("Hotel",on_delete=models.CASCADE)
    timestamp       =models.DateTimeField(auto_now_add=True)


class Hotel(models.Model):
    name            =models.CharField(max_length=254,blank=False,null=False)
    price           =models.CharField(max_length=254, blank=False, null=False)
    link            =models.CharField(max_length=2540, blank=False, null=False,unique=True)
    saved_by        =models.ManyToManyField(USER,through=HotelSave,related_name='saved_by',blank=True)

    class Meta:
        ordering=['-id']

    def serialize(self):
        x = {
            'name': self.name,
            'price': self.price,
            'link': self.link,
        }
        return x

    def __str__(self):
        return self.name
    @classmethod
    def create(cls,**kwargs):
        hotel=cls(
        name=kwargs['name'],
        price=kwargs['price'],
        link=kwargs['link'],
        )
        hotel.save()

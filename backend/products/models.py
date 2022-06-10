from django.db import models
from django.conf import settings
from django.db.models import Q

User = settings.AUTH_USER_MODEL



class ProductsQuerySet(models.QuerySet):
    
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        print(query, user)
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2= self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs


class ProductsManager(models.Manager):
    
    def get_queryset(self, *args, **kwargs):
        return ProductsQuerySet(self.model, using=self._db)
    
    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)


# Create your models here.
class Products(models.Model):

    # owner   = models.ForeignKey(User)
    user    = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title   = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price   = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public  = models.BooleanField(default=True)

    objects = ProductsManager()
    
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)

    def holiday_price(self):
        return "%.2f" %(float(self.price)*1.2)
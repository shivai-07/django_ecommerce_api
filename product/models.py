import uuid
from django.db import models

# Create your models here.
class ProductModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    manufacturerdate = models.DateField()
    rating = models.FloatField()
    imageurl = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "products"
        ordering = ['-createdAt']

        def __str__(self) -> str:
            return self.name

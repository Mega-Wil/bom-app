from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    """
    # Add any additional fields if necessary
    pass

class Product(models.Model):
    """
    Model representing a product in the bill of materials.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    serial_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    def get_bom_tree(self, level=0):
        """
        Recursively get the bill of materials tree for this product.
        """
        bom = []
        bom_items = BOMItem.objects.filter(parent=self)
        for item in bom_items:
            bom.append({
                'level': level,
                'component': item.component,
                'quantity': item.quantity,
            })
            # Recursively get the BOM for the component
            bom.extend(item.component.get_bom_tree(level + 1))
        return bom
    
class BOMItem(models.Model):
    """
    Model representing an item in the bill of materials.
    """
    parent = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bom_items')
    component = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='used_in_boms')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} OFF {self.component.name} in {self.parent.name}"
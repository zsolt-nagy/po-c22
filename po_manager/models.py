from django.db import models
from company_manager import models as company_models

# Create your models here.
class PurchaseOrder(models.Model):
    company_id = models.ForeignKey(company_models.Company, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    amount = models.FloatField()
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)

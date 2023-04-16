from django.db import models

class Transaction(models.Model):
    username=models.CharField(max_length=100,blank=False)
    tran_date = models.DateField("Transaction Date")
    tran_category = models.CharField("Transaction Category", max_length = 50)
    credit_amount = models.DecimalField("Credit Amount",max_digits=10, decimal_places = 5, default = 0)
    debit_amount = models.DecimalField("Debit Amount",max_digits=10, decimal_places = 5, default = 0)
    class Meta:
        db_table = "transactions"

    @property
    def is_credit_amount(self):
        return self.credit_amount>=0
# Create your models here.

from django.db import models

class Fraud(models.Model):
    name = models.CharField(max_length=50)
    account_no=models.CharField(max_length=20)
    ifsc_code=models.CharField(max_length=20)
    amount=models.CharField(max_length=10)
    transaction_id=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
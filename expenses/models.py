from django.db import models
# Create your models here.




class Expense(models.Model):
		class Categories(models.TextChoices):
				Groceries = "Groceries"
				Leisure = "Leisure"
				Electronics = "Electronics"
				Utilities = "Utilities"
				Clothing = "Clothing"
				Health = "Health"
				Others = "Others"


		category = models.CharField(max_length=50, choices=Categories.choices)
		amount = models.DecimalField(max_digits=10, decimal_places=2)
		date = models.DateField()	
		created_at = models.DateTimeField(auto_now_add=True, editable=False)
		description = models.TextField()


		def __str__(self):
				return f"{self.category} - {self.amount} - {self.created_at}"
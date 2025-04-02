from django.db import models


# Create your models here.

class toDoModel(models.Model):
      IMPORTANCE_CHOICES = [
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('High', 'High'),
       ]

      title=models.CharField(max_length=50)
      details=models.TextField(blank=True, null=True,max_length=100)
      completed=models.BooleanField(default=False)
      
      
      importance=models.CharField(max_length=10,choices=IMPORTANCE_CHOICES, default='Medium')
      


      def __str__(self):
            return self.title

      
      




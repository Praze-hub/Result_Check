from django.db import models
from user_profile.models import UserProfile


class Course(models.Model):
    GRADE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    ]
    name = models.CharField(max_length=255, null=True)
    grade = models.CharField(max_length=1, choices = GRADE_CHOICES, null=True)
    credit_units = models.PositiveIntegerField(null = True)
    
    def grade_point(self):
        grade_mapping = {'A':5.0,'B':4.0,'C':3.0,'D':2.0,'E':1.0,'F':0.0}
        return grade_mapping.get(self.grade, 0.0)


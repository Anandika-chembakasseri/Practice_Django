from django.db import models
from django.core.validators import RegexValidator


class Registration(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    COURSE_CHOICES = [
        ('dm', 'Digital Marketing'),
        ('py', 'Python Fullstack'),
        ('bd', 'Business Development'),
        ('da', 'Data Analyst'),
        ('react', 'React Developer'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # store hashed password ideally

    dob = models.DateField(verbose_name="Date of Birth")

    mobile = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[0-9]{10}$',
                message='Mobile number must be 10 digits.'
            )
        ]
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    course = models.CharField(
        max_length=20,
        choices=COURSE_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

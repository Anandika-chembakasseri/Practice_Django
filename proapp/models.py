# your_app/models.py
from django.db import models
from django.core.validators import RegexValidator

class Registration(models.Model):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    COURSE_CHOICES = [
        ("sel", "Select one course"),
        ("dm", "Digital Marketing"),
        ("py", "Python Fullstack"),
        ("bd", "Business Development"),
        ("da", "Data Analyst"),
        ("react", "React Developer"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    mobile = models.CharField(
        max_length=10,
        unique=True,
        validators=[RegexValidator(r"^\d{10}$", "Enter a valid 10-digit mobile number.")],
        help_text="10-digit mobile number",
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    course = models.CharField(max_length=20, choices=COURSE_CHOICES, default="sel")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

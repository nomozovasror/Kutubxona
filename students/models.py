from django.db import models

# Create your models here.


from django.db import models


class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    parent = models.IntegerField()

    # StructureType field
    structure_type_code = models.CharField(max_length=255)
    structure_type_name = models.CharField(max_length=255)

    # LocalityType field
    locality_type_code = models.CharField(max_length=255)
    locality_type_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)  # Add fields for first, second, and third names
    second_name = models.CharField(max_length=100)
    third_name = models.CharField(max_length=100)
    image = models.URLField()  # Assuming the image is a URL
    student_id_number = models.CharField(max_length=20)
    birth_date = models.DateField()
    avg_gpa = models.DecimalField(max_digits=5, decimal_places=2)
    total_credit = models.DecimalField(max_digits=8, decimal_places=2)  # Adjust the max_digits as needed
    gender = models.CharField(max_length=20)  # You can create a Gender model if needed
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    specialty_id = models.CharField(max_length=10)  # Assuming specialty_id is a string
    group_id = models.CharField(max_length=10)  # Assuming group_id is a string
    education_year_code = models.CharField(max_length=10)  # Assuming education_year_code is a string
    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    citizenship = models.CharField(max_length=100)
    semester_id = models.CharField(max_length=10)  # Assuming semester_id is a string
    level = models.CharField(max_length=50)
    education_form = models.CharField(max_length=50)
    education_type = models.CharField(max_length=50)
    payment_form = models.CharField(max_length=50)
    student_type = models.CharField(max_length=50)
    social_category = models.CharField(max_length=50)
    accommodation = models.CharField(max_length=50)
    student_status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hash = models.CharField(max_length=255)  # Assuming 'hash' is a string

    def __str__(self):
        return self.full_name

from django.db import models
from faker import Faker


class Student(models.Model):
    first_name = models.CharField(max_length=15, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, email: {self.email}'

    @classmethod
    def generate_student(cls):
        faker = Faker()

        student = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
        )

        student.save()

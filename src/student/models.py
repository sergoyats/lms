import random

from django.db import models

from faker import Faker

from group.models import Group


class Student(models.Model):
    first_name = models.CharField(max_length=15, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=20, null=True, db_index=True)
    telephone = models.CharField(max_length=20, default=None, unique=True, null=True)
    group = models.ForeignKey(
        to=Group,
        null=True,
        on_delete=models.SET_NULL,
        db_constraint=True,
        related_name='students'
    )

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}, email: {self.email}, tel.: {self.telephone}'

    @classmethod
    def generate_student(cls, groups=None):
        faker = Faker()
        if groups is None:
            groups = list(Group.objects.all())

        student = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            telephone=faker.phone_number(),
            group=random.choice(groups)
        )

        student.save()

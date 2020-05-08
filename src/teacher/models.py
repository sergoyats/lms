from django.db import models

from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=15, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=20, null=True)
    telephone = models.CharField(max_length=20, default=380966666666, unique=True, null=False)
    github_repository = models.URLField(max_length=100, null=True)
    experience = models.PositiveIntegerField(default=2, null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name},' \
               f' email: {self.email}, tel.: {self.telephone},' \
               f' experience: {self.experience} years'

    @classmethod
    def generate_teacher(cls):
        faker = Faker()

        teacher = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            telephone=faker.phone_number(),
        )

        teacher.save()

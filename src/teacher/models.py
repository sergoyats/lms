from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=15, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=20, null=True)
    telephone = models.CharField(max_length=15, null=False)
    github_repository = models.URLField(max_length=100, null=True)
    experience = models.PositiveIntegerField(default=2, null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, tel.: {self.telephone}, experience: {self.experience} years'

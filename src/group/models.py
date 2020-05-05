from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=15, null=False)
    specialty = models.CharField(max_length=30, null=False)
    students_number = models.PositiveIntegerField(default=25, null=True)

    def __str__(self):
        return f'{self.name}, {self.specialty}, {self.students_number} students'

from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Todo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    priority = models.Choices(high,low)
    completed = models.BooleanField()
    created_by = models.CharField(max_length=200)
    created_at = models.TimeField()
    due_by = models.DateField()
    category = models.Choices()

    def __str__(self):
        return self.name

class Categories(models.Model):
    type = models.CharField(primary_key=True)
    due = models.DateField()
    completed = models.BooleanField()

    def __str__(self):
        return self.label

class Events(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    when = models.DateTimeField()
    status = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)

    def __str__(self):
        return self.name
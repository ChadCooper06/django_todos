from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name


class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=200, default='Tasks')

    def __str__(self):
        return self.label

class Todo(models.Model):

    HIGH = 'H'
    NORMAL = 'N'
    LOW = 'L'
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (NORMAL, 'Normal'),
        (LOW, 'Low'),
    ]
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=200, blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateField('Date created', auto_now_add=True)
    due_by = models.DateField('Due Date', auto_now=False)
    category = models.ManyToManyField(Categories, blank=True)
    priority_choices = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default=NORMAL,
    )

    def __str__(self):
        return self.name


class Events(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    start = models.DateTimeField('Start Date', auto_now=False)
    end = models.DateTimeField('End Date', auto_now=False)
    status = models.CharField(max_length=200, blank=False, null=False)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        blank=False, 
        null=False
        )

    def __str__(self):
        return self.name
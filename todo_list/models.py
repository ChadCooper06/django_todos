from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Todo(models.Model):

    id = models.ManyToManyField(User, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField('Date created', auto_created=True)
    due_by = models.DateField('Due Date', auto_now=False)
    category = models.ManyToManyField(Categories, on_delete=models.CASCADE)

    HIGH = 'H'
    NORMAL = 'N'
    LOW = 'L'
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (NORMAL, 'Normal'),
        (LOW, 'Low'),
    ]
    priority_choices = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default=NORMAL,
    )

    def __str__(self):
        return self.name

class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.ManyToManyField(
        Todos,
        setdefault=null,
        )

    def __str__(self):
        return self.label

class Events(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    start = models.DateTimeField(default='date')
    end = models.DateTimeField(default='date')
    status = models.CharField(max_length=200)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.name
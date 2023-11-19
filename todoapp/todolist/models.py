from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField('Название задачи', max_length=500)
    is_complete = models.BooleanField('Задача закрыта', default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
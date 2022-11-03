from django.db import models

# Create your models here.

class HomeBg(models.Model):
    img = models.ImageField('Home bg', upload_to='media')


class Post(models.Model):
    name = models.CharField('Post name', max_length=40)
    img = models.ImageField('Post image', upload_to='media')
    about = models.TextField('Post text')
    date = models.DateTimeField('Post date')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

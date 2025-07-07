from django.db import models

class Films_post(models.Model):
    title = models.CharField('Название фильма', max_length=150)
    description = models.TextField('Описание описание')
    comments = models.TextField('Отзывы о фильме')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title
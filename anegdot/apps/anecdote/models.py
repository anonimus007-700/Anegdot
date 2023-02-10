from django.db import models

class Anecdote(models.Model):
    anecdot_title = models.CharField('Ім\'я гуморески', max_length=200)
    anecdot_text = models.TextField('Текст гуморески')

    def __str__(self):
        return self.anecdot_title
    
    class Meta:
        verbose_name = 'Анегдот'
        verbose_name_plural = 'Анегдоти'
    
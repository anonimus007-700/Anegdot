from django.db import models

class Offer(models.Model):
    offer_text = models.TextField('Питання або пропозиція')
    
    def __str__(self):
        return self.offer_text
    
    class Meta:
        verbose_name = 'Питання'
        verbose_name_plural = 'Питання'

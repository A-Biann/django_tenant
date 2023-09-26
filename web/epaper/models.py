# epaper/models.py

from django.db import models

# Create your models here.

class EPaperEmail(models.Model):
    '''
    epaper mailbox
    '''
    email = models.EmailField('E-mail', max_length=255)
    
    class Meta:
        verbose_name = 'epaper subscribe mail'
        verbose_name_plural = 'epaper subscribe mails'

    def __str__(self):
        return f'{self.email}'
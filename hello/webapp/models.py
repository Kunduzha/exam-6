from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
status_choice=[('active', 'активно'), ('blocked', 'заблокировано')]
class Comments(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="name")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='email')
    comment = models.CharField(max_length=3000, null=True, blank=True, verbose_name='comment')
    status = models.TextField(null=False, blank=False, choices=status_choice,  verbose_name='status', default='active')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated_at')

    class Meta:
        db_table ='comments'
        verbose_name ='Комментарий'
        verbose_name_plural ='Комментарии'


    def __str__(self):
        return f'{self.id}. {self.name}:{self.comment}'



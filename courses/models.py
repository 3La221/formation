from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.



class Formation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=True , blank=True) 
    desc = models.TextField(null=True , blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    localisation = models.CharField(max_length=120 , null=True , blank=True) 
    cout = models.IntegerField(default=1000)
    image = models.ImageField(default='default_img.jpg',upload_to='formation_images/', null=True, blank=True)
    top = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
    
    
    
class Etudiant(AbstractUser):
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(unique=True, null=True)
    numero_tel = models.CharField(max_length=12 , null=True , blank=True)
    address = models.CharField(max_length=30 , null=True , blank=True)
    niveau = models.CharField(max_length=30 , null=True , blank=True)
    
    PASSWORD_FIELD = 'password'
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Insc(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 , editable=False)
    formation_id = models.UUIDField()
    etudiant_id = models.IntegerField() 
    confirmed = models.BooleanField(default=False)
    
    
    def __str__(self) -> str:
        
        return f'{self.etudiant_id} {self.formation_id}'

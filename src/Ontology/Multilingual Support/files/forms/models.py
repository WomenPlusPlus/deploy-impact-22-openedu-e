import datetime

from django.db import models
from django.utils import timezone

from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _

# Create your models here.
  

    
class Resource(TranslatableModel):
    translations = TranslatedFields(
        title_text = models.CharField(max_length=100),
        description = models.TextField(),
        url = models.CharField(max_length=100),
    )
    pub_date = models.DateTimeField('date published', default = timezone.now())
    
    class Level(models.TextChoices):
    	BEGINNER = 'be',_('Beginner')
    	INTERMEDIATE = 'in',_('Intermediate')
    	ADVANCED = 'ad',_('Advanced')
    	MULTIPLE = 'mu',_('Multiple')
    	
    level = models.CharField(max_length=2,choices=Level.choices,)
    def get_level(self) -> Level:
        return self.Level(self.level).label
        
    level_label = property()
    level_label = level_label.getter(get_level)
    
    class Key_Competences(models.IntegerChoices):
    	LITERACY = 1,_('Literacy')
    	MULTILINGUAL = 2,_('Multilingual')
    	MATH = 3,_('Mathematical, science, technology, engineering')
    	DIGITAL = 4,_('Digital')
    	PERSONAL = 5,_('Personal, social, learning to learn')
    	CITIZENSHIP = 6,_('Citizenship')
    	ENTREPRENEURSHIP = 7,_('Entrepreneurship')
    	CULTURAL = 8,_('Cultural awareness and expression')

    key_competence = models.IntegerField(choices=Key_Competences.choices,)
    def get_key_competence(self) -> Level:
        return self.Key_Competences(self.key_competence).label
        
    key_competence_label = property()
    key_competence_label = key_competence_label.getter(get_key_competence)

    def __str__(self):
        return self.title_text
        
        
        
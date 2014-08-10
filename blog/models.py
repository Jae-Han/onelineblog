from django.db import models

# Create your models here.
class Article(models.Model):
    content = models.CharField(max_length=200)
    written_date = models.DateTimeField('data written')
    def __unicode__(self):
        return self.content

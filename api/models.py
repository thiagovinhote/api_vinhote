from django.db import models

class Project(models.Model):
  
  name = models.CharField(max_length = 100, null = False)
  description = models.CharField(max_length = 500, blank = True, null = False)
  image = models.FileField(upload_to = 'project', blank = True, null = True)

  class Meta:
    verbose_name = u'Project'
    verbose_name_plural = u'Projects'

  def __str__(self):
    return self.name

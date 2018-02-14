from django.db import models
from django.utils.translation import ugettext_lazy as _
from .constants import LINK_TYPES, Link_Types

class Project(models.Model):
  
  name = models.CharField(max_length = 100, null = False)
  description = models.CharField(max_length = 500, blank = True, null = False)
  image = models.FileField(upload_to = 'project', blank = True, null = True)

  class Meta:
    verbose_name = u'Project'
    verbose_name_plural = u'Projects'

  def __str__(self):
    return self.name

  def links(self):
    return Link.objects.filter(project = self)


class Link(models.Model):
  
  type = models.IntegerField(
    _('link_type'),
    choices = LINK_TYPES,
    default = Link_Types.none,
  )
  url = models.CharField(max_length = 250, blank = False, null = False)
  project = models.ForeignKey(Project, null = False, blank = False, on_delete = models.CASCADE)

  class Meta:
    verbose_name = u'Link'
    verbose_name_plural = u'Links'

  def __str__(self):
    return '%s - %s'%(self.type, self.url)
    

class Job(models.Model):
  
  description = models.CharField(max_length = 500, null = False)
  image = models.FileField(upload_to = 'job', blank = False, null = False)

  class Meta:
    verbose_name = u'Job'
    verbose_name_plural = u'Work'

  def __str__(self):
    return self.description

from django.db import models
from django.utils.translation import ugettext_lazy as _
from .constants import LINK_TYPES, Link_Types

class Project(models.Model):
  
  name = models.CharField('nome', max_length = 100, null = False)
  description = models.CharField('descrição', max_length = 500, blank = True, null = False)
  image = models.FileField('imagem', upload_to = 'project', blank = True, null = True)

  class Meta:
    verbose_name = u'Project'
    verbose_name_plural = u'Projects'

  def __str__(self):
    return self.name

  def links(self):
    return Link.objects.filter(project = self)


class Link(models.Model):
  
  type = models.IntegerField(
    'tipo',
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
  
  name = models.CharField('nome', max_length = 100, default = '', blank = False, null = False)
  description = models.CharField('descrição', max_length = 500, null = False)
  image = models.FileField('imagem', upload_to = 'job', blank = False, null = False)
  
  is_store = models.BooleanField('na loja', default = False, blank = True)
  link_store = models.CharField('link da loja', max_length = 200, default = '', blank = True, null = True)

  class Meta:
    verbose_name = u'Job'
    verbose_name_plural = u'Work'

  def __str__(self):
    return self.description


class Experience(models.Model):
  
  role = models.CharField('cargo', max_length = 100, blank = False, null = False)
  company = models.CharField('empresa', max_length = 100, blank = False, null = False)
  from_date = models.DateField('de', blank = False, null = False)
  to_date = models.DateField('até', blank = False, null = False)

  class Meta:
    verbose_name = u'Experience'
    verbose_name_plural = u'Experiences'

  def __str__(self):
    return '%s - [%s - %s]'%(self.role, self.from_date, self.to_date)

  def days_time(self):
    return (self.to_date - self.from_date).days


class Skill(models.Model):
  
  name = models.CharField('nome', max_length = 100, blank = False, null = False)
  description = models.CharField('descrição', max_length = 500, blank = False, null = False)
  image = models.FileField('imagem', upload_to = 'skill', blank = True, null = True)

  class Meta:
    verbose_name = 'Skill'
    verbose_name_plural = 'Skills'

  def __str__(self):
    return self.name

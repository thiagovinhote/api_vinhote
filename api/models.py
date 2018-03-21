from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import (
  AbstractBaseUser,
  BaseUserManager
)

from .constants import LINK_TYPES, Link_Types

class UserManager(BaseUserManager):
  def _create_user(self, email, password,
                    is_staff, is_superuser, **extra_fields):
      now = timezone.now()
      if not email:
          email = self.normalize_email(email)
          raise ValueError('The given email must be set')
      
      user = self.model(email=email,
                        is_staff=is_staff, is_active=True,
                        is_superuser=is_superuser, last_login=now,
                        date_joined=now, password=password, **extra_fields)
      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_user(self, email, password=None, **extra_fields):
      return self._create_user(email, password, False, False,
                                **extra_fields)

  def create_user(self, username, email=None, password=None, **extra_fields):
      """
      This override is necessary to Python Social Auth plugin works. This method
      just receive username and after ignore it.
      """
      if email == "":
          logger.error("Inside create user:" + username)
          email = username
      return self._create_user(email, password, False, False,
                              **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
      return self._create_user(email, password, True, True,
                                **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), unique = True, max_length = 30)
    email = models.EmailField(_('email address'), unique = True)
    first_name = models.CharField(_('first name'), max_length = 30, blank = True)
    last_name = models.CharField(_('last name'), max_length=30, blank = True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add = True)
    is_active = models.BooleanField(_('active'), default = True)
    is_staff = models.BooleanField(_('staff'), default = False)
    is_superuser = models.BooleanField(_('superuser'), default = False)
    avatar = models.FileField('avatar', upload_to = 'avatar/', null = True, blank = True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Project(models.Model):
  
  name = models.CharField('nome', max_length = 100, null = False)
  description = models.CharField('descrição', max_length = 500, blank = True, null = False)
  image = models.FileField('imagem', upload_to = 'project', blank = True, null = True)

  class Meta:
    verbose_name = u'Projetos'
    verbose_name_plural = u'Projetos'

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
    return '%s - %s | %s'%(self.type, self.url, self.project.name)
    

class Job(models.Model):
  
  name = models.CharField('nome', max_length = 100, default = '', blank = False, null = False)
  description = models.CharField('descrição', max_length = 500, null = False)
  image = models.FileField('imagem', upload_to = 'job', blank = True, null = True)
  
  is_store = models.BooleanField('na loja', default = False, blank = True)
  link_store = models.CharField('link da loja', max_length = 200, default = '', blank = True, null = True)

  class Meta:
    verbose_name = u'Trabalho'
    verbose_name_plural = u'Trabalhos'

  def __str__(self):
    return self.description


class Experience(models.Model):
  
  role = models.CharField('cargo', max_length = 100, blank = False, null = False)
  company = models.CharField('empresa', max_length = 100, blank = False, null = False)
  from_date = models.DateField('de', blank = False, null = False)
  to_date = models.DateField('até', blank = False, null = False)

  class Meta:
    verbose_name = u'Experiência'
    verbose_name_plural = u'Experiências'

  def __str__(self):
    return '%s - [%s - %s]'%(self.role, self.from_date, self.to_date)

  def days_time(self):
    return (self.to_date - self.from_date).days


class Skill(models.Model):
  
  name = models.CharField('nome', max_length = 100, blank = False, null = False)
  description = models.CharField('descrição', max_length = 500, blank = False, null = False)
  image = models.FileField('imagem', upload_to = 'skill', blank = True, null = True)

  class Meta:
    verbose_name = 'Habilidade'
    verbose_name_plural = 'Habilidades'

  def __str__(self):
    return self.name


class Certificate(models.Model):

  category = models.CharField('categoria', max_length = 50, blank = False, null = False)
  holder = models.CharField('titular', max_length = 100, blank = False, null = False)
  date_conclusion = models.DateField('data de conclusão', blank = False, null = False)
  course = models.CharField('curso', max_length = 150, blank = False, null = False)
  school = models.CharField('escola', max_length = 150, blank = False, null = False)

  def __str__(self):
    return '%s - %s'%(self.course, self.category)

  class Meta:
    verbose_name = 'Certificado'
    verbose_name_plural = 'Certificados'

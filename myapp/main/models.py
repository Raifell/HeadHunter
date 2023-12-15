from django.contrib.auth.models import User
from django.db import models
from pytils.translit import slugify


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True)
    title = models.CharField('Title', max_length=255)
    name = models.CharField('Name', max_length=255)
    surname = models.CharField('Surname', max_length=255)
    patronymic = models.CharField('Patronymic', max_length=255)
    birthdate = models.DateField('Birth Date')
    email = models.EmailField('Mail', unique=True)
    skills = models.TextField('Skill')
    experience = models.TextField('Exp')
    education = models.TextField('Education')
    slug = models.CharField('Slug', max_length=255, unique=True, null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify('{}-{}'.format(self.name, self.surname))
        super(Resume, self).save(force_insert, force_update, using, update_fields)


class Vacancy(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True)
    name = models.CharField('Name', max_length=255)
    company = models.CharField('Company', max_length=255)
    salary = models.PositiveIntegerField('Salary')
    skill = models.TextField('Skills')
    duty = models.TextField('Duty')
    address = models.CharField('Address', max_length=255)
    slug = models.CharField('Slug', max_length=255, unique=True, null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify('{}-{}'.format(self.name, self.company))
        super(Vacancy, self).save(force_insert, force_update, using, update_fields)

from django.db import models
from django.utils.text import slugify


class Human(models.Model):
    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=50)
    age = models.PositiveIntegerField('Age')

    class Meta:
        abstract = True
        ordering = ['id']


class KidParent(Human):
    slug = models.SlugField(max_length=255, null=True, unique=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify('parent-{}-{}'.format(self.name, self.surname))
        super().save(force_insert, force_update, using, update_fields)

    def get_absolute_url(self):
        return 'info/{}'.format(self.slug)

    def __str__(self):
        return '{} - {}'.format(self.name, self.surname)


class Kid(Human):
    parent = models.ForeignKey('KidParent', on_delete=models.CASCADE, null=True, verbose_name='Parent')
    slug = models.SlugField(max_length=255, null=True, unique=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify('kid-{}-{}'.format(self.name, self.surname))
        super().save(force_insert, force_update, using, update_fields)

    def get_absolute_url(self):
        return 'info/{}'.format(self.slug)

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.surname, self.parent)


class Icecream(models.Model):
    name = models.CharField('Name', max_length=150)
    slug = models.SlugField(max_length=255, null=True, unique=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify('icecream-{}'.format(self.name))
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return 'info/{}'.format(self.slug)


class IcecreamShop(models.Model):
    name = models.CharField('Name', max_length=150)
    icecream = models.ManyToManyField('Icecream', related_name='ice')
    slug = models.SlugField(max_length=255, null=True, unique=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify('shop-{}'.format(self.name))
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '{} - {}'.format(self.name, self.icecream.all())

    def get_absolute_url(self):
        return 'info/{}'.format(self.slug)


class IcecreamSale(models.Model):
    date = models.DateField()
    buyer = models.ForeignKey('Kid', on_delete=models.CASCADE, null=True, verbose_name='Kid')
    icecream = models.ForeignKey('Icecream', on_delete=models.CASCADE, null=True, verbose_name='Icecream')
    slug = models.SlugField(max_length=255, null=True, unique=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify('sale-{}-{}'.format(self.buyer, self.icecream))
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '{} - {} - {}'.format(self.date, self.buyer, self.icecream)

    def get_absolute_url(self):
        return 'info/{}'.format(self.slug)

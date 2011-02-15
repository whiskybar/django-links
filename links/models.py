from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(default='', blank=True)
    ordering = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('ordering',)
        verbose_name_plural = 'categories'

class Link(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField(verify_exists=False, null=True, blank=True)
    description = models.TextField(default='', blank=True)
    ordering = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('category__ordering', 'ordering',)

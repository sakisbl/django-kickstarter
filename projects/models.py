from django.db import models
from django.conf import settings
from django.urls import reverse
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField
from categories.models import Category


class Project(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    short_description = models.TextField()
    description = HTMLField()
    cover_image = models.ImageField(upload_to='projects/%Y/%m/%d')
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    amountRaised = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    finish = models.DateField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('single_project', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']

from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class TastingNote(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', blank=True)
    name = models.TextField(blank=False)
    wtype = models.TextField(blank=False)
    region = models.TextField(blank=False)
    tag = models.TextField(blank=True)

    slug = models.SlugField(max_length=250)

    content = RichTextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(TastingNote, self).save(*args, **kwargs)


class Comment(models.Model):

    note = models.ForeignKey(TastingNote, on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=False, max_length=140)
    name = models.TextField(blank=True, max_length=32)
    
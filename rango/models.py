from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True) 
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    #The field name has been set to unique, meaning that every category name must be unique. This means that you can use the field as a primary key.
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Categories'
        #Note the typo within the admin interface (Categorys, not Categories).
    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #CASCADE instructs Django to delete the pages associated with the category when the category is deleted
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    #provided a __str__() method to return a meaningful value when a string representation of a UserProfile model instance is requested.
    def __str__(self):
        return self.user.username
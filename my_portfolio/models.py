from django.db import models
from django.utils.text import slugify


class Technology(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS = ((1, 'Draft'),
              (2, 'Live'))
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ManyToManyField(Category, related_name='project_category')
    visit_number = models.PositiveIntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=1)
    github_link = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    requirement = models.TextField()
    website_link = models.CharField(max_length=255, null=True, blank=True)
    technology = models.ManyToManyField(Technology, related_name='Project_technology', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    img = models.ImageField(upload_to='project/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_image')
    is_thumbnail = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}: {self.project.title}"

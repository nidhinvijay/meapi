from django.db import models

class Link(models.Model):
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    portfolio = models.URLField(blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=64, unique=True)
    def __str__(self): return self.name

class Profile(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    education = models.TextField()
    skills = models.ManyToManyField(Skill, blank=True, related_name="profiles")
    links = models.OneToOneField(Link, on_delete=models.CASCADE, null=True, blank=True)

class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    links = models.JSONField(default=dict, blank=True)
    skills = models.ManyToManyField(Skill, related_name="projects", blank=True)

class Work(models.Model):
    company = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="work")

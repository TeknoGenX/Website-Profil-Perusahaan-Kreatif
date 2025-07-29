from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    description = models.TextField()

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/')
    description = models.TextField()

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team/')
    bio = models.TextField()

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    feedback = models.TextField()
    company = models.CharField(max_length=100)

class CompanyInfo(models.Model):
    company_name = models.CharField(max_length=200)
    about = models.TextField()
    logo = models.ImageField(upload_to='logo/')
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    map_embed = models.TextField(help_text="Google Maps Embed Code")

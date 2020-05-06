from django.db import models
from ckeditor.fields import RichTextField


# Articles
class Section(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Article(models.Model):
    category = models.ForeignKey(Section, on_delete=models.CASCADE)
    createDate = models.DateField()
    modifyDate = models.DateField(blank=True)
    homepageDisplay = models.BooleanField()
    title = models.CharField(max_length=150)
    text = RichTextField()
    imageTitle = models.ImageField(upload_to='articles/images/')
    imageTitleCaption = models.CharField(max_length=300, blank=True)
    image2 = models.ImageField(upload_to='articles/images/', blank=True)
    image2Caption = models.CharField(max_length=300, blank=True)
    image3 = models.ImageField(upload_to='articles/images/', blank=True)
    image3Caption = models.CharField(max_length=300, blank=True)
    image4 = models.ImageField(upload_to='articles/images/', blank=True)
    image4Caption = models.CharField(max_length=300, blank=True)
    image5 = models.ImageField(upload_to='articles/images/', blank=True)
    image5Caption = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title


# Member list
class MemberType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Member(models.Model):
    type = models.ForeignKey(MemberType, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, blank=True)
    website = models.URLField(max_length=150, blank=True)
    pobox = models.CharField(max_length=150, blank=True)
    town = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name


# Newsletter
class Newsletter(models.Model):
    image = models.ImageField(upload_to='articles/images/')
    issue = models.IntegerField()
    year = models.IntegerField()
    file = models.FileField(upload_to='articles/images/')


class NewsletterSubscriber(models.Model):
    email = models.EmailField(max_length=150, unique=True)

    def __str__(self):
        return self.email


# Job adverts
class JobPost(models.Model):
    name = models.CharField(max_length=200)
    postDate = models.DateField()
    jobFile = models.FileField(upload_to='articles/images/')

    def __str__(self):
        return self.name


# AWAC Registration
class AwacRegistration(models.Model):
    name = models.CharField(max_length=150)
    organisation = models.CharField(max_length=150, blank=True)
    position = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=150, unique=True)
    phone = models.CharField(max_length=20, blank=True)
    atawasmember = models.BooleanField(null=True, blank=True, verbose_name="Are you a member of ATAWAS?")
    organisationatawasmember = models.BooleanField(null=True, blank=True, verbose_name="Is your organisation a member of ATAWAS?")
    exhibitor = models.BooleanField(null=True, blank=True, verbose_name="Would you also like to be an exhibitor?")

    def __str__(self):
        return self.name

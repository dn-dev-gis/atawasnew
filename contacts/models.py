from django.db import models
from django.urls import reverse

class OrganisationType(models.Model):
    orgType = models.CharField(max_length=100)

    def __str__(self):
        return self.orgType

class Group(models.Model):
    group = models.CharField(max_length=200)

    def __str__(self):
        return self.group

class Organisation(models.Model):
    orgType = models.ForeignKey(OrganisationType, on_delete=models.CASCADE)
    orgName = models.CharField(max_length=200)
    orgNameShort = models.CharField(max_length=50, blank=True)
    phone1 = models.CharField(max_length=20, blank=True)
    phone2 = models.CharField(max_length=20, blank=True)
    phone3 = models.CharField(max_length=20, blank=True)
    phone4 = models.CharField(max_length=20, blank=True)
    phone5 = models.CharField(max_length=20, blank=True)
    phone6 = models.CharField(max_length=20, blank=True)
    phone7 = models.CharField(max_length=20, blank=True)
    email1 = models.EmailField(max_length=50, blank=True)
    email2 = models.EmailField(max_length=50, blank=True)
    email3 = models.EmailField(max_length=50, blank=True)
    email4 = models.EmailField(max_length=50, blank=True)
    email5 = models.EmailField(max_length=50, blank=True)
    website = models.URLField(max_length=100, blank=True)
    pobox = models.CharField(max_length=20, blank=True)
    town = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    comment = models.TextField(blank=True)
    group = models.ManyToManyField(Group, blank=True)

    def __str__(self):
        return self.orgName

    def getGroup(self):
        return self.group.group


class Person(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, blank=True)
    lastName = models.CharField(max_length=100)
    firstNames = models.CharField(max_length=100, blank=True)
    phone1 = models.CharField(max_length=20, blank=True)
    phone2 = models.CharField(max_length=20, blank=True)
    phone3 = models.CharField(max_length=20, blank=True)
    phone4 = models.CharField(max_length=20, blank=True)
    phone5 = models.CharField(max_length=20, blank=True)
    phone6 = models.CharField(max_length=20, blank=True)
    phone7 = models.CharField(max_length=20, blank=True)
    email1 = models.EmailField(max_length=50, blank=True)
    email2 = models.EmailField(max_length=50, blank=True)
    email3 = models.EmailField(max_length=50, blank=True)
    email4 = models.EmailField(max_length=50, blank=True)
    email5 = models.EmailField(max_length=50, blank=True)
    pobox = models.CharField(max_length=20, blank=True)
    town = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=200, blank=True)
    comment = models.TextField(blank=True)
    group = models.ManyToManyField(Group, blank=True)

    def __str__(self):
        return self.lastName

    def getOrganisation(self):
        return self.organisation.orgName

    def getGroup(self):
        return self.group.group

    # def get_absolute_url(self):
    #     return reverse('post_detail', args=[str(self.id)])

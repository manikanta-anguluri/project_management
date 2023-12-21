from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    found_date = models.DateField()
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Companies'
        ordering = ('name',)

    def __str__(self):
        return (self.name)


class UserProfile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    img    = models.ImageField(default="blank_profile.png",blank=True,null=True)

    def __str__(self):
        return (str(self.user))
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.safestring import mark_safe

class Shelter(models.Model):
    name = models.CharField(max_length=264)
    email = models.EmailField()
    page_link = models.CharField(max_length=264, default="none")
    shelter_logo = models.ImageField(upload_to='my_app/shelters', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('my_app:detail', kwargs={'pk': self.pk})

    def return_image_tag(self):
        return mark_safe('<img src="{}"'.format(self.shelter_logo))


class Dog(models.Model):
    shelter = models.ForeignKey(Shelter, related_name='dogs', on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    breed = models.CharField(max_length=264, default="None")
    dog_logo = models.ImageField(upload_to='my_app/dogs', blank=True, null=True)

    def __str__(self):
        return self.name


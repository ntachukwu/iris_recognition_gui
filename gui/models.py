import sys, subprocess
from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class EnrollModel(models.Model):
    name = models.CharField(max_length=20)
    no_files = models.IntegerField(default=0)
    enrollment_time = models.FloatField(default=0.0)

    def __str__(self):
        return self.name



class Profile(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    MARITAL = (
        ('Married', 'Married'),
        ('Single', 'Single')
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=GENDER, default=1)
    about_me = models.TextField()
    marital_status = models.CharField(max_length=10, choices=MARITAL, default=2)
    hobbies = models.TextField()
    profile_iris_image = models.ImageField()
    profileMatFileName = models.CharField(max_length=20, help_text=_("Leave this blank"), blank=True)

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)



@receiver(post_save, sender=Profile)
def update_profile_mat_file(sender, instance, **kwargs):

    media_location = instance.profile_iris_image.url

    path = '//{}//{}'.format(settings.BASE_DIR, "enroll_profile_image.py")

    path_to_image = '//{}'.format(settings.BASE_DIR) + media_location

    out = subprocess.run(
        [sys.executable, path, path_to_image], shell=False, stdout=subprocess.PIPE)

    result = out.stdout.decode("utf-8")
    instance.profileMatFileName = result[:3]
    post_save.disconnect(update_profile_mat_file, sender=Profile)
    instance.save()
    post_save.connect(update_profile_mat_file, sender=Profile)

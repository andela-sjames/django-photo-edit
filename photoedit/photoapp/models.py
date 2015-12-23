import os
from time import time

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User


def get_upload_file_name(instance, filename):
    return "upload_files/user_{0}/{1}_{2}" .format(
        instance.user.id,
        str(time()).replace('.', '_'),
        filename
    )


class FacebookUser(models.Model):

    '''Model Associates Facebook user to django user for keeping
    sessions.'''

    facebook_id = models.CharField(max_length=60, unique=True)

    # Keep track of the facebook user -> django user mapping
    contrib_user = models.OneToOneField(User, related_name='user')
    contrib_picture = models.TextField()

    def __unicode__(self):
        return "%s %s" % (self.contrib_user.first_name,
                          self.contrib_user.last_name)


class Photo(models.Model):

    ''' Model holds a reference to cloudinary-stored
        image and contains some metadata about the image.'''

    title = models.CharField(
        "Title (optional)",
        max_length=60,
        blank=True,
        null=True)

    image = models.ImageField(upload_to=get_upload_file_name,
                              blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return "Photo <%s:%s>" % (self.title, self.id)

    class Meta:
        ordering = ('-created',)


@receiver(post_delete, sender=Photo)
def delete_from_file_system(sender, instance, **kwargs):

    path = instance.image.path

    filepath, ext = os.path.splitext(path)
    delete_path = filepath + 'edited' + ext

    if os.path.exists(delete_path):
        os.remove(delete_path)
        os.remove(path)

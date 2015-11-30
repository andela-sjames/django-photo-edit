from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from cloudinary.models import CloudinaryField

# Create your models here.
class FacebookUser(models.Model):
    facebook_id = models.CharField(max_length=100, unique=True)
    
    # Keep track of the facebook user -> django user mapping
    contrib_user = models.OneToOneField(User,related_name='user')
    contrib_picture = models.URLField()

    def __unicode__(self):
        return "%s %s" % (self.contrib_user.first_name, self.contrib_user.last_name)

class Photo(models.Model):

    ''' Model holds a reference to cloudinary-stored
        image and contains some metadata about the image.'''

    title = models.CharField("Title (optional)", max_length=60, blank=True, null=True)
    image = CloudinaryField(
        resource_type='image',
        type='upload',
        blank=True,
        default="img/photo_default.png",
    )
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)
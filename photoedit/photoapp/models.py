from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FacebookUser(models.Model):
    facebook_id = models.CharField(max_length=100, unique=True)
    
    # Keep track of the facebook user -> django user mapping
    contrib_user = models.OneToOneField(User,related_name='user')
    contrib_picture = models.URLField()

    def __unicode__(self):
        return "%s %s" % (self.contrib_user.first_name, self.contrib_user.last_name)



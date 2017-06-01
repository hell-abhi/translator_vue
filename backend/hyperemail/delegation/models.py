from django.db import models

# Create your models here.
from django.db import models
import uuid

class User(models.Model):

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=254, unique=True)

    def __unicode__(self):
        return self.email_id

class Helper(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    connected_email = models.CharField(max_length=250)
    connected_folder = models.CharField(max_length=250, null=False)
    def __unicode__(self):
        return unicode(self.user)
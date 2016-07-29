from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from base.models import TimeAuditModel
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)





"""

class Account(TimeAuditModel):

	user = models.OneToOneField(User)
	contact_no = models.CharField(max_length =15 , blank =True)


	def __str__(self):
		return self.user.username


"""
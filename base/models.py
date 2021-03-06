# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import datetime


from django.contrib.auth.models import User
from django.db import models

from datetime import datetime
#default = datetime.datetime.now

class TimeAuditModel(models.Model):

    created_at = models.DateTimeField(default = datetime.now)
    modified_at = models.DateTimeField(default = datetime.now)

    # created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    #modified_at = models.DateTimeField(auto_now=True, verbose_name="Last Modified At")

    class Meta:
        abstract = True


class UserAuditModel(models.Model):
   
    created_by = models.ForeignKey(User, related_name='created_%(class)s_set',
                                   null=True, blank=True, verbose_name="Created By")
    modified_by = models.ForeignKey(User, related_name='updated_%(class)s_set',
                                    null=True, blank=True, verbose_name="Modified By")

    class Meta:
        abstract = True


class AuditModel(TimeAuditModel, UserAuditModel):

    class Meta:
        abstract = True

# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Standard Library
import os
# Third Party Stuff
from celery import Celery
#from django.conf import settings

#

from celery import Task
from celery.task import Task

#from django.core.mail import EmailMultiAlternativess
#





# set the default Django settings module for the 'celery' program.
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

app = Celery('Task')

# Using a string here means the worker will not have to
# pickle the object when using Windows.


#from django.core.mail import send_mail
# reference from -- mahdi yusuf Django Celery Part 1

@app.task
def add(x, y):
    return x + y


#app.config_from_object('settings')
#app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)




"""


class SendEmailTask(Task):


	def run(self,user):

		subject,from_email,to = 'Welcome','vxixnxaxy@gmail.com','pythonistvinay@gmail.com'
		# html_content = render_to_string('email_signup.html',{'user': user.first_name})
		html_content = render_to_string('email_signup.html',{'user': vinay})
		text_content  = strip_tags(html_content)
		msg = EmailMultiAlternatives(subject,text_content,from_email,[to])
		msg.attach_alternative(html_content,'text/html')
		msg.send()


task.register(SendEmailTask)	

"""






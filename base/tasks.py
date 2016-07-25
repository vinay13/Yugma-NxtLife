from celery.registry import Task
from celery.task import Task
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
#from django.core.mail import send_mail
# reference from -- mahdi yusuf Django Celery Part 1



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
In views.py
SendEmailTask.delay(user)
"""









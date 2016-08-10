


from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Channel
from channels import Group
from channels.sessions import channel_session
from channels.auth import  channel_session_user , channel_session_user_from_http
from chat.models import Message

"""
def ws_add(message):
	#print message
	Group("chat").add(message.reply_channel)
"""
# Connected to websocket.receive


@channel_session
def ws_connect(message):
	room = message.content['path'].strip("/")
	message.channel_session['room'] = room
	Group('chat-{}'.format(room)).add(message.reply_channel)


@channel_session_user
def ws_message(message):
	print 'user',message.user.username
	Group("chat-{}".format(message.channel_session['room'])).send({
        "text": "[{}] {}".format(message.user.username,message['text']),
    })


# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message):
	Group("chat-{}".format(message.channel_session['room'])).send({"text": "user has disconnected"})
	Group("chat-{}".format(message.channel_session['room'])).discard(message.reply_channel)






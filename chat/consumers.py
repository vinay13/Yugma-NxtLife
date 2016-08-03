from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from channels.sessions import channel_session
from channels.auth import http_session_user , channel_session_user , channel_session_user_from_http


def http_consumer(message):

	response = HttpResponse('hello vinay %s' % message.content['path'])

	for chunk in AsgiHandler.encode_response(response):
		message.reply_channel.send(chunk)



def msg_consumer(message):
	#save to model
	room = message.content['room']
	ChatMessage.objects.create(

		room = room ,
		message = message.content['message'],
	)

	#broadCast to listening sockets

	Group("chat-%s" % room ).send({
		"text":message.content['message'],

	})


# def ws_message(message):

# 	message.reply_channel.send({
# 		"text":message.content['text'],
# 	}) 



@channel_session
def ws_connect(message):
	room = message.content['path'].strip("/")
	message.channel_session['room'] = room
	Group("chat-%s"% room).add(message.reply_channel)




@channel_session_user_from_http
def ws_add(message):
	Group("chat-%s" % message.user.username[0]).add(message.reply_channel)




@channel_session_user
def ws_message(message):
    Group("chat-%s" % message.channel_session['room']).send({
        "text": message['text'],
    })




@channel_session_user
def ws_disconnect(message):
    Group("chat-%s" % message.channel_session['room']).discard(message.reply_channel)	

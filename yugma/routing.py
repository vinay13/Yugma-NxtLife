
from channels.routing import route
from chat.consumers import ws_add,ws_message,ws_disconnect
#from django.conf.urls import patterns, url , include 


channel_routing = [
				
				#route("http.request","yugma.consumers.http_consumer"),
				route("websocket.connect", ws_add),
				route("websocket.receive",ws_message),
				route("websocket.disconnect", ws_disconnect),
				]


				
"""
http_routing = [
    route("http.request", poll_consumer, path=r"^/poll/$", method=r"^POST$"),
]


chat_routing = [

		route("websocket.connect", chat_connect ,path=r"^/(?P<room>[a-zA-Z0-9_]+)/$"),
		route("websocket.disconnect", chat_disconnect),
		
		# route("http.request","chat.consumers.http_consumer"),
		# route("websocket.connect",ws_connect),
		# route("websocket.receive",ws_message),
		# route("websocket.disconnect",ws_disconnect),

	

		]


routing = [
    # You can use a string import path as the first argument as well.
    include(chat_routing, path=r"^/chat"),
   # include(http_routing),
]
					
"""
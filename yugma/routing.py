from channels.routing import route
from chat.consumers import ws_connect,ws_message,ws_disconnect



"""
http_routing = [
    route("http.request", poll_consumer, path=r"^/poll/$", method=r"^POST$"),
]
"""

channel_routing = [
		
		route("http.request","chat.consumers.http_consumer"),
		route("websocket.connect",ws_connect),
		route("websocket.receive",ws_message),
		route("websocket.disconnect",ws_disconnect),

		]
					
from websocket_server import WebsocketServer
from db import DB
from utils import get_ws_config


# Called for every client connecting (after handshake)
def new_client(client, server):
    print('New client connected and was given id %d' % client['id'])
    msg = database.read()
    server.send_message_to_all(msg)


# Called for every client disconnecting
def client_left(client, server):
    print('Client(%d) disconnected' % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
    server.send_message_to_all(message)
    database.write(message)
    print('Client(%d) said: %s' % (client['id'], message))


ws_config = get_ws_config('config.js')
database = DB('last_number.dat')
server = WebsocketServer(int(ws_config['wsPort']))
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()

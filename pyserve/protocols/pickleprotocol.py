
import pickle

from .plugin import SocketProtocol, malformed_packet_wrap

DefaultArgs = {
    "byteEncodingString":">L",
    "infoBytes":4
}

class Plugin(SocketProtocol):
    send_message = malformed_packet_wrap(pickle.dumps)
    recv_message = malformed_packet_wrap(pickle.loads)

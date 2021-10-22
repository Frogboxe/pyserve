
import msgpack

from .plugin import SocketProtocol, malformed_packet_wrap

DefaultArgs = {
    "byteEncodingString":">L",
    "infoBytes":4
}

class Plugin(SocketProtocol):
    send_message = malformed_packet_wrap(msgpack.dumps)
    recv_message = malformed_packet_wrap(msgpack.loads)

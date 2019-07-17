import asyncio
from client import Client


async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection("127.0.0.1", 8181, loop=loop)
    print("send: %r" % message)
    writer.write(message.encode())
    writer.close()

loop = asyncio.get_event_loop()

message = "get *"
for i in ["put test_key 12.0 1503319740", "put test_key 13.0 1503319739", "put test 13.0 1503319739"]:
    loop.run_until_complete(tcp_echo_client(i, loop))

loop.run_until_complete(tcp_echo_client("got 1234", loop))


loop.close()
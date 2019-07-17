import asyncio


class ClientServerProtocol(asyncio.Protocol):

    @staticmethod
    def find_and_return_value(metric):

        data = []
        with open("log.txt", "r") as f:
            for i in f.readlines():
                message = i.split(" ")
                message.pop()
                data.append([message[1], float(message[2]), int(message[3])])

        if metric == "*":
            res = ""
            for i in data:
                res += "{} {} {}".format(i[0], i[1], i[2]) + "\n"

            return res

        elif metric != "*":
            res = ""
            for i in data:
                if i[0] == metric:
                    res += "{} {} {}".format(i[0], i[1], i[2]) + "\n"
            return res

    @staticmethod
    def formulate_response(command, metric, value, timestamp):

        if command == "get":
            print("ok")
            print(ClientServerProtocol.find_and_return_value(metric))

        if command == "put":
            print("ok\n")
            with open("log.txt", "a") as f:
                f.write("{} {} {} {}".format(command, metric, value, timestamp) + " \n")

        if command != "put" and command != "get":
            print("WRONG COMMAND")

    def data_received(self, data):

        print(data.decode("utf-8"))
        if data.decode()[-1] == "*":
            command, metric = data.decode("utf-8").split(" ")
            value = -999
            timestamp = -999

        elif data.decode()[-1] != "*":

            data = data.decode("utf-8").split(" ")
            if len(data) == 2:
                command, metric = data
                value = -999
                timestamp = -999
            if len(data) == 4:
                command, metric, value, timestamp = data

        ClientServerProtocol.formulate_response(command, metric, value, timestamp)



if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        '127.0.0.1', 8181
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

    #print(run_server("127.0.0.1", 8181))


    def run_server(host, port):

        pass
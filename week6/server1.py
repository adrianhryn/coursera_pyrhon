import asyncio


class ClientServerProtocol(asyncio.Protocol):

    def read_database(self):
        data = []
        with open("log.txt", "r") as f:
            for i in f.readlines():
                message = i.split(" ")
                message.pop()
                data.append([message[1], float(message[2]), int(message[3])])
        return data

    def find_and_return_value(self, metric):

        data = self.read_database()

        # returns all data from database
        if metric == "*":
            res = ""
            for i in data:
                res += "{} {} {}".format(i[0], i[1], i[2]) + "\n"

            return res

        # if metric is not in the database, the func will return "" (due to task conditions)
        # if metric is there, return its values and timestamps
        elif metric != "*":
            res = ""
            for i in data:
                if i[0] == metric:
                    res += "{} {} {}".format(i[0], i[1], i[2]) + "\n"
            return res

    def formulate_response(self, command, metric, value, timestamp):
        """
        Chooses an appropriate server response according to what a client wrote
        """

        # server response for users get command
        if command == "get":
            print("ok")
            print(self.find_and_return_value(metric))

        # server response for users put command: write the value to the database
        if command == "put":
            print("ok\n")
            with open("log.txt", "a") as f:
                f.write("{} {} {} {}".format(command, metric, value, timestamp) + " \n")

        # if server received wrong typed command
        if command != "put" and command != "get":
            print("WRONG COMMAND")

    def data_received(self, data):
        """
        Receives message from some client, calculate which type is this
        :param data: str
        """

        print(data.decode("utf-8"))
        data = data.decode("utf-8").split(" ")

        # if client types "get" command, we don't need the last two arguments in data
        if len(data) == 2:
            data.append("-999")
            data.append("-999")

        command, metric, value, timestamp = data
        to_server = ClientServerProtocol()
        to_server.formulate_response(command, metric, value, timestamp)


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

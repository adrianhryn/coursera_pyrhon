import time
import json
import socket


class Client:

    def __init__(self, host, port, timeout=None):
        self._host = host
        self._port = port
        self._timeout = timeout
        self.base = dict()

    def put(self, metric, value, timestamp=None):
        # puts a new metric to the data base

        try:

            if timestamp is None:
                timestamp = str(int(time.time()))

            # adds non-existing metric in database to it
            if metric not in self.base.keys():
                self.base[metric] = [(timestamp, float(value))]

            elif metric in self.base.keys():
                # if there is no other actions in 'timestamp' time, adds new value to an existing metric
                if timestamp not in [i[0] for i in self.base[metric]]:
                    self.base[metric].append((timestamp, float(value)))
                else:
                    # finds appropriate timestamp and changes the value of it, because if we have a collision of two
                    # timestamps, we should consider the last value from put
                    for ind, val in enumerate(self.base[metric]):

                        if val[0] == timestamp:
                            self.base[metric][ind] = (timestamp, float(value))
                self.base[metric].sort()

        except ClientError:
            return "get_client_error"

    def get(self, metric="-999999"):

        try:
            # if metric is wrong typed
            if metric == "-999999":
                raise ClientError

            # return all records from a database
            if metric is "*":
                return self.base

            # find an appropriate metric in database and return it with according value
            if metric in self.base.keys():
                res = dict()
                res[metric] = self.base[metric]
                return res

            elif metric not in self.base.keys():
                return dict()

        except ClientError:
            return "get_client_error"


class ClientError(Exception):
    """get_client_error"""


if __name__ == "__main__":
    client = Client("127.0.0.1", 8888)

    client.put("test", 0.5, 1)
    client.put("test", 2.0, 2)
    client.put("test", 0.4, 2)
    client.put("load", 301, 3)

    # client.put("eardrum.memory", 4200000)

    # first   return all
    print("return all")
    metrics_fixture = {
        "test": [(1, .5), (2, .4)],
        "load": [(3, 301.0)]
    }

    print(client.get("*") == metrics_fixture)
    print(client.get("*"))
    print(metrics_fixture)

    print("_________________________________________")

    # second   get key
    print("get key")
    metrics_fixture = {
        "test": [(1, .5), (2, .4)],
    }
    print(client.get("test") == metrics_fixture)
    print(client.get("test"))
    print(metrics_fixture)

    print("_________________________________________")

    print(client.get())

    print(client.get("non_existing_key"))
    print(client.get("test"))
    print(client.get)

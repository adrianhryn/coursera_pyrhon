import os
import tempfile
import argparse
import json


def parser(d):
    parser = argparse.ArgumentParser()

    parser.add_argument("--key", help="a key from a storage")
    parser.add_argument("--val", help="values from a storage")

    args = parser.parse_args()

    d = vars(args)
    return json.dumps(d)


def main():


    with open("log.txt", "a") as f:
        #lines = f.readlines()

        print(f.readlines())

        f.write("12")

    #args = parser(d)

    #storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

    #with open("log.txt", "a") as f:
    #    f.write(str(args) + "\n")




main()
#with open(storage_path, 'w') as f:

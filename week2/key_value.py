import os
import tempfile
import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="a key from a storage")
    parser.add_argument("--val", help="values from a storage")
    args = parser.parse_args()

    return vars(args)


def main():

    storage_path = os.path.join(tempfile.gettempdir(), 'storage.txt')
    data = parser()

    with open(storage_path, 'r') as f:
        storage = []
        for i in f.readlines():
            storage.append(i.split())

        if data['val'] is None:

            # find a value from key
            trigger = False
            for i in storage:
                if i[0] == data['key']:
                    trigger = True
                    values = ""
                    for value in i[1:]:
                        values += value + ", "
                    print(values[:-2])
            if not trigger:
                print("not existing key")
        else:
            # find key and append new value to it
            trigger = False
            for i in storage:
                if i[0] == data['key']:
                    trigger = True
                    if data['val'] not in str(i):
                        i.append(data['val'])
            # adding non-existing in storage key and value to storage
            if not trigger:
                storage.append([data['key'], data['val']])

    with open(storage_path, "w") as f:
        f.truncate()

        result = ""
        for i in storage:
            line = ""
            for el in i:
                line += el + " "
            result += line + "\n"

        f.write(result)
main()


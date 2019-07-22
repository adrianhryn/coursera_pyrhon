import os
import tempfile
import argparse


def get_arguments():
    """
    Gets key and value or only key from user input
    :return: dict()
    """
    arguments = argparse.ArgumentParser()
    arguments.add_argument("--key", help="a key from a storage")
    arguments.add_argument("--val", help="values from a storage")
    args = arguments.parse_args()
    vars(args)
    return vars(args)


def get_value(storage, needed_key):
    """
    Returns a value from storage.
    If key is not there, prints "not existing key"
    :param storage: list
    :param needed_key: str
    :return: str (str of needed valus or "not existing key"
    """
    # find a value from key
    trigger = False
    for i in storage:
        if i[0] == needed_key:
            trigger = True
            values = ""
            for j in i[1:]:
                values += j + ", "
            return values[:-2]

    if not trigger:
        return "not existing key"


def set_value(storage, data):
    """
    Sets a value to a storage. If key is not in storage, adds a new key
    :param storage: list
    :param data: dict
    :return: list
    """
    trigger = False
    for i in storage:
        if i[0] == data['key']:
            trigger = True
            if data['val'] not in str(i):
                i.append(data['val'])
    # adding non-existing in storage key and value to storage
    if not trigger:
        storage.append([data['key'], data['val']])

    return storage


def save_to_storage(storage, storage_path):
    """
    Writes a storage in appropriate form, then writes it to the file
    :param storage: list
    :param storage_path: str
    :return: str
    """
    with open(storage_path, "w") as f:
        f.truncate()

        result = ""
        for i in storage:
            line = ""
            for el in i:
                line += el + " "
            result += line + "\n"

        f.write(result)
        return " "


def main():
    
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
     
    # opens an existing file, if it is not exist, create one
    try:
        with open(storage_path, 'r') as f:
            storage = []
            for i in f.readlines():
                storage.append(i.split())
    except FileNotFoundError:
        with open(storage_path, "x"):
            storage = []
    
    # get user input 
    data = get_arguments()

    # data['val'] is None, if user wrote only the key, so user wanted to get a value from the storage
    if data['val'] is None:
        print(get_value(storage, data['key']))
    else:
        storage = set_value(storage, data)
        print(save_to_storage(storage, storage_path))


main()

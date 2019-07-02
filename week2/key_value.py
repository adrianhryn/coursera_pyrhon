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



#with open(storage_path, 'w') as f:

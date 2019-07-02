import functools
import json


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        fin_res = json.dumps(result)
        return fin_res

    return wrapped


@to_json
def get_data():
    return {
        'data': 42,
        'data2': 21,
        'data3': {'data4': [1, 2, 3, 4, 5]}
    }


print(get_data())  # вернёт '{"data": 42}'
print(get_data.__name__)

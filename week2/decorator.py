import functools
import json


def to_json(func):
    """Converts simple dictionary into json format"""
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        fin_res = json.dumps(result)
        return fin_res

    return wrapped


@to_json
def get_data(dict_):
    return dict_


if __name__ == "__main__":

    dict_ = {
        'data': 42,
        'data2': 21,
        'data3': {'data4': [1, 2, 3, 4, 5]}
    }

    assert get_data(dict_) == '{"data": 42, "data2": 21, "data3": {"data4": [1, 2, 3, 4, 5]}}'
    assert get_data({'data': 42}) == '{"data": 42}'
    assert get_data.__name__ == "get_data"

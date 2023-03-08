import json


def dump_data(data: dict) -> json.JSONEncoder:
    if data is dict:
        return json.dump(
            obj=data,
        )
    else:
        print("Data is not a dict type")


def load_data(data: str) -> json.JSONDecoder:
    return json.loads(
        s=data,
    )

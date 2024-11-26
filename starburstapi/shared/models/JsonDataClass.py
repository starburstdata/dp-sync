from typing import cast
import marshmallow_dataclass
from dataclasses import asdict, is_dataclass
from json import JSONEncoder, dumps
from datetime import datetime
from functools import singledispatchmethod


class DateTimeEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)


class JsonDataClass:

    @singledispatchmethod
    @classmethod
    def load(cls, arg):
        raise NotImplemented('JsonDataClass.load() only accepts dicts and json strings')

    @load.register
    @classmethod
    def _(cls, data: str):
        if is_dataclass(cls):
            schema = marshmallow_dataclass.class_schema(cls)()
            return cast(cls, schema.loads(data))
        else:
            raise NotImplemented('Only dataclasses should inherit from JsonDataClass!')

    @load.register
    @classmethod
    def _(cls, data: dict):
        if is_dataclass(cls):
            schema = marshmallow_dataclass.class_schema(cls)()
            return cast(cls, schema.load(data))
        else:
            raise NotImplemented('Only dataclasses should inherit from JsonDataClass!')

    def asdict(self):
        if is_dataclass(self):
            return asdict(self)
        else:
            raise NotImplemented('Only dataclasses should inherit from JsonDataClass!')

    def to_json(self):
        return dumps(self.asdict(), cls=DateTimeEncoder)

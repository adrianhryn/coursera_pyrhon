class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class NullHandler:

    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.event_type == INT:
            if event.if_set_type is None:
                return obj.integer_field
            else:
                obj.integer_field = event.if_set_type
        else:
            print("pass it forward")
            return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event.event_type == FLOAT:
            if event.if_set_type is None:
                return obj.float_field
            else:
                obj.float_field = event.if_set_type
        else:
            print("pass it forward")
            return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.event_type == STR:
            if event.if_set_type is None:
                return obj.string_field
            else:
                obj.string_field = event.if_set_type
        else:
            print("pass it forward")
            return super().handle(obj, event)


INT, FLOAT, STR = "INT", "FLOAT", "STR"


class EventGet:

    def __init__(self, get_event_type):
        self.event_type = {int: INT, float: FLOAT, str: STR}[get_event_type]
        self.if_set_type = None


class EventSet:

    def __init__(self, value):
        self.event_type = {int: INT, float: FLOAT, str: STR}[type(value)]
        self.if_set_type = value


if __name__ == "__main__":

    obj = SomeObject()
    obj.integer_field = 42
    obj.float_field = 3.14
    obj.string_field = "some text"

    chain = IntHandler(FloatHandler(StrHandler(NullHandler)))

    assert chain.handle(obj, EventGet(int)) == 42

    assert chain.handle(obj, EventGet(float)) == 3.14

    assert chain.handle(obj, EventGet(str)) == 'some text'
    chain.handle(obj, EventSet(100))
    assert chain.handle(obj, EventGet(int)) == 100
    chain.handle(obj, EventSet(0.5))
    assert chain.handle(obj, EventGet(float)) == 0.5
    chain.handle(obj, EventSet('new text'))
    assert chain.handle(obj, EventGet(str)) == 'new text'


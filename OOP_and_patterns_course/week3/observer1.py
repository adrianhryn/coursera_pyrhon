from abc import ABC, abstractmethod


class AbstractObserver(ABC):

    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter(AbstractObserver):

    def __init__(self):
        self.achievements = set()

    def update(self, achievement):
        self.achievements.add(achievement)


class FullNotificationPrinter(AbstractObserver):

    def __init__(self):
        self.achievements = list()

    def update(self, achievement):
        self.achievements.append(achievement)


class Engine:
    """Gives titles"""
    pass


class ObservableEngine(Engine):

    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, achievement):
        for subscriber in self.__subscribers:
            subscriber.update(achievement)



if __name__ == "__main__":
    titles = [("1 champion", "first"), ("2 champion", "second"), ("3 champion", "third")]
    achievemnets = ["'title': {}, 'text': {}".format(i[0], i[1]) for i in titles]

    engine = ObservableEngine()
    short = ShortNotificationPrinter()
    full = FullNotificationPrinter()

    engine.subscribe(short)
    engine.subscribe(full)

    for i in achievemnets:
        engine.notify(i)

    engine.unsubscribe(short)

    engine.notify("ASDASDAS")

    print(short.achievements)
    print(full.achievements)
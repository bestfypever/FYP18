class Manager():
    observers = set()

    @classmethod
    def attach(cls, observer):
        cls.observers.add(observer)

    @classmethod
    def notify_observers(cls, data):
        for observer in cls.observers:
            observer.notify(data)

if __name__=='__main__':
    pass

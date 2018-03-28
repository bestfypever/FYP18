import abc

class Observer(object):
    __metaclass__=abc.ABCMeta

    @abc.abstractmethod
    def notify(self, message):
        return


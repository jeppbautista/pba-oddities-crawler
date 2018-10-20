from abc import ABCMeta, abstractmethod

class Scraper(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def init_driver(self):
        raise NotImplementedError('subclasses must override init_driver()!')

    @abstractmethod
    def close_driver(self):
        raise NotImplementedError('subclasses must override close_driver()!')

    @abstractmethod
    def parse(self, element='', *args, **kwargs):
        raise NotImplementedError('subclasses msut override parse()')

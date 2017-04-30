# -*- coding: utf-8 -*-
""" APIの抽象クラス."""

from abc import abstractmethod
from abc import ABCMeta

from six import with_metaclass


class AbstractAPI(with_metaclass(ABCMeta)):

    @abstractmethod
    def make_query(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def parse(self):
        pass

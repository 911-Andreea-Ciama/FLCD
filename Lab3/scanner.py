import re


def is_identifier(elem):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9])*$', elem) is not None


def is_constant(elem):
    return re.match(r'^(0|[+-]?[1-9][0-9]*)$|^\'.*\'$', elem) is not None

class Scanner:
    def __init__(self):
        self.__reserved_words = []
        self.__separators = []
        self.__operators = []

    def get_separators(self):
        return self.__separators

    def get_reserved_words(self):
        return self.__reserved_words

    def get_operators(self):
        return self.__operators

    def get_all(self):
        return self.__operators + self.__separators + self.__reserved_words


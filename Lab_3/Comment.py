from Validator import Validator
from datetime import datetime


class Comment():
    def __init__(self):
        self._validator = Validator()
        self.__text = "What's an awesome article"
        self.__authorNickname = "Roma"
        self.__publishDate = datetime.now()
        self.__isPositive = True


    @property
    def authorNickname(self):
        return self.__authorNickname

    @authorNickname.setter
    def authorNickname(self, name):
        if not (self._validator.validateStringLength(name, 30)):
            raise Exception("Invalid Nickname")

        self.__authorNickname = name

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        if not (self._validator.validateString(text)):
            raise Exception("Text should be string")

        self.__text = text

    def getCommentInfo(self):
        return f"Author: {self.__authorNickname}\nDate: {self.__publishDate}\nText: {self.__text}\nLiked: {self.__isPositive}"

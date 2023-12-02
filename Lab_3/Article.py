from datetime import datetime
from Validator import Validator


class Article:
    def __init__(self):
        self._title = "Введение в теорию множеств"
        self._text = "Концепция бесконечности идеологически далека от обычной математической терминологии — ни одна другая тема не выходит за пределы математики так, что превращается из практического, аналитического инструмента в явление мифического порядка. Понятие бесконечности на короткой ноге с такими культурными темами, как религия и философия, и окутана загадочной аурой божественности."
        self._authorNickname = "Denis"
        self._publishDate = datetime.now()
        self._topic = "Math insights"
        self._validator = Validator()


    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        if not(self._validator.validateStringLength(title, 100)):
            raise Exception("Title is too long")

        self._title = title

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if not(self._validator.validateString(text)):
            raise Exception("Text should be string")

        self._text = text

    @property
    def topic(self):
        return self._topic

    @topic.setter
    def topic(self, text):
        if not (self._validator.validateStringLength(text, 50)):
            raise Exception("Topic is too long")

        self._topic = text

    @property
    def authorNickname(self):
        return self._authorNickname

    @authorNickname.setter
    def authorNickname(self, name):
        if not(self._validator.validateStringLength(name, 30)):
            raise Exception("Invalid Nickname")

        self._authorNickname = name

    @property
    def publishDate(self):
        return self._publishDate

    def getArticleInfo(self) -> str:
        return f"Author: {self._authorNickname}\nTopic: {self._topic}\nTitle: {self._title}\nText: {self._text}\nDate: {self._publishDate}"

    def __eq__(self, other):
        if not(isinstance(other, type(self))):
            return False
        return self._title == other._title and self._text == other._text and self._authorNickname == other._authorNickname and self._topic == other._topic


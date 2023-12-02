from Article import Article


class DescriptionArticle(Article):

    def __init__(self):
        super().__init__()
        self._description = "Когда-то давным давно во всех академических дисциплинах было заложено фундаментальное убеждение — существует единственная бесконечность."

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not(self._validator.validateString(value)):
            raise Exception("Invalid description")

    def getArticleInfo(self) -> str:
        return f"Author: {self._authorNickname}\nTopic: {self._topic}\nTitle: {self._title}\nDescription: {self._description}\nText: {self._text}"

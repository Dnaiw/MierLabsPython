from typing import Iterator

from Article import Article
from Comment import Comment
from datetime import datetime


class CommentedArticle(Article):

    def __init__(self):
        super().__init__()
        self.__comments = []

    def addComment(self, comment: Comment):
        if not(isinstance(comment, Comment)):
            raise Exception("Invalid comment")

        self.__comments.append(comment)

    def addCommentRange(self, comments: list[Comment]):
        for com in comments:
            if not(isinstance(com, Comment)):
                raise ValueError("Invalid comments")

        self.__comments += comments

    def getComments(self) -> Iterator[Comment]:
        for comment in self.__comments:
            yield comment

    def getCommentsInfo(self) -> str:
        result = f"All comments:"
        for comment in self.__comments:
            result += f"\n{comment.getCommentInfo()}\n"

        return result










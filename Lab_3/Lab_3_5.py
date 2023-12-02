from datetime import datetime

from Article import Article
from Comment import Comment
from CommentedArticle import CommentedArticle
from DescriptionArticle import DescriptionArticle
from data import *


article1 = Article()
article2 = DescriptionArticle()
article3 = CommentedArticle()

print("Common article")
print(article1.getArticleInfo())
print()
print("Article with description")
print(article2.getArticleInfo())
print()
print("Article with comments")
print(article3.getArticleInfo())

comment1 = Comment()
print(comment1.getCommentInfo())
comment2 = Comment()
comment2.authorNickname = "Stepan"
comment2.text = commentText1


comment3 = Comment()
comment3.authorNickname = "Dima"
comment3.text = commentText2

comment4 = Comment()
comment4.authorNickname = "Kir"
comment4.text = commentText3

article3.addCommentRange([comment1, comment2, comment3, comment4])

print("------------------------------------------------")
print("Comments by iterator:")
comments = article3.getComments()
for comment in comments:
    print(comment.getCommentInfo())
    print()

print("------------------------------------------------")
print("Comments by 'GetCommentsInfo':")
print(article3.getCommentsInfo())

articleA = Article()
articleB = Article()

print(articleA == articleB)

article = Article()
article.title = input("\nEnter article title\n")
article.topic = input("Enter article topic\n")
article.authorNickname = input("Enter article author\n")
article.text = input("Enter article text\n")

print("Created article:")
print(article.getArticleInfo())

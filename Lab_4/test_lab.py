import pytest

from Article import Article
from Comment import Comment
from CommentedArticle import CommentedArticle
from DescriptionArticle import DescriptionArticle
from LengthError import LengthError


@pytest.fixture(scope="function")
def common_article():
    article = Article()
    yield article
    del article


@pytest.fixture(scope="module")
def description_article():
    article = DescriptionArticle()
    yield article
    del article


@pytest.fixture(scope="function")
def commented_article():
    article = CommentedArticle()
    yield article
    del article

@pytest.fixture(scope="module")
def comment():
    comment = Comment()
    yield comment
    del comment

@pytest.fixture(scope="function")
def comment_list():
    comment1 = Comment()
    comment2 = Comment()
    comment3 = Comment()
    comment4 = Comment()
    yield [comment1, comment2, comment3, comment4]
    del comment1
    del comment2
    del comment3
    del comment4


class TestClass:
    def test_common_article(self, common_article):
        title = "assdaadads"
        topic = "asdaasda"
        author = "dsdad"
        text = "asdada"
        common_article.title = title
        common_article.topic = topic
        common_article.text = text
        common_article.authorNickname = author
        assert common_article.title == title and common_article.authorNickname == author and common_article.text == text and common_article.topic == topic

    def test_description_article(self, description_article):
        title = "assdaadads"
        topic = "asdaasda"
        author = "dsdad"
        text = "asdada"
        description = "asdadasd"
        description_article.title = title
        description_article.topic = topic
        description_article.text = text
        description_article.authorNickname = author
        description_article.description = description
        assert description_article.title == title and description_article.authorNickname == author and description_article.text == text and description_article.topic == topic and description_article.description == description

    def test_comment_article(self, commented_article, comment):
        title = "assdaadads"
        topic = "asdaasda"
        author = "dsdad"
        text = "asdada"
        comment_text = "ASSDA"
        comment_author = "asdads"
        comment_rate = True
        comment.text = comment_text
        comment.authorNickname = comment_author
        comment.isPositive = comment_rate
        commented_article.addComment(comment)
        commented_article.title = title
        commented_article.topic = topic
        commented_article.text = text
        commented_article.authorNickname = author
        assert commented_article.title == title and commented_article.authorNickname == author and commented_article.text == text and commented_article.topic == topic and list(commented_article.getComments())[0].text == comment_text

    def test_title_exceptions(self):
        with pytest.raises(LengthError):
            article = Article()
            article.title = "asd"*100

    def test_description_exceptions(self):
        with pytest.raises(ValueError):
            article = DescriptionArticle()
            article.description = 1223

    def test_add_comments_range(self, comment_list, commented_article, common_article):
        with pytest.raises(ValueError):
            comment_list.append(common_article)
            commented_article.addCommentRange(comment_list)

    def test_comments_iterator(self, comment_list, commented_article):
        commented_article.addCommentRange(comment_list)
        assert list(commented_article.getComments()) == comment_list

    def test_eq(self, common_article):
        clone = Article()
        clone.text = common_article.text
        clone.topic = "sfdfsf"
        clone.title = common_article.title
        clone.authorNickname = common_article.authorNickname
        assert common_article == clone



import pickle
from datetime import datetime

from Article import Article
from Comment import Comment
from CommentedArticle import CommentedArticle
from DescriptionArticle import DescriptionArticle
from LengthError import LengthError
from data import *

#
# article1 = Article()
# article2 = DescriptionArticle()
# article3 = CommentedArticle()
#
# print("Common article")
# print(article1.getArticleInfo())
# print()
# print("Article with description")
# print(article2.getArticleInfo())
# print()
# print("Article with comments")
# print(article3.getArticleInfo())
#
# comment1 = Comment()
# print(comment1.getCommentInfo())
# comment2 = Comment()
# comment2.authorNickname = "Stepan"
# comment2.text = commentText1
#
#
# comment3 = Comment()
# comment3.authorNickname = "Dima"
# comment3.text = commentText2
#
# comment4 = Comment()
# comment4.authorNickname = "Kir"
# comment4.text = commentText3
#
# article3.addCommentRange([comment1, comment2, comment3, comment4])
#
# print("------------------------------------------------")
# print("Comments by iterator:")
# comments = article3.getComments()
# for comment in comments:
#     print(comment.getCommentInfo())
#     print()
#
# print("------------------------------------------------")
# print("Comments by 'GetCommentsInfo':")
# print(article3.getCommentsInfo())
#
allArticles = {
    "common": [],
    "description": [],
    "commented": []
}

while True:
    print("1 - Show all data\n2 - Create common article\n3 - Create description article\n4 - Create commented article\n5 - load data from file\n6 - save data to file\n7 - leave program")
    try:
        mode = int(input("Выберите команду\n"))
    except ValueError:
        "Введите цифру"
        continue

    if mode == 1:
        print("\nCommon")
        for article in allArticles["common"]:
            print(article.getArticleInfo())
        print("\nDescription")
        for article in allArticles["description"]:
            print(article.getArticleInfo())
        print("\nCommented")
        for article in allArticles["commented"]:
            print(article.getArticleInfo())
            print(f"Comments\n {article.getCommentsInfo()}")
        continue

    if mode == 2:
        newArticle = Article()
        while True:
            try:
                newArticle.title = input("Введите название\n")
            except ValueError:
                print("Некорректное название")
                continue
            except Exception:
                print("Неизвестная ошибка")
                continue

            try:
                newArticle.text = input("Введите текст\n")
            except ValueError:
                print("Некорретный текст")
                continue
            except Exception:
                print("Неизвестная ошибка")
                continue

            try:
                newArticle.authorNickname = input("Введите имя автора\n")
            except LengthError:
                print("Слишком длинное имя автора")
                continue
            except ValueError:
                print("Некорректное имя автора")
                continue
            except:
                print("Неизвестная ошибка")
                continue

            try:
                newArticle.topic = input("Введите тему")
            except LengthError:
                print("Слишком длинная тема")
                continue
            except ValueError:
                print("Некорректная тема")
                continue
            except:
                print("Неизвестная ошибка")
                continue

            allArticles["common"].append(newArticle)
            break
        continue

    if mode == 3:
        newArticle = DescriptionArticle()
        while True:
            try:
                newArticle.title = input("Введите название\n")
            except ValueError:
                print("Некорректное название")
                continue
            except Exception:
                print("Неизвестная ошибка")
                continue

            try:
                newArticle.text = input("Введите текст\n")
            except ValueError:
                print("Некорретный текст")
                continue
            except Exception:
                print("Неизвестная ошибка")
                continue

            try:
                newArticle.authorNickname = input("Введите имя автора\n")
            except LengthError:
                print("Слишком длинное имя автора")
                continue
            except ValueError:
                print("Некорректное имя автора")
                continue
            except Exception:
                print("Неизвестная ошибка")
                continue

            try:
                newArticle.topic = input("Введите тему")
            except LengthError:
                print("Слишком длинная тема")
                continue
            except ValueError:
                print("Некорректная тема")
                continue
            except:
                print("Неизвестная ошибка")
                continue

            try:
                newArticle.topic = input("Введите описание")
            except ValueError:
                print("Некорректное описание")
                continue
            except:
                print("Неизвестная ошибка")
                continue

            allArticles["description"].append(newArticle)
            break
        continue

    if mode == 4:
        newArticle = CommentedArticle()
        while True:
            try:
                newArticle.title = input("Введите название\n")
            except ValueError:
                print("Некорректное название")
                continue
            except Exception:
                print("Неизвестная ошибка")
                continue

            try:
                newArticle.text = input("Введите текст\n")
            except ValueError:
                print("Некорретный текст")
                continue
            except Exception:
                print("Неизвестная ошибка")
                continue

            try:
                newArticle.authorNickname = input("Введите имя автора\n")
            except LengthError:
                print("Слишком длинное имя автора")
                continue
            except ValueError:
                print("Некорректное имя автора")
                continue
            except Exception:
                print("Неизвестная ошибка")
                continue

            try:
                newArticle.topic = input("Введите тему")
            except LengthError:
                print("Слишком длинная тема")
                continue
            except ValueError:
                print("Некорректная тема")
                continue
            except:
                print("Неизвестная ошибка")
                continue

            while True:
                try:
                   mode2 = int(input("1 - Добавить комментарий\n2 - Сохранить\n"))
                except ValueError:
                    print("Некоректная комнда")
                    continue
                except:
                    print("Неизвестная ошибка")
                    continue

                if mode2 == 1:
                    newComment = Comment()
                    while True:
                        try:
                            newComment.text = input("Введите текст\n")
                        except ValueError:
                            print("Некорректный текст")
                            continue
                        except Exception:
                            print("Неизвестная ошибка")
                            continue

                        try:
                            newComment.authorNickname = input("Введите имя автора\n")
                        except ValueError:
                            print("Некорректное имя автора")
                            continue
                        except Exception:
                            print("Неизвестная ошибка")
                            continue


                        status = input("Коммент положительный? Введите да/нет\n")
                        if status.lower() == "да":
                            newComment.isPositive = True
                            break
                        if status.lower() == "нет":
                            newComment.isPositive = False
                            break
                        else:
                            print("Введите да или нет")
                            continue

                    newArticle.addComment(newComment)


                if mode2 == 2:
                    break

            allArticles["commented"].append(newArticle)
            break
        continue

    if mode == 5:
        try:
            filename = input("Введите имя файла с данными\n")
            with open(filename, "rb") as file:
                allArticles = pickle.load(file)
            continue
        except FileNotFoundError:
            print("Файл с таким именем не найден")
            continue
        except:
            print("Неизвестная ошибка при чтении из файла")
            continue


    if mode == 6:
        try:
            filename = input("Введите имя файла для сохранения\n")
            with open(filename, "wb") as file:
                pickle.dump(allArticles, file)
                continue
        except:
            print("Неизвестная ошибка при чтении из файла")
            continue

    if mode == 7:
        break

    else:
        print("Неизвестная команда")
        continue



















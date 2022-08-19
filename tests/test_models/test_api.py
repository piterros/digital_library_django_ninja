import django

django.setup()

from pydantic_factories import ModelFactory

from digital_library.schemas import BooksSchemaIn, GamesSchemaIn, VideosSchemaIn

from django.test import TestCase
from digital_library.models import Books, Games, Videos


class BooksFactory(ModelFactory):
    __model__ = BooksSchemaIn


class GamesFactory(ModelFactory):
    __model__ = GamesSchemaIn


class VideosFactory(ModelFactory):
    __model__ = VideosSchemaIn


class BookTests(TestCase):
    def fake_books(self):
        fake_books = [BooksFactory.build() for x in range(10)]
        return fake_books

    def test_author(self):
        for fake_book in self.fake_books():
            book = Books.objects.create(
                title=fake_book.dict()["title"],
                type=fake_book.dict()["type"],
                author=fake_book.dict()["author"],
                purchase_date=fake_book.dict()["purchase_date"],
                finish_date=fake_book.dict()["finish_date"],
        )
            self.assertEqual(fake_book.dict()["author"], book.author)

    def test_title(self):
        for fake_book in self.fake_books():
            book = Books.objects.create(
                title=fake_book.dict()["title"],
                type=fake_book.dict()["type"],
                author=fake_book.dict()["author"],
                purchase_date=fake_book.dict()["purchase_date"],
                finish_date=fake_book.dict()["finish_date"],
        )
            self.assertEqual(fake_book.dict()["title"], book.title)

    def test_type(self):
        for fake_book in self.fake_books():
            book = Books.objects.create(
                title=fake_book.dict()["title"],
                type=fake_book.dict()["type"],
                author=fake_book.dict()["author"],
                purchase_date=fake_book.dict()["purchase_date"],
                finish_date=fake_book.dict()["finish_date"],
            )
            self.assertEqual(fake_book.dict()["type"], book.type)

    def test_purchase_date(self):
        for fake_book in self.fake_books():
            book = Books.objects.create(
                title=fake_book.dict()["title"],
                type=fake_book.dict()["type"],
                author=fake_book.dict()["author"],
                purchase_date=fake_book.dict()["purchase_date"],
                finish_date=fake_book.dict()["finish_date"],
            )
            self.assertEqual(fake_book.dict()["purchase_date"], book.purchase_date)

    def test_finish_date(self):
        for fake_book in self.fake_books():
            book = Books.objects.create(
                title=fake_book.dict()["title"],
                type=fake_book.dict()["type"],
                author=fake_book.dict()["author"],
                purchase_date=fake_book.dict()["purchase_date"],
                finish_date=fake_book.dict()["finish_date"],
            )
            self.assertEqual(fake_book.dict()["finish_date"], book.finish_date)

    def test_books_api(self):
        response = self.client.get("/api/books")
        self.assertEqual(response.status_code, 200)


# class GameTests(TestCase):
#     def fake_games(self):
#         fake_games = [GamesFactory.build() for x in range(10)]
#         for x in fake_games:
#             print(x.dict())
#         return fake_games
#
#     def test_title(self):
#         for fake_game in self.fake_games():
#             game = Games.objects.create(
#                 title=fake_game.dict()["title"],
#                 platform=fake_game.dict()["platform"],
#                 purchase_date=fake_game.dict()["purchase_date"],
#                 finish_date=fake_game.dict()["finish_date"],
#             )
#             self.assertEqual(fake_game.dict()["title"], game.title)
#
#     def test_platform(self):
#         for fake_game in self.fake_games():
#             game = Games.objects.create(
#                 title=fake_game.dict()["title"],
#                 platform=fake_game.dict()["platform"],
#                 purchase_date=fake_game.dict()["purchase_date"],
#                 finish_date=fake_game.dict()["finish_date"],
#             )
#             self.assertEqual(fake_game.dict()["platform"], game.platform)
#
#     def test_purchase_date(self):
#         for fake_game in self.fake_games():
#             game = Games.objects.create(
#                 title=fake_game.dict()["title"],
#                 platform=fake_game.dict()["platform"],
#                 purchase_date=fake_game.dict()["purchase_date"],
#                 finish_date=fake_game.dict()["finish_date"],
#             )
#             self.assertEqual(fake_game.dict()["purchase_date"], game.purchase_date)
#
#     def test_finish_date(self):
#         for fake_game in self.fake_games():
#             game = Games.objects.create(
#                 title=fake_game.dict()["title"],
#                 platform=fake_game.dict()["platform"],
#                 purchase_date=fake_game.dict()["purchase_date"],
#                 finish_date=fake_game.dict()["finish_date"],
#             )
#             self.assertEqual(fake_game.dict()["finish_date"], game.finish_date)
#
#     def test_games_api(self):
#         response = self.client.get("/api/games")
#         self.assertEqual(response.status_code, 200)


class VideoTests(TestCase):
    def fake_videos(self):
        fake_videos = [VideosFactory.build() for x in range(10)]
        for x in fake_videos:
            print(x.dict())
        return fake_videos

    def test_finish_date(self):
        for fake_video in self.fake_videos():
            video = Videos.objects.create(
                title=fake_video.dict()["title"],
                type=fake_video.dict()["type"],
                finish_date=fake_video.dict()["finish_date"],
            )
            self.assertEqual(fake_video.dict()["finish_date"], video.finish_date)
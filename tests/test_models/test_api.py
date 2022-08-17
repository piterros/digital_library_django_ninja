import django

django.setup()

from pydantic_factories import ModelFactory

from digital_library.schemas import BooksSchemaIn

from django.test import TestCase
from digital_library.models import Books


class BooksFactory(ModelFactory):
    __model__ = BooksSchemaIn


def results():
    result = [BooksFactory.build() for x in range(10)]
    return result


class BookTests(TestCase):
    def test_model_content(self):
        for x in results():
            book = Books.objects.create(
                title=x.dict()["title"],
                type=x.dict()["type"],
                author=x.dict()["author"],
                purchase_date=x.dict()["purchase_date"],
                finish_date=x.dict()["finish_date"],
            )
            self.assertEqual(book.title, x.dict()["title"])
            self.assertEqual(book.author, x.dict()["author"])
            self.assertEqual(book.purchase_date, x.dict()["purchase_date"])

    def test_books_api(self):
        response = self.client.get("/api/books")
        self.assertEqual(response.status_code, 200)

# import factory.fuzzy
# import datetime
#
# from digital_library.models import Books
# from faker import Faker
# from faker_enum import EnumProvider
#
# fake = Faker()
# fake.add_provider(EnumProvider)
#
# factory.Faker._DEFAULT_LOCALE = 'pl_PL'
#
#
# class PostFactory(factory.Factory):
#     class Meta:
#         model = Books
#
#     title = factory.Faker("name")
#     author = factory.Faker("name")
#     purchase_date = factory.fuzzy.FuzzyDate(datetime.date(2008, 1, 1))
#     finish_date = factory.fuzzy.FuzzyDate(datetime.date(2009, 12, 30))
#     type = factory.Faker("word")

from pydantic_factories import ModelFactory

from digital_library.schemas import BooksSchemaIn


class BooksFactory(ModelFactory):
    __model__ = BooksSchemaIn


result = BooksFactory.build()

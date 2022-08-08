from ninja import Schema, Field
from datetime import date
from pydantic import validator
from enum import Enum


class BookTypes(Enum):
    book = "book"
    ebook = "ebook"
    audiobook = "audiobook"


class VideoTypes(Enum):
    series = "series"
    movie = "movie"


class DigitalLibrarySchemaIn(Schema):
    title: str
    finish_date: date


class DigitalLibrarySchemaOut(Schema):
    title: str
    finish_date: date

    @validator("title")
    def title_as_title(cls, title):
        return title.title()


class GamesSchemaIn(DigitalLibrarySchemaIn):
    platform = str
    purchase_date: date


class GamesSchemaOut(DigitalLibrarySchemaOut):
    platform = str
    purchase_date: date

    @validator("platform", check_fields=False)
    def platform_uppercase_or_as_title(cls, platform):
        if len(platform) > 3:
            return platform.title()
        return platform.upper()


class BooksSchemaIn(DigitalLibrarySchemaIn):
    author: str
    type: BookTypes
    purchase_date: date


class BooksSchemaOut(DigitalLibrarySchemaOut):
    author: str
    type: str
    purchase_date: date

    @validator("author", check_fields=False)
    def author_as_title(cls, author):
        return author.title()


class VideosSchemaIn(DigitalLibrarySchemaIn):
    type: VideoTypes


class VideosSchemaOut(DigitalLibrarySchemaOut):
    type: str
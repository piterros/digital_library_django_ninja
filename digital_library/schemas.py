from ninja import Schema
from datetime import date
from pydantic import validator
from enum import Enum
from ninja.errors import HttpError


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

    @validator("title")
    def title_as_title(cls, title):
        return title.title()


class DigitalLibrarySchemaOut(Schema):
    title: str
    finish_date: date


class GamesSchemaIn(DigitalLibrarySchemaIn):
    platform = str
    purchase_date: date

    @validator("platform", check_fields=False)
    def platform_uppercase_or_as_title(cls, platform):
        if len(platform) > 3:
            return platform.title()
        return platform.upper()


class GamesSchemaOut(DigitalLibrarySchemaOut):
    platform = str
    purchase_date: date


class BooksSchemaIn(DigitalLibrarySchemaIn):
    author: str
    type: BookTypes
    purchase_date: date

    class Config:
        use_enum_values = True

    @validator("author", check_fields=False)
    def author_as_title(cls, author):
        return author.title()

    @validator("type", pre=True)
    def validate_type(cls, book_type):
        if book_type not in ("book", "ebook", "audiobook"):
            raise HttpError(422, "Incorrect book type")
        return book_type


class BooksSchemaOut(DigitalLibrarySchemaOut):
    id: int
    author: str
    type: str
    purchase_date: date


class VideosSchemaIn(DigitalLibrarySchemaIn):
    type: VideoTypes

    class Config:
        use_enum_values = True

    @validator("type", pre=True)
    def validate_type(cls, video_type):
        if video_type not in ("series", "movie"):
            raise HttpError(422, "Incorrect video type")
        return video_type


class VideosSchemaOut(DigitalLibrarySchemaOut):
    type: str

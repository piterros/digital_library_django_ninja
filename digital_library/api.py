from ninja import NinjaAPI
from .schemas import BooksSchemaIn, BooksSchemaOut, GamesSchemaIn, GamesSchemaOut, VideosSchemaIn, VideosSchemaOut
from .models import Books, Games, Videos
from typing import List
from django.shortcuts import get_object_or_404, get_list_or_404
from django.core.exceptions import FieldError
from ninja.errors import HttpError

api = NinjaAPI()


@api.get("/books", response=List[BooksSchemaOut])
def list_books(request):
    books = Books.objects.all()
    return books


@api.get("/books/{book_id}", response=BooksSchemaOut)
def get_book(request, book_id: int):
    book = get_object_or_404(Books, id=book_id)
    return book


@api.post("/books", response={201: BooksSchemaOut})
def create_book(request, item: BooksSchemaIn):
    book = Books.objects.create(**item.dict())
    return get_object_or_404(Books, id=book.id)


@api.put("/books/{book_id}")
def update_book(request, book_id: int, payload: BooksSchemaIn):
    book = get_object_or_404(Books, id=book_id)
    for attr, value in payload.dict().items():
        setattr(book, attr, value)
    book.save()
    return book


@api.delete("/books/{book_id}")
def delete_book(request, book_id: int):
    book = get_object_or_404(Books, id=book_id)
    book.delete()
    return {"Book deleted": True}


@api.get("/games", response=List[GamesSchemaOut])
def list_games(request):
    games = Games.objects.all()
    return games


@api.get("/games/{game_id}", response=GamesSchemaOut)
def get_game(request, game_id: int):
    game = get_object_or_404(Games, id=game_id)
    return game


@api.post("/games", response={201: GamesSchemaOut})
def create_game(request, item: GamesSchemaIn):
    game = Games.objects.create(**item.dict())
    return get_object_or_404(Games, id=game.id)


@api.put("/games/{game_id}")
def update_game(request, game_id: int, payload: GamesSchemaIn):
    game = get_object_or_404(Games, id=game_id)
    for attr, value in payload.dict().items():
        setattr(game, attr, value)
    game.save()
    return game


@api.delete("/games/{game_id}")
def delete_game(request, game_id: int):
    game = get_object_or_404(Games, id=game_id)
    game.delete()
    return {"Game deleted": True}


@api.get("/videos", response=List[VideosSchemaOut])
def list_videos(request):
    videos = Videos.objects.all()
    return videos


@api.get("/videos/{video_id}", response=VideosSchemaOut)
def get_video(request, video_id: int):
    video = get_object_or_404(Videos, id=video_id)
    return video


@api.post("/videos", response={201: VideosSchemaOut})
def create_video(request, item: VideosSchemaIn):
    video = Videos.objects.create(**item.dict())
    return get_object_or_404(Videos, id=video.id)


@api.put("/videos/{video_id}")
def update_video(request, video_id: int, payload: VideosSchemaIn):
    video = get_object_or_404(Videos, id=video_id)
    for attr, value in payload.dict().items():
        setattr(video, attr, value)
    video.save()
    return video.id


@api.delete("/videos/{video_id}")
def delete_video(request, video_id: int):
    video = get_object_or_404(Videos, id=video_id)
    video.delete()
    return {"Video deleted": True}


@api.get("/search")
def search(request, title: str):
    # print("################# ", model)
    # print("############## model.filter(**{search_key: search_value})", Books.objects.filter(**{search_key: search_value}))
    # if search_key and search_value:
        try:
            # queryset = Books.objects.filter(**{search_key: search_value})
            # queryset = Books.objects.filter(title="book 2")
            queryset = get_list_or_404(Books, title=title)
        except FieldError:
            return HttpError(
                422, message="incorrect key"
            )
        if queryset:
            return queryset
        return {"search_result": "no data"}

    # return {"search_result": "key and/or value not specified"},

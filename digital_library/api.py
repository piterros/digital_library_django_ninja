from ninja import NinjaAPI
from .schemas import BooksSchemaIn, BooksSchemaOut
from .models import Books
from typing import List
from django.shortcuts import get_object_or_404

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
    return book.id


@api.delete("/books/{book_id}")
def delete_employee(request, book_id: int):
    book = get_object_or_404(Books, id=book_id)
    book.delete()
    return {"Book deleted": True}

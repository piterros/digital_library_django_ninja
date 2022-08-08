from ninja import NinjaAPI
from .schemas import BooksSchemaIn, BooksSchemaOut
from .models import Books
from typing import List

api = NinjaAPI()


# @api.get("/hello")
# def hello(request):
#     return "Hello world"


@api.get("/books", response=List[BooksSchemaOut])
def get(request):
    books = Books.objects.all()
    return books

@api.post("/books")
def create(request, item: BooksSchemaIn):
    book = Books.objects.create(**item.dict())
    return book.id

# @api.post("/path")
# def post_operation(request):
#     ...
#
# @api.put("/path")
# def put_operation(request):
#     ...
#
# @api.delete("/path")
# def delete_operation(request):
#     ...
#
# @api.patch("/path")
# def patch_operation(request):
#     ...

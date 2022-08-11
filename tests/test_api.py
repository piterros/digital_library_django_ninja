import pytest
from django.test import Client


class TestBooksView:
    @pytest.mark.django_db
    def test_books_views_if_request_is_correct(self):
        client = Client()
        response = client.get(path='/api/books')
        assert response.status_code == 200

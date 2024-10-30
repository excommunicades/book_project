import pytest
import json
from rest_framework import status
from rest_framework.test import APIClient

from django.urls import reverse

from books.models import Books

@pytest.fixture
def book_data():
    return {
        "title": "Test book",
        "description": "simply test book"
    }


@pytest.fixture
def book_not_found():
    return {
        "error": "Book not found."
        }


@pytest.mark.django_db
def test_book_list(client, book_data):

    url = '/api/books/'

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data == []


    response_create_post = client.post(
                        url,
                        data=json.dumps(book_data),
                        content_type='application/json',
                        )

    assert response_create_post.status_code == status.HTTP_201_CREATED
    assert response_create_post.data == book_data

    response_after_creation = client.get(url)

    assert response_after_creation.status_code == status.HTTP_200_OK
    assert len(response_after_creation.data) == 1
    assert response_after_creation.data[0]['title'] == book_data['title']


@pytest.mark.django_db
def test_book_retrieve(client, book_data, book_not_found):

    url = '/api/books/1/'
    response = client.get(url)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data == book_not_found

    create_url = '/api/books/'

    response_create_post = client.post(
                        create_url,
                        data=json.dumps(book_data),
                        content_type='application/json',
                        )

    assert response_create_post.status_code == status.HTTP_201_CREATED
    assert response_create_post.data == book_data


@pytest.mark.django_db
def test_create_book(client, book_data):

    url = '/api/books/'

    response = client.post(
                        url,
                        data=json.dumps(book_data),
                        content_type='application/json',
                        )

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_update_book(client, book_data, book_not_found):

    book_pk = 1

    url = f'/api/books/{book_pk}/'

    response = client.put(
                        url,
                        data=json.dumps(book_data),
                        content_type='application/json',
                        )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data == book_not_found

    create_url = '/api/books/'

    response_create_post = client.post(
                        create_url,
                        data=json.dumps(book_data),
                        content_type='application/json',
                        )

    assert response_create_post.status_code == status.HTTP_201_CREATED
    assert response_create_post.data == book_data

    book_list = client.get('/api/books/')
    book_pk = book_list.data[0].get('pk')
    url = f'/api/books/{book_pk}/'

    book_update_data = {

        "title": "Test booky",
        "description": "simply test booky updated"
    }

    response = client.put(
                        url,
                        data=json.dumps(book_update_data),
                        content_type='application/json',
                        )

    assert response.status_code == status.HTTP_200_OK
    assert response.data == book_update_data


@pytest.mark.django_db
def test_delete_book(client, book_data, book_not_found):

    book_pk = 1

    url = f'/api/books/{book_pk}/'

    response = client.delete(url)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data == book_not_found

    create_url = '/api/books/'

    response_create_post = client.post(
                        create_url,
                        data=json.dumps(book_data),
                        content_type='application/json',
                        )

    assert response_create_post.status_code == status.HTTP_201_CREATED
    assert response_create_post.data == book_data

    book_list = client.get('/api/books/')
    book_pk = book_list.data[0].get('pk')

    url = f'/api/books/{book_pk}/'

    response_delete = client.delete(url)

    assert response_delete.status_code == status.HTTP_204_NO_CONTENT
    assert response_delete.data == {"message": "Book was deleted successfully."}

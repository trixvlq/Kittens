import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from cats.models import Cat, Breed, Rate

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(db):
    return User.objects.create_user(username='testuser', password='testpass')

@pytest.fixture
def create_breed(db):
    return Breed.objects.create(name='Siamese')

@pytest.fixture
def create_cat(db, create_user, create_breed):
    return Cat.objects.create(
        user=create_user,
        name="Fluffy",
        color="black",
        age=12,
        description="A cute black kitten",
        breed=create_breed
    )

@pytest.mark.django_db
def test_user_registration(api_client):
    response = api_client.post('/auth/users/', {
        'username': 'newuser',
        'password': 'newpass123'
    })
    assert response.status_code == 201
    assert User.objects.filter(username='newuser').exists()

@pytest.mark.django_db
def test_user_login(api_client, create_user):
    response = api_client.post('/auth/jwt/create/', {
        'username': 'testuser',
        'password': 'testpass'
    })
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data

@pytest.mark.django_db
def test_get_cat_list(api_client, create_cat):
    response = api_client.get('/cats/')
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == 'Fluffy'

@pytest.mark.django_db
def test_create_cat(api_client, create_user, create_breed):
    api_client.login(username='testuser', password='testpass')
    response = api_client.post('/cats/create/', {
        'name': 'Snowball',
        'color': 'white',
        'age': 6,
        'description': 'A playful kitten',
        'breed': create_breed.id
    })
    assert response.status_code == 201
    assert Cat.objects.filter(name='Snowball').exists()

@pytest.mark.django_db
def test_update_cat(api_client, create_user, create_cat):
    api_client.login(username='testuser', password='testpass')
    response = api_client.patch(f'/cats/{create_cat.id}/', {
        'description': 'An updated description'
    })
    assert response.status_code == 200
    assert Cat.objects.get(id=create_cat.id).description == 'An updated description'

@pytest.mark.django_db
def test_delete_cat(api_client, create_user, create_cat):
    api_client.login(username='testuser', password='testpass')
    response = api_client.delete(f'/cats/{create_cat.id}/')
    assert response.status_code == 204
    assert not Cat.objects.filter(id=create_cat.id).exists()

@pytest.mark.django_db
def test_rate_cat(api_client, create_user, create_cat):
    user2 = User.objects.create_user(username='user2', password='pass2')
    api_client.login(username='user2', password='pass2')
    response = api_client.post(f'/cats/rate/{create_cat.id}/', {
        'rate': 5,
        'comment': 'Amazing cat!'
    })
    assert response.status_code == 201
    assert Rate.objects.filter(cat=create_cat, user=user2).exists()


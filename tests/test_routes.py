import pytest
from app import create_app
from app import models

@pytest.fixture
def client():
    """Creates a test version of the Flask app."""
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page_loads(client):
    """Homepage should return HTTP 200 OK."""
    response = client.get('/')
    assert response.status_code == 200

def test_home_page_contains_shark_content(client):
    """Homepage must contain whale shark content."""
    response = client.get('/')
    data = response.data.decode('utf-8')
    assert 'Whale Shark' in data or 'sighting' in data.lower()

def test_add_page_loads(client):
    """Add-sighting page should return HTTP 200 OK."""
    response = client.get('/add')
    assert response.status_code == 200

def test_health_endpoint_returns_ok(client):
    """Health check endpoint must return status 'ok'."""
    response = client.get('/health')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'ok'

def test_submit_sighting_redirects(client):
    """POSTing a valid sighting should redirect (302) back to homepage."""
    response = client.post('/add', data={
        'location': 'Gulf of Mexico',
        'date': '2024-07-04',
        'size_meters': '8.0',
        'observer': 'Test Researcher',
        'notes': 'Feeding near surface',
    })
    assert response.status_code == 302  # redirect after POST

def test_submitted_sighting_appears_on_homepage(client):
    """After submitting a sighting, it should appear in the sightings list."""
    client.post('/add', data={
        'location': 'Red Sea Test Location',
        'date': '2024-08-01',
        'size_meters': '6.5',
        'observer': 'Automated Test',
        'notes': '',
    })
    response = client.get('/')
    assert b'Red Sea Test Location' in response.data

def test_stats_has_correct_keys():
    """Stats dict must always contain count, avg_size, and max_size."""
    stats = models.get_stats()
    assert 'count' in stats
    assert 'avg_size' in stats
    assert 'max_size' in stats

def test_preloaded_sightings_exist():
    """Should have pre-loaded sightings, not an empty database."""
    stats = models.get_stats()
    assert stats['count'] > 0

def test_adding_sighting_increments_count():
    """Adding a sighting via the model should increase count by 1."""
    before = models.get_stats()['count']
    models.add_sighting(
        location='Test Ocean',
        date='2024-01-01',
        size_meters=7.5,
        observer='Unit Test',
    )
    after = models.get_stats()['count']
    assert after == before + 1
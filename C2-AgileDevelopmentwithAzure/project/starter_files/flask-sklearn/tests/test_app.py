import pytest
from app import app

@pytest.fixture
def client():
    """Fixture to create a test client for the Flask app."""
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Sklearn Prediction Home" in response.data

def test_predict_valid(client, mocker):
    """Test the predict route with valid input."""
    
    # Mock the joblib.load to return a fake model for testing
    mock_model = mocker.Mock()
    mock_model.predict.return_value = [24.0]  # Mock prediction value

    mocker.patch('joblib.load', return_value=mock_model)

    response = client.post('/predict', json={
        "CHAS": {"0": 0},
        "RM": {"0": 6.575},
        "TAX": {"0": 296.0},
        "PTRATIO": {"0": 15.3},
        "B": {"0": 396.9},
        "LSTAT": {"0": 4.98}
    })

    assert response.status_code == 200
    json_data = response.get_json()
    assert "prediction" in json_data
    assert json_data["prediction"] == [24.0]

def test_predict_model_not_found(client, mocker):
    """Test the predict route when model file is not found."""

    # Mock joblib.load to raise FileNotFoundError
    mocker.patch('joblib.load', side_effect=FileNotFoundError("Model file not found"))

    response = client.post('/predict', json={
        "CHAS": {"0": 0},
        "RM": {"0": 6.575},
        "TAX": {"0": 296.0},
        "PTRATIO": {"0": 15.3},
        "B": {"0": 396.9},
        "LSTAT": {"0": 4.98}
    })

    assert response.status_code == 404
    assert response.data == b"Model file not found"

def test_predict_model_error(client, mocker):
    """Test the predict route when model loading fails with an OS error."""

    # Mock joblib.load to raise an OSError
    mocker.patch('joblib.load', side_effect=OSError("OS error during model loading"))

    response = client.post('/predict', json={
        "CHAS": {"0": 0},
        "RM": {"0": 6.575},
        "TAX": {"0": 296.0},
        "PTRATIO": {"0": 15.3},
        "B": {"0": 396.9},
        "LSTAT": {"0": 4.98}
    })

    assert response.status_code == 500
    assert response.data == b"Model loading failed"

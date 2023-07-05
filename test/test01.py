import sys
sys.path.append('/app/app')
from main import app
from fastapi.testclient import TestClient
version = f"{sys.version_info.major}.{sys.version_info.minor}"


def test_home_page():
    client = TestClient(app)
    response = client.get("/")
    message = f"Hello Abdullah Cay! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    assert response.status_code == 200
    assert response.json() == {"message" : message}

def test_predict():
    client = TestClient(app)
    response = client.get("/predict")
    assert response.status_code == 200
    
    
def test_predict_periods():
    client = TestClient(app)
    response = client.get(f"/predict?periods=a")
    assert response.status_code == 200
    

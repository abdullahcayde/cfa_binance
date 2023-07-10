import sys
sys.path.append('/app/app')
from main import app
from fastapi.testclient import TestClient
version = f"{sys.version_info.major}.{sys.version_info.minor}"


def test_home_page():
    client = TestClient(app)
    response = client.get("/")
    message = f"Hello Eveline Farzane Abdullah! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    assert response.status_code == 200
    assert response.json() == {"message" : message}

def test_predict():
    client = TestClient(app)
    response = client.get("/api/predictall")
    assert response.status_code == 200
    
    
def test_predict_periods():
    client = TestClient(app)
    response = client.get(f"/api/predict/1?periods=a")
    assert response.status_code == 200
    

import pytest
from faker import Faker
from utils.config import Config
from utils.api_client import APIClient


@pytest.fixture
def api_client():
    # Initialize the ApiClient with a base URL and token
    base_url = Config.get_base_url()
    token = "b6f4b4b2699e59e72c57c6fcb0f73484ee4a783d44e76fad4462cc5f6489b925"
    return APIClient(base_url, token)

@pytest.fixture
def generate_user_data(scope="session"):
    fake = Faker()
    return {
        "name": fake.name(),
        "gender": "male",
        "email": fake.email(),
        "status": "active"
    }


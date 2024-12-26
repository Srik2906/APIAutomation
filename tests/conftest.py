import pytest
import os
from dotenv import load_dotenv
from faker import Faker
from utils.config import Config
from utils.api_client import APIClient

load_dotenv()

@pytest.fixture
def api_client():
    # Initialize the ApiClient with a base URL and token
    base_url = Config.get_base_url()
    token = os.getenv("API_TOKEN")
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


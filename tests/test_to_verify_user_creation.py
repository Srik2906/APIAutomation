import allure
import pytest

from tests.conftest import api_client
from utils.config import Config
from utils.api_client import APIClient

@allure.suite("User service")
@pytest.mark.usefixtures("api_client","generate_user_data")
class TestToVerifyUserCreation:

    @allure.title("Create user")
    def test_create_user(self,generate_user_data,api_client):
        user_data = generate_user_data
        create_user_data = api_client.create_user(user_data)
        user_id = create_user_data["id"]
        get_user_data = api_client.get_user(user_id)
        assert create_user_data["id"] == get_user_data["id"],"User not created"

    @allure.title("Update user")
    def test_update_user(self,api_client):
        get_users_data = api_client.get_users()
        user_id = get_users_data[0]["id"]
        updated_data = {"name": "updated name"}
        api_client.update_user(user_id,updated_data)
        get_user_data = api_client.get_user(user_id)
        assert get_user_data["name"] == "updated name","User not updated"

    @allure.title("Delete user")
    def test_delete_user(self,api_client):
        user_id = api_client.get_users()[0]["id"]
        response_data = api_client.delete_user(user_id)
        assert response_data == "", "User not deleted"











import requests


class APIClient:
    def __init__(self, base_url,token=None):
        self.base_url = base_url
        self.token = token
        self.headers = { "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"}

    def create_user(self,user_data):
        response = requests.post(f"{self.base_url}/users",json=user_data,headers=self.headers)
        assert response.status_code == 201, f"User creation failed with status code {response.status_code}"
        return response.json()

    def get_user(self,user_id):
        response = requests.get(f"{self.base_url}/users/{user_id}",headers=self.headers)
        assert response.status_code == 200, f"User retrieval failed with status code {response.status_code}"
        return response.json()

    def get_users(self):
        response = requests.get(f"{self.base_url}/users",headers=self.headers)
        assert response.status_code == 200, f"User retrieval failed with status code {response.status_code}"
        return response.json()

    def update_user(self,user_id,user_data):
        response = requests.patch(f"{self.base_url}/users/{user_id}",json=user_data,headers=self.headers)
        assert response.status_code == 200, f"User update failed with status code {response.status_code}"
        return response.json()

    def delete_user(self,user_id):
        response = requests.delete(f"{self.base_url}/users/{user_id}",headers=self.headers)
        assert response.status_code == 204, f"User deletion failed with status code {response.status_code}"
        return response.text
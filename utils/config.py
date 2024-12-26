from pathlib import Path
import json
import os


class Config:
    @staticmethod
    def get_base_url():
        # Use the current directory (or adjust this to any base path you prefer)
         # Get the directory of this script

        # Define the relative path to your config file (assuming it's located in 'config/urls.json')
        config_path = "/Users/srikanthkrishnan/PycharmProjects/APIAutomation/config/urls.json"
        print(config_path)


        # Load the JSON data from the file
        with open(config_path, "r") as file:
            config_data = json.load(file)

        # Determine the environment from the 'environment' section of the config
        environment = config_data.get("environment", {}).get("env", "prod")  # Default to 'prod' if not found

        # Fetch the base URL for the correct environment (either 'prod' or 'uat')
        base_url = config_data.get(environment, {}).get("Base_URL")

        if not base_url:
            raise KeyError(f"Base_URL for environment '{environment}' is missing in the configuration")

        return base_url


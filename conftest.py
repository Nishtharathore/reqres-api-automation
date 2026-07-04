# conftest.py
import os
import pytest
from dotenv import load_dotenv

load_dotenv()  # loads .env file into environment variables

BASE_URL = "https://reqres.in/api"


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def headers():
    api_key = os.getenv("REQRES_API_KEY")
    if not api_key:
        raise ValueError("REQRES_API_KEY environment variable not set")
    return {"x-api-key": api_key}
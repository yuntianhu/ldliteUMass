import requests
import json
import os
from dotenv import load_dotenv

def okapi_auth(okapi_endpoint, username, password, tenant):
    headers = {
        "X-Okapi-Tenant": tenant,
        "Content-Type": "application/json"  # Ensure this is included if JSON is expected
    }
    payload = {
        "username": username,
        "password": password
    }
    url = okapi_endpoint + "/authn/login-with-expiry"

    response = requests.post(url, headers=headers, json=payload)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)
        print("Response status code:", response.status_code)
        print("Response body:", response.text)  # This prints more details from the server
        return {}, {}  # Return empty since authentication failed

    return response.cookies.get_dict()

def okapi_auth_refresh(okapi_endpoint, username, password, tenant):
    headers = {
        "X-Okapi-Tenant": tenant,
        "Content-Type": "application/json"  # Ensure this is included if JSON is expected
    }
    payload = {
        "username": username,
        "password": password
    }
    url = okapi_endpoint + "/authn/refresh"

    response = requests.post(url, headers=headers, cookies={"folioRefreshToken":refreshToken})
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)
        print("Response status code:", response.status_code)
        print("Response body:", response.text)  # This prints more details from the server
        return {}, {}  # Return empty since authentication failed

    return response.cookies.get_dict()



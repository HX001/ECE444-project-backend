import pytest
import json
#from app import flask_app, db
import requests

# test case created by Yuqing Zhao
def test_login():
    """Test login and logout using helper functions"""
    url = "http://0.0.0.0:5000/login/"
    data = {"username": "Kafka", "password": "123456"}
    res1 = requests.post(url, json=data)
    assert 'Username does not exist' in res1.json()['message']

    data = {"username": "Tom", "password": "123"}
    res2 = requests.post(url, json=data)
    assert 'Successfully logged in' in res2.json()['message']

    data = {"username": "Tom", "password": "1234"}
    res3 = requests.post(url, json=data)
    assert 'Password not matched' in res3.json()['message']

# test case created by Yitong Wang
def test_signup():
    # Test if an existing user is able to sign up
    url = "http://127.0.0.1:5000/signup/"
    existing_user = {
        "username": "Tom",
        "password": "123456",
        "email": "123@gmail.com"
    }
    rv = requests.post(url, json=existing_user)
    assert 'fail' in rv.json()['status']
    assert 'Username already exists' in rv.json()['message']

    # Test if an new user is able to sign up
    new_user = {
        "username": "New User",
        "password": "123456",
        "email": "123@gmail.com"
    }
    rv = requests.post(url, json=new_user)
    assert 'success' in rv.json()['status']
    assert 'Successfully signed up' in rv.json()['message']

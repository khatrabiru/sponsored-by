from curses.ascii import NUL
from email.mime import base
from pickle import NONE
import re
from urllib import response

import py
import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient

from app.main import app
client = TestClient(app)


@pytest.mark.asyncio
async def test_main():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


@pytest.mark.asyncio
async def test_get_event():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/event/1")

    assert response.status_code == 200
    assert response.json()['name'] == 'EventByTests'
    assert 'name' in response.json()
    assert 'sponsors' in response.json()


@pytest.mark.asyncio
async def test_create_event():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/event/",
            json={
                "name": "EventByTests123",
                "image_url": "string",
                "description": "string",
                "short_description": "string",
                "organized_by": "string",
                "location": "string",
                "category": "string",
                "date": "2022-09-30",
                "sponsors": [1, 2, 3]
            }
        )
    assert response.status_code == 201
    assert response.json()['name'] == 'EventByTests123'
    assert response.json()['sponsors'] == [1, 2, 3]


@pytest.mark.asyncio
async def test_delete_event():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response1 = await ac.post(
            "/event/",
            json={
                "name": "TestName",
                "image_url": "string",
                "description": "string",
                "short_description": "string",
                "organized_by": "string",
                "location": "string",
                "category": "string",
                "date": "2022-09-30",
                "sponsors": [1, 2]
            }
        )
        id = response1.json()['id']
        response2 = await ac.delete(f'/event/{id}')
        response3 = await ac.get(f'/event/{id}')

    assert response1.status_code == 201
    assert response2.status_code == 204
    assert response3.status_code == 404


@pytest.mark.asyncio
async def test_update_event():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response1 = await ac.post(
            "/event/",
            json={
                "name": "TestNamebeforeUpdate",
                "image_url": "string",
                "description": "string",
                "short_description": "string",
                "organized_by": "string",
                "location": "string",
                "category": "string",
                "date": "2022-09-30",
                "sponsors": [1, 2]
            }
        )

        id = response1.json()['id']
        url = f'/event/{id}'
        response2 = await ac.put(
            url,
            json={
                "name": "TestNameAfterUpdate",
                "image_url": "string",
                "description": "string",
                "short_description": "string",
                "organized_by": "string",
                "location": "string",
                "category": "string",
                "date": "2022-09-30",
                "sponsors": [1, 3]
            }
        )
        response3 = await ac.get(url)
    assert response1.status_code == 201
    assert response2.status_code == 204
    assert response3.status_code == 200

    assert response1.json()['name'] == 'TestNamebeforeUpdate'
    assert response3.json()['name'] == 'TestNameAfterUpdate'
    assert response1.json()['id'] == response3.json()['id']
    assert response1.json()['sponsors'] != response3.json()['sponsors']
    assert len(response1.json()['sponsors']) == len(response3.json()['sponsors'])


@pytest.mark.asyncio
async def test_create_sposor():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {
                "name": "Sponsor1",
                "image_url": "string",
                "description": "string",
                "short_description": "string",
                "headquarter_location": "string",
                "website_url": "string",
                "facebook_url": "string",
                "twitter_url": "string",
                "instagram_url": "string",
                "events": [
                ]
            }
        response = await ac.post("/sponsor/", json=payload)

    assert response.status_code == 201
    assert response.json()['name'] == 'Sponsor1'
    assert 'events' in response.json()


@pytest.mark.asyncio
async def test_get_sponsor():
    async with AsyncClient(app=app, base_url = "http://test") as ac:
        payload = {
                "name": "Sponsor1",
                "image_url": "string",
                "description": "string",
                "short_description": "string",
                "headquarter_location": "string",
                "website_url": "string",
                "facebook_url": "string",
                "twitter_url": "string",
                "instagram_url": "string",
                "events": [
                ]
            }
        response1 = await ac.post('/sponsor/', json=payload)
        id = response1.json()['id']
        response2 = await ac.get(f'/sponsor/{id}')
    
    assert response1.status_code == 201
    assert response2.status_code == 200
    assert 'name' in response2.json()
    assert response2.json()['name'] == 'Sponsor1'



@pytest.mark.asyncio
async def test_delete_sponsor():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {
                "name": "Sponsor2",
                "image_url": "string",
                "description": "string",
                "short_description": "string",
                "headquarter_location": "string",
                "website_url": "string",
                "facebook_url": "string",
                "twitter_url": "string",
                "instagram_url": "string",
                "events": [
                ]
            }
        response1 = await ac.post("/sponsor/", json=payload)
        id = response1.json()['id']
        response2 = await ac.delete(f'/sponsor/{id}')
        response3 = await ac.get(f'/sponsor/{id}')
    
    assert response1.status_code == 201
    assert response2.status_code == 204
    assert response3.status_code == 404


@pytest.mark.asyncio
async def test_update_sponsor():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        payload = {
                "name": "Sponsor2",
                "image_url": "string",
                "description": "string",
                "short_description": "string",
                "headquarter_location": "string",
                "website_url": "string",
                "facebook_url": "string",
                "twitter_url": "string",
                "instagram_url": "string",
                "events": [
                ]
            }
        response1 = await ac.post("/sponsor/", json=payload)
        payload['name'] = "Sponsor3"
        id = response1.json()['id']
        response2 = await ac.put(f'/sponsor/{id}', json=payload)
        response3 = await ac.get(f'/sponsor/{id}')
    
    assert response1.status_code == 201
    assert response2.status_code == 204
    assert response3.status_code == 200

    assert response1.json()['name'] == 'Sponsor2'
    assert response3.json()['name'] == "Sponsor3"

    assert response1.json() != response3.json()
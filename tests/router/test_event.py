# from fastapi.testclient import TestClient
# from app.main import app

# client = TestClient(app)


# def test_get_all():
#     response = client.get("/event/")
#     assert response.status_code == 200


# def test_get():
#     response = client.get("/event/1/")
#     assert response.status_code == 200
#     data = response.json()
#     assert data['name'] == 'Event1'
#     assert data['sponsors'] == [1, 2]


# def test_create():
#     response = client.post(
#         "/event/",
#         json={
#             "name": "EventByTests",
#             "image_url": "string",
#             "description": "string",
#             "short_description": "string",
#             "organized_by": "string",
#             "location": "string",
#             "category": "string",
#             "date": "2022-09-30",
#             "sponsors": [1]
#         }
#     )
#     assert response.status_code == 200
#     data = response.json()
#     assert data['name'] == 'EventByTests'
#     assert data['sponsors'] == [1]


# def test_delete():
#     response = client.post(
#         "/event/",
#         json={
#             "name": "EventByTests",
#             "image_url": "string",
#             "description": "string",
#             "short_description": "string",
#             "organized_by": "string",
#             "location": "string",
#             "category": "string",
#             "date": "2022-09-30",
#             "sponsors": [1, 2, 3]
#         }
#     )
#     assert response.status_code == 200
#     data = response.json()
#     assert data['name'] == 'EventByTests'
#     assert data['sponsors'] == [1, 2, 3]
#     id = data['id']
#     url = '/event/' + str(id)
#     response = client.delete(url)
#     assert response.status_code == 200


# def test_update():
#     response = client.post(
#         "/event/",
#         json={
#             "name": "EventByTests1",
#             "image_url": "string",
#             "description": "string",
#             "short_description": "string",
#             "organized_by": "string",
#             "location": "string",
#             "category": "string",
#             "date": "2022-09-30",
#             "sponsors": [1, 2, 3]
#         }
#     )
#     assert response.status_code == 200
#     data = response.json()
#     assert data['name'] == 'EventByTests1'
#     assert data['sponsors'] == [1, 2, 3]
#     id = data['id']
#     url = '/event/' + str(id)
#     response = client.put(
#         url,
#         json={
#             "name": "EventByTestsUpdated",
#             "image_url": "string",
#             "description": "string",
#             "short_description": "string",
#             "organized_by": "string",
#             "location": "string",
#             "category": "string",
#             "date": "2022-09-30",
#             "sponsors": [2, 3, 4]
#         }
#     )
#     assert response.status_code == 200

#     response = client.get("/event/" + str(id))
#     assert response.status_code == 200
#     data = response.json()
#     assert data['name'] == 'EventByTestsUpdated'

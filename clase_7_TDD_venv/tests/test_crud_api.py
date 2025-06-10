import time


def test_root(test_client):
    response = test_client.get("/api/healthchecker")
    assert response.status_code == 200
    assert response.json() == {"message": "EL API está vivo!!"}


def test_create_get_user(test_client, user_payload):
    response = test_client.post("/api/users/", json=user_payload)
    response_json = response.json()
    assert response.status_code == 201

    # Obtiene el usuario creado
    response = test_client.get(f"/api/users/{user_payload['id']}")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["Status"] == "Success"
    assert response_json["User"]["id"] == user_payload["id"]
    assert response_json["User"]["address"] == "123 Farmville"
    assert response_json["User"]["first_name"] == "John"
    assert response_json["User"]["last_name"] == "Doe"


def test_create_update_user(test_client, user_payload, user_payload_updated):
    response = test_client.post("/api/users/", json=user_payload)
    response_json = response.json()
    assert response.status_code == 201

    # ACtualizamos el usuario creado
    time.sleep(
        1
    )  # Sleep por un segundo para asegurarnos quw updatedAt es diferente (la precisión de datetime es baja en SQLite)


    response = test_client.put(
        f"/api/users/{user_payload['id']}", json=user_payload_updated
    )
    response_json = response.json()
    assert response.status_code == 202
    assert response_json["Status"] == "Success"
    assert response_json["User"]["id"] == user_payload["id"]
    assert response_json["User"]["address"] == "321 Farmville"
    assert response_json["User"]["first_name"] == "Jane"
    assert response_json["User"]["last_name"] == "Doe"
    assert response_json["User"]["activated"] is True
    assert (
        response_json["User"]["updatedAt"] is not None
        and response_json["User"]["updatedAt"] > response_json["User"]["createdAt"]
    )


def test_create_delete_user(test_client, user_payload):
    response = test_client.post("/api/users/", json=user_payload)
    response_json = response.json()
    assert response.status_code == 201

    # ELimina el usuario creado
    response = test_client.delete(f"/api/users/{user_payload['id']}")
    response_json = response.json()
    assert response.status_code == 202
    assert response_json["Status"] == "Success"
    assert response_json["Message"] == "User eliminado con éxito"

    # Obtiene el usuario eliminado
    response = test_client.get(f"/api/users/{user_payload['id']}")
    assert response.status_code == 404
    response_json = response.json()
    assert response_json["detail"] == f"No existe un usuario con este id: `{user_payload['id']}`"


def test_get_user_not_found(test_client, user_id):
    response = test_client.get(f"/api/users/{user_id}")
    assert response.status_code == 404
    response_json = response.json()
    assert response_json["detail"] == f"No existe un usuario con este id: `{user_id}`"


def test_get_user_not_found(test_client, user_id):
    response = test_client.get(f"/api/users/{user_id}")
    assert response.status_code == 404
    response_json = response.json()
    assert response_json["detail"] == f"No existe un usuario con este id: `{user_id}`"


def test_create_user_wrong_payload(test_client):
    response = test_client.post("/api/users/", json={})
    assert response.status_code == 422


def test_update_user_wrong_payload(test_client, user_id, user_payload_updated):
    user_payload_updated["first_name"] = (
        True  # El nombre debe ser un String no un booleano
    )
    response = test_client.put(f"/api/users/{user_id}", json=user_payload_updated)
    assert response.status_code == 422
    response_json = response.json()
    assert response_json == {
        "detail": [
            {
                "type": "string_type",
                "loc": ["body", "first_name"],
                "msg": "Input should be a valid string",
                "input": True,
            }
        ]
    }


def test_update_user_doesnt_exist(test_client, user_id, user_payload_updated):
    response = test_client.put(f"/api/users/{user_id}", json=user_payload_updated)
    assert response.status_code == 404
    response_json = response.json()
    assert response_json["detail"] == f"No existe un usuario con este id: `{user_id}`"



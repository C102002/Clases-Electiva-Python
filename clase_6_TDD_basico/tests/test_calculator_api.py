def test_add(client, json_headers, json_data):
    response = client.post("/api/v1/calculadora/add/", headers=json_headers, json=json_data)
    assert response.status_code == 200
    assert response.json()["status"] == "Success"
    assert response.json()["operation_response"]["result"] == 18


def test_subtract(client, json_headers, json_data):
    response = client.post("/api/v1/calculadora/subtract/", headers=json_headers, json=json_data)
    assert response.status_code == 200
    assert response.json()["status"] == "Success"
    assert response.json()["operation_response"]["result"] == -6
    


def test_multiply(client, json_headers, json_data):
    response = client.post("/api/v1/calculadora/multiply/", headers=json_headers, json=json_data)
    assert response.status_code == 200
    assert response.json()["status"] == "Success"
    assert response.json()["operation_response"]["result"] == 72


def test_divide(client, json_headers, json_data):
    response = client.post("/api/v1/calculadora/divide/", headers=json_headers, json=json_data)
    assert response.status_code == 200
    assert response.json()["status"] == "Success"
    assert response.json()["operation_response"]["result"] == 0.5


def test_divide_by_zero(client, json_headers):
    response = client.post("/api/v1/calculadora/divide/", headers=json_headers, json={"oper1": 6, "oper2": 0})
    assert response.status_code == 400
    assert response.json()["detail"] == "No puede dividir entre cero"
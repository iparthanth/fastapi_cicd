from fastapi.testclient import TestClient
from src.main import api

client = TestClient(api)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Ticket Booking System"}

def test_get_tickets_initially_empty():
    response = client.get("/ticket")
    assert response.status_code == 200
    assert response.json() == []

def test_add_ticket():
    ticket = {
        "id": 1,
        "flight_name": "Flight A",
        "flight_date": "2025-10-15",
        "flight_time": "14:30",
        "destination": "Paris"
    }
    response = client.post("/ticket", json=ticket)
    assert response.status_code == 200
    assert response.json() == ticket

def test_update_ticket():
    updated = {
        "id": 1,
        "flight_name": "Flight A (Rescheduled)",
        "flight_date": "2025-10-16",
        "flight_time": "16:00",
        "destination": "Paris"
    }
    response = client.put("/ticket/1", json=updated)
    assert response.status_code == 200
    assert response.json() == updated

def test_delete_ticket():
    response = client.delete("/ticket/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "flight_name": "Flight A (Rescheduled)",
        "flight_date": "2025-10-16",
        "flight_time": "16:00",
        "destination": "Paris"
    }

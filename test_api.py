"""
Примеры тестов для проверки работы API
Запуск: python test_examples.py
"""
import requests
import json

BASE_URL = "http://localhost:5000/api/tasks"

def print_response(method, url, status, response):
    print(f"{method} {url}")
    print(f"Статус: {status}")
    print(f"Ответ: {response}\n")

def test_api():
    print("=== Тестирование Task Manager API ===\n")
    
    # 1. GET все задачи
    resp = requests.get(BASE_URL)
    print_response("GET", BASE_URL, resp.status_code, resp.json())
    
    # 2. POST создать задачу
    resp = requests.post(BASE_URL, json={"title": "Протестировать API"})
    print_response("POST", BASE_URL, resp.status_code, resp.json())
    
    # 3. PUT обновить статус (ID=1)
    resp = requests.put(f"{BASE_URL}/1", json={"status": "done"})
    print_response("PUT", f"{BASE_URL}/1", resp.status_code, resp.json())
    
    # 4. GET конкретную задачу (ID=1)
    resp = requests.get(f"{BASE_URL}/1")
    print_response("GET", f"{BASE_URL}/1", resp.status_code, resp.json())
    
    # 5. DELETE задачу (ID=1)
    resp = requests.delete(f"{BASE_URL}/1")
    print_response("DELETE", f"{BASE_URL}/1", resp.status_code, "No Content" if resp.status_code == 204 else resp.json())
    
    print("=== Тест завершен ===")

if __name__ == "__main__":
    test_api()
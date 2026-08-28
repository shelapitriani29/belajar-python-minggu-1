import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")

if response.status_code == 200:

    data = response.json()

    for todo in data[:5]:
        print(f"ID: {todo['id']} | Judul: {todo['title']}")

else:

    print("Gagal mengambil data!")
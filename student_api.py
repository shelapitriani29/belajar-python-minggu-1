import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:

    students = response.json()

    for student in students[:5]:

        print(f"ID: {student['id']}")
        print(f"Nama: {student['name']}")
        print(f"Email: {student['email']}")
        print("-" * 30)

else:

    print("Gagal mengambil data!")
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:

    students = response.json()

    search = input("Masukkan nama siswa: ").lower()

    found = False

    for student in students:

        if student["name"].lower() == search:

            print("Siswa ditemukan!")
            print(f"ID: {student['id']}")
            print(f"Nama: {student['name']}")
            print(f"Email: {student['email']}")

            found = True

    if found == False:

        print("Siswa tidak ditemukan.")

else:

    print("Gagal mengambil data!")
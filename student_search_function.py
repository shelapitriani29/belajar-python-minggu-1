import requests


def get_students():

    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    if response.status_code == 200:

        return response.json()

    else:

        return None


def search_student(students, search):

    for student in students:

        if student["name"].lower() == search.lower():

            return student

    return None


students = get_students()

if students:

    search = input("Masukkan nama siswa: ")

    student = search_student(students, search)

    if student:

        print("Siswa ditemukan!")
        print(f"ID: {student['id']}")
        print(f"Nama: {student['name']}")
        print(f"Email: {student['email']}")

    else:

        print("Siswa tidak ditemukan.")

else:

    print("Gagal mengambil data dari API.")
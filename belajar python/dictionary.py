import json

data_json = '''
{
    "name": "Shela",
    "age": 18,
    "hobbies": ["coding", "reading", "gaming"]
}
'''

student = json.loads(data_json)

print(f"Nama: {student['name']}")
print(f"Umur: {student['age']}")
print("Hobi:")

for hobby in student["hobbies"]:
    print(f"- {hobby}")
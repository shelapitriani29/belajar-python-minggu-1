import requests

data = {
    "name": "Shela",
    "age": 18,
    "major": "PPLG"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

print(response.status_code)
print(response.json())
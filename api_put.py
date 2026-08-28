import requests

data = {
    "name": "Shela",
    "age": 19,
    "major": "PPLG"
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=data
)

print(response.status_code)
print(response.json())
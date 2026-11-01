import httpx

response = httpx.get(
    "http://127.0.0.1:8000/hello", headers={"X-Custom-Header", "test"}, timeout=10
)

print("Status: ", response.status_code)
print("Headers: ", dict(response.headers))
print("Body: ", response.text)

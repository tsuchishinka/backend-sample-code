import redis

client = redis.Redis(host="127.0.0.1", port=6379, db=0, decode_responses=True)

print(client.ping())

client.set("user:1:name", "太郎", ex=10)
print(client.get("user:1:name"))

client.set("user:2:name", "一郎", ex=600)

client.delete("user:1:name")
print(client.get("user:1:name"))

client.close()

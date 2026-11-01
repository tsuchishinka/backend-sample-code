text = "😀"

data = text.encode("utf-8")
print(data)
print(list(data))

restored = data.decode("utf-8")
print(restored)

import time


def timer():
    time.sleep(1)
    yield "1秒後"
    time.sleep(1)
    yield "2秒後"
    time.sleep(1)
    yield "3秒後"


if __name__ == "__main__":
    # print(timer())
    generator = timer()
    for msg in generator:
        print(msg)

from contextlib import contextmanager


@contextmanager
def execute():
    print("enter")
    try:
        yield
    finally:
        print("exit")


class Sample:
    def execute(self):
        print("execute")


@contextmanager
def sample():
    print("enter")
    try:
        yield Sample()
    finally:
        print("exit")


if __name__ == "__main__":
    with execute() as e:
        print("処理中")

    with sample() as s:
        s.execute()

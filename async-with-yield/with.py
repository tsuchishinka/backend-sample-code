class Sample:
    def __enter__(self):
        print(self.__enter__.__name__)
        return self

    def execute(self):
        print(self.execute.__name__)

    def __exit__(self, exc_type, exc, tb):
        print(self.__exit__.__name__)


if __name__ == "__main__":
    with Sample() as s:
        s.execute()

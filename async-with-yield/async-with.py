import asyncio


class Sample:
    async def __aenter__(self):
        print(self.__aenter__.__name__)
        return self

    async def execute(self):
        await asyncio.sleep(1)
        print(self.execute.__name__)

    async def __aexit__(self, exc_type, exc, tb):
        print(self.__aexit__.__name__)


async def main():
    async with Sample() as s:
        await s.execute()


if __name__ == "__main__":
    asyncio.run(main())

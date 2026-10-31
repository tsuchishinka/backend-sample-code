import asyncio
from contextlib import asynccontextmanager


@asynccontextmanager
async def execute():
    print("enter")
    try:
        yield
    finally:
        print("exit")


class Sample:
    async def execute(self):
        await asyncio.sleep(1)
        print("execute")


@asynccontextmanager
async def sample():
    print("enter")
    try:
        yield Sample()
    finally:
        print("exit")


async def main():
    async with execute():
        await asyncio.sleep(1)
        print("実行")

    async with sample() as s:
        await s.execute()


if __name__ == "__main__":
    asyncio.run(main())

import asyncio
from contextlib import asynccontextmanager


@asynccontextmanager
async def sample():
    print("enter")
    try:
        await asyncio.sleep(1)
        yield
    finally:
        print("exit")


async def main():
    async with sample():
        print("実行")


if __name__ == "__main__":
    asyncio.run(main())

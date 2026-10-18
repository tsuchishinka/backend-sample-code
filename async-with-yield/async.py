import asyncio


async def hello_world_1():
    print(hello_world_1.__name__ + "開始")
    await asyncio.sleep(1)
    print(hello_world_1.__name__ + "実行")
    await asyncio.sleep(1)
    print(hello_world_1.__name__ + "終了")


async def hello_world_2():
    print(hello_world_2.__name__ + "開始")
    await asyncio.sleep(1)
    print(hello_world_2.__name__ + "実行")
    await asyncio.sleep(1)
    print(hello_world_2.__name__ + "終了")


async def main():
    await asyncio.gather(hello_world_1(), hello_world_2())


if __name__ == "__main__":
    asyncio.run(main())

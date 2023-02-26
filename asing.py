import asyncio,time


async def f():  # Asinhrono izvrsavanje
    await asyncio.sleep(2)
    print("Hello world")    


x = f()
asyncio.run(x)
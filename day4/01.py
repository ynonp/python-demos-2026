import asyncio
import time

async def async_calc_demo(label):
    result = 0
    for i in range(10):
        print(f"{label}: {i}")
        await asyncio.to_thread(time.sleep, 1)
        result += i
    return result

async def main():
    print(time.time())
    results = await asyncio.gather(
        async_calc_demo("A"),
        async_calc_demo("B"),
    )
    print(time.time())
    print(results)

asyncio.run(main())
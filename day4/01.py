import asyncio
import time

async def async_calc_demo():
    result = 0
    for i in range(10):
        await asyncio.sleep(1)
        result += i
    return result

async def main():
    print(time.time())
    results = await asyncio.gather(
        async_calc_demo(),
        async_calc_demo(),
    )
    print(time.time())
    print(results)

asyncio.run(main())
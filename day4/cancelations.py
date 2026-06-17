import asyncio

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(1)

async def cancel_after(other, timeout):
    await asyncio.sleep(timeout)
    other.cancel()

async def main():
    t1 = asyncio.create_task(print_numbers())
    t2 = asyncio.create_task(cancel_after(t1, 3))
    try:
        await asyncio.gather(t1, t2)
    except asyncio.CancelledError:
        print("A task was cancelled")

asyncio.run(main())
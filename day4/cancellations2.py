import asyncio


async def print_numbers():
    i = 0
    try:
        while True:
            await asyncio.sleep(1)
            print(i)
            i += 1

    finally:
        print("Waiting 5 extra seconds")
        await asyncio.sleep(5)
        print("done")


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
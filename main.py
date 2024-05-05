import asyncio
import logging
import sys
from app import main


async def pprint():
    while True:
        print("hello111")
        await asyncio.sleep(2)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    # asyncio.create_task(pprint())
    asyncio.run(main())

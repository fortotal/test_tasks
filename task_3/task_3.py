import asyncio
from aiohttp import ClientSession
import nest_asyncio
from tqdm import tqdm

nest_asyncio.apply()


async def fetch(url, session):
    async with session.get(url) as response:
        return await response.read()


async def run(r, url):
    tasks = []

    async with ClientSession() as session:
        for i in range(int(r)):
            task = asyncio.create_task(fetch(url.format(i), session))
            tasks.append(task)

        pbar = tqdm(total=len(tasks))
        for f in asyncio.as_completed(tasks):
            value = await f
            pbar.set_description('', refresh=True)
            pbar.update()


if __name__ == '__main__':
    count = input('Введите кол-во: ')
    url = input('Введите url: ')
    asyncio.run(run(count, url))

import aiosqlite
import asyncio

async def async_fetch_users():
    async with aiosqlite.connect('ALX_prodev.db') as db:
        async with db.execute("SELECT * FROM users") as cursor:
            return await cursor.fetchall()


async def async_fetch_older_users():
    async with aiosqlite.connect('ALX_prodev.db') as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            return await cursor.fetchall()

async def main():
    results = await asyncio.gather(
        async_fetch_users(), async_fetch_older_users()
    )
    all_users, older_users = results
    print("All users:", all_users)
    print("Older users:", older_users)

if __name__ == "__main__":
   asyncio.run(main())
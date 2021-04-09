from asyncpg import create_pool
from os import getenv

CREATE = """CREATE TABLE IF NOT EXISTS Users (
  id BIGINT NOT NULL PRIMARY KEY,
  xp BIGINT NOT NULL,
  last_xp TIMESTAMP NOT NULL DEFAULT NOW(),
  balance BIGINT NOT NULL DEFAULT 0,
  last_work TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS Warns (
  id SERIAL PRIMARY KEY,
  user_id BIGINT NOT NULL,
  reason VARCHAR(2000)
);"""

class Database:
    """A database interface for the bot to connect to Postgres."""

    def __init__(self):
        self.pool = None

    async def setup(self):
        self.pool = await create_pool(dsn=getenv("DATABASE_URL"))

        await self.execute(CREATE)

    async def execute(self, query: str, *args):
        async with self.pool.acquire() as conn:
            await conn.execute(query, *args)

    async def fetchrow(self, query: str, *args):
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(query, *args)

    async def fetch(self, query: str, *args):
        async with self.pool.acquire() as conn:
            return await conn.fetch(query, *args)

    async def create_user(self, id: int):
        return await self.fetchrow("INSERT INTO Users (id, xp) VALUES ($1, $2) RETURNING *;", id, 0)

    async def update_user_xp(self, id: int, xp: int):
        await self.execute("UPDATE Users SET xp = xp + $1, last_xp = NOW() WHERE id = $2;", xp, id)
    
    async def get_leaderboard(self):
        return await self.fetch("SELECT * FROM Users ORDER BY xp DESC LIMIT 15;")
    async def get_user(self, id: int):
        user =  await self.fetchrow("SELECT * FROM Users WHERE id = $1;", id)
        if user:
            return user
        return await self.create_user(id)
        
    async def create_warn(self, user_id: int, reason: str):
        warn = await self.fetchrow("INSERT INTO Warns (user_id, reason) VALUES ($1, $2) RETURNING *;", user_id, reason)
        return warn['id']

    async def get_warns(self,id):
        await self.fetchrow("SELECT * FROM warns WHERE user_id = $1;", id)

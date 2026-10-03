from fastapi import HTTPException, status
from sqlalchemy import func, select
from database import engine
from models.post import posts
from schemas.post import PostIn, PostUpdateIn


class PostService:

    async def read_all(
        self,
        published: bool,
        limit: int,
        skip: int = 0
    ):
        query = (
            posts.select()
            .where(posts.c.published == published)
            .limit(limit)
            .offset(skip)
        )

        async with engine.connect() as conn:
            result = await conn.execute(query)
            return result.mappings().all()

    async def create(self, post: PostIn) -> int:
        command = posts.insert().values(
            title=post.title,
            content=post.content,
            published_at=post.published_at,
            published=post.published,
        )

        async with engine.begin() as conn:
            result = await conn.execute(command)

        return result.inserted_primary_key[0]

    async def read(self, id: int):
        return await self.__get_by_id(id)

    async def update(self, id: int, post: PostUpdateIn):
        total = await self.count(id)

        if not total:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Post not found"
            )

        data = post.model_dump(exclude_unset=True)

        command = (
            posts.update()
            .where(posts.c.id == id)
            .values(**data)
        )

        async with engine.begin() as conn:
            await conn.execute(command)

        return await self.__get_by_id(id)

    async def delete(self, id: int) -> None:
        command = posts.delete().where(posts.c.id == id)

        async with engine.begin() as conn:
            await conn.execute(command)

    async def count(self, id: int) -> int:
        query = (
            select(func.count())
            .select_from(posts)
            .where(posts.c.id == id)
        )

        async with engine.connect() as conn:
            result = await conn.execute(query)
            return result.scalar_one()

    async def __get_by_id(self, id: int):
        query = posts.select().where(posts.c.id == id)

        async with engine.connect() as conn:
            result = await conn.execute(query)
            post = result.mappings().first()

        if not post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Post not found"
            )

        return post

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from core.config import settings


class HelperDb:
    def __init__(
        self,
        url: str,
        echo: bool,
        echo_pool: bool,
        max_overflow: int,
        pool_size: int,
    ):
        self.async_engine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            max_overflow=max_overflow,
            pool_size=pool_size,
        )
        self.fabric_session = async_sessionmaker(
            bind=self.async_engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def dispose(self):
        await self.async_engine.dispose()

    async def session_getter(self):
        async with self.fabric_session() as session:
            yield session
            await session.close()


db_helper = HelperDb(
    url=settings.db.url,
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    max_overflow=settings.db.max_overflow,
    pool_size=settings.db.pool_size,
)

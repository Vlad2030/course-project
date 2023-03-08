from sqlalchemy import create_engine


async def sql_engine(db_url: str, debug: bool = False) -> None:
    return create_engine(url=db_url, echo=debug)

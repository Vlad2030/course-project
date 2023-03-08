from sqlalchemy.orm import Session
from databases.engine import sql_engine

engine = sql_engine(db_url="idk://", debug=True)


async def connection(function: function) -> None:
    def wrapper():
        with Session(engine) as session:
            function()
            session.add_all(function.__getattribute__)
            session.commit

    return wrapper

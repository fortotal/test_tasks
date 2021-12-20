import typing as tp

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text

from src.cat import Cat


class DB_Client:
    def __init__(
            self,
            user_name: str = 'user',  # кароч, мне лень таскать где-то пароли, я их захардкожу в код
            password: str = 'password',
            host_name: str = 'db',
            db_name: str = 'db',
            port: int = 5433,
    ):
        self.engine = create_engine(
            f'postgresql://{user_name}:{password}@{host_name}:{port}/{db_name}',
        )
        self.init = False

    def init_db(self):

        meta = MetaData()

        cats = Table(
            'cats', meta,
            Column('nickname', String, primary_key=True),
            Column('age', Integer),
            Column('breed', String),
            Column('img_path', String),
            Column('description', String),
        )  # этим тоже не горжусь
        meta.create_all(self.engine)
        with self.engine.connect() as conn:
            escaped_sql = text(open('shop_skill.sql').read())
            conn.execute(escaped_sql)

    def get_cats(self, age: int, breed: str) -> tp.List:
        if self.init == False:
            self.init_db()
            self.init = True

        statement = "SELECT * FROM public.cats"

        with self.engine.connect() as conn:
            if age is not None:
                if int(age) == 0:
                    statement += " WHERE age < 12"


                if int(age) == 1:
                    statement += " WHERE age > 12"

            if breed is not None:
                if age is not None:
                    statement += f" AND breed = '{breed}'"
                else:
                    statement += f" WHERE breed = '{breed}'"

            result_set = conn.execute(statement)

        cats = [Cat(*result) for result in result_set]
        return cats

    def get_cat_by_name(self, name: str):
        statement = f"SELECT * FROM cats WHERE nickname = '{name}'"
        with self.engine.connect() as conn:
            cat = Cat(*list(conn.execute(statement))[0])
        return cat

from collections import namedtuple
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class UserRepository:
    """class to manage User Repository"""

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """insert data in user entity
        :param - name: person name
               - password: user password
        :return
        """

        insert_data = namedtuple("Users", "id name, password")

        with DBConnectionHandler() as db:
            try:

                new_user = Users(name=name, password=password)
                db.session.add(new_user)
                db.session.commit()

                return insert_data(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )

            except:
                db.session.rollback()
                raise
            finally:
                db.session.close()

        return None

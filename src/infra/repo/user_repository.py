from typing import List
from src.domain.models import Users
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UsersModel


class UserRepository:
    """class to manage User Repository"""

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """insert data in user entity
        :param - name: person name
               - password: user password
        :return
        """

        with DBConnectionHandler() as db:
            try:

                new_user = UsersModel(name=name, password=password)
                db.session.add(new_user)
                db.session.commit()

                return Users(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )

            except:
                db.session.rollback()
                raise
            finally:
                db.session.close()

        return None

    @classmethod
    def select_user(cls, user_id: int = None, name: str = None) -> List[Users]:
        """Select data in User Entity"""

        try:
            query_data = None

            if user_id and not name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=user_id)
                        .one()
                    )
                    query_data = [data]

            elif name and not user_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(name=name)
                        .one()
                    )
                    query_data = [data]

            elif name and user_id:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersModel)
                        .filter_by(id=user_id, name=name)
                        .one()
                    )
                    query_data = [data]

            return query_data

        except:
            db_connection.session.rollback()
            raise

        finally:
            db_connection.session.close()

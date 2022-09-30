from project.dao.models import User
from project.dao.base import BaseDAO


class UserDAO(BaseDAO):
    def get_by_email(self, email: str):
        """get user by email"""
        try:
            user = self.session.query(User).filter(User.email == email).one()
            return user
        except:
            return None

    def create(self, data: dict):
        """create user"""
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return user

    def update_by_email(self, data, email):
        """update user by email"""
        self.session.query(User).filter(User.email == email).update(data)
        self.session.commit()

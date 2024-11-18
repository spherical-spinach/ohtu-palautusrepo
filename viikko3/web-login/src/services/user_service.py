from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if self._user_repository.find_by_username(username):
            raise UserInputError("Problem with registration")
        if not username or not password:
            raise UserInputError("Username and password are required")
        if len(username) < 3 or not username.isalpha() or not username.islower():
            raise UserInputError("Username has to be only lowercase letters with minimum length of 3")
        if len(password) < 8 or password.isalpha():
            raise UserInputError("Password min length is 8 and can't consist only of letters")
        if not password == password_confirmation:
            raise UserInputError("Password and its confirmation doesn't match!")
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa


user_service = UserService()

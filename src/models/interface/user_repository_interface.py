from abc import ABC
from sqlite3 import Connection


class UserRepositoryInterface(ABC):
    def __init__(self, conn: Connection) -> None:
        pass

    @classmethod
    def registry_user(self, username: str, password: str) -> None:
        pass

    @classmethod
    def edit_balance(self, user_id: int, new_balance: float) -> None:
        pass

    @classmethod
    def get_user_by_username(self, username: str) -> tuple[int, str, str]:
        pass

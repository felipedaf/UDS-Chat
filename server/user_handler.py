from .user import User
class UserHandler:
    def __init__(self):
        self.users = dict()

    def get_user(self, user_addr):
        if user_addr in self.users:
            return self.users[user_addr]

        return None

    def get_all_users(self):
        return self.users.values

    def add_user(self, user_addr, name, conn):
        if not user_addr in self.users:
            self.users[user_addr] = User(user_addr, name, conn)

    def remove_user(self, user_addr):
        del self.users[user_addr]

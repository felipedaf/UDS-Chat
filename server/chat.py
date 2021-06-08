from message import Message
class Chat:
    def __init__(self, addr_user1, addr_user2):
        self.user1 = addr_user1
        self.user2 = addr_user2
        self.messages = []

    def add_message(self, addr_sender, message):
        new_message = Message(addr_sender, message)
        self.messages.append(new_message)

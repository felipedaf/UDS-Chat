from .chat import Chat

class ChatHandler:
    def __init__(self):
        self.chats = dict()

    def __get_valid_chat(self, addr_user1, addr_user2):
        hash1 = hash((addr_user1, addr_user2))
        hash2 = hash((addr_user2, addr_user1))

        if hash1 in self.chats:
            return hash1
        elif hash2 in self.chats:
            return hash2

        return None

    def start_chat(self, addr_user1, addr_user2):
        chat = self.__get_valid_chat(addr_user1, addr_user2)

        if not chat:
            self.chats[chat] = Chat(addr_user1, addr_user2)


    def send_message(self, addr_sender, addr_receiver, message):
        chat = self.__get_valid_chat(addr_sender, addr_receiver)

        self.chats[chat].add_message(addr_sender, message)


    def get_chat(self, addr_user1, addr_user2):
        chat = self.__get_valid_chat(addr_user1, addr_user2)

        if not chat:
            return None

        return self.chats[chat]

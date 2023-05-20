

class Conversation:
    def __init__(self, id: str) -> None:
        self.__id = id
        self.__url = f"https://huggingface.co/chat/conversation/{self.__id}"

    def url(self) -> str:
        return self.__url
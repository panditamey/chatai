from json import loads
from requests import Session

from Conversation import Conversation


class HuggingChat:
    def __init__(self) -> None:
        self.__conversation = None
        self.__session = self.__get_session()

    def __get_session(self) -> Session:
        session = Session()

        # Get cookies
        session.get(url="https://huggingface.co/chat/")

        return session

    def newConversation(self) -> Conversation:
        res = self.__session.post(url="https://huggingface.co/chat/conversation")

        assert res.status_code == 200, "Failed to create new conversation"

        return Conversation(res.json()["conversationId"])

    def chat(self, input: str, temperature: float = 0.9, top_p: float = 0.95, repetition_penalty: float = 1.2, top_k: int = 50, truncate: int = 1024, watermark: bool = False, max_new_tokens: int = 1024) -> str:
        if self.__conversation is None:
            self.__conversation = self.newConversation()

        res = self.__session.post(
            url=self.__conversation.url(),
            json={
                "inputs": input,
                "parameters": {
                    "temperature": temperature,
                    "top_p": top_p,
                    "repetition_penalty": repetition_penalty,
                    "top_k": top_k,
                    "truncate": truncate,
                    "watermark": watermark,
                    "max_new_tokens": max_new_tokens,
                    "stop": [
                    "<|endoftext|>"
                    ],
                    "return_full_text": False
                },
                "stream": True,
                "options": {
                    "use_cache": False
                }
            },
            stream=True
        )

        assert res.status_code == 200, "Failed to send message"

        for chunk in res.iter_content(chunk_size=None):
            if chunk:
                try : 
                    data = loads(chunk.decode("utf-8")[5:])
                    if "error" not in data:
                        yield data
                    else:
                        print("error: ", data["error"])
                        break
                except:
                    pass
                
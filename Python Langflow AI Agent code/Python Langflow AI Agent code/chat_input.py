from langflow.schema.message import Message

class ChatInput:
    def __init__(self, input_value: str):
        self.input_value = input_value
        self.sender = "User"
        self.sender_name = "User"
        self.session_id = "session_001"
        self.should_store_message = True
        self.background_color = ""
        self.chat_icon = ""
        self.text_color = ""
        self.files = []

    async def message_response(self) -> Message:
        message = await Message.create(
            text=self.input_value,
            sender=self.sender,
            sender_name=self.sender_name,
            session_id=self.session_id,
            files=self.files,
            properties={
                "background_color": self.background_color,
                "text_color": self.text_color,
                "icon": self.chat_icon,
            },
        )
        if self.session_id and self.should_store_message:
            stored_message = await self.send_message(message)
            return stored_message
        return message

    async def send_message(self, message):
        return message
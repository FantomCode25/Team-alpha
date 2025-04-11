from langflow.schema.message import Message

class GoogleGenerativeAIModel:
    def __init__(self, input_value: str):
        self.input_value = input_value
        self.system_message = ""

    async def text_output(self) -> Message:
        return Message(text=f"Gemini response to: {self.input_value}")
class ChatOutput:
    def __init__(self):
        self.input_value = None

    def receive(self, message):
        self.input_value = message.text
        print(f"Chat Output: {self.input_value}")
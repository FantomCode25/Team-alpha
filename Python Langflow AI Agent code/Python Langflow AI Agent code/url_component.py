from langflow.schema.message import Message

class URLComponent:
    def __init__(self, urls):
        self.urls = urls

    async def component_as_tool(self):
        return f"Tool for {self.urls}"
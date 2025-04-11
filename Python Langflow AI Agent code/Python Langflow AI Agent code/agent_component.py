from langflow.components.helpers import CurrentDateComponent
from langflow.components.helpers.memory import MemoryComponent
from langflow.base.agents.agent import LCToolsAgentComponent
from langflow.schema.message import Message
from langflow.logging import logger

class AgentComponent(LCToolsAgentComponent):
    def __init__(self):
        self.input_value = ""
        self.system_prompt = "You are a helpful assistant."
        self.tools = []
        self.add_current_date_tool = True
        self.chat_history = []

    async def message_response(self) -> Message:
        try:
            if self.add_current_date_tool:
                tool = (await CurrentDateComponent().to_toolkit()).pop(0)
                self.tools.append(tool)
            if not self.tools:
                raise ValueError("Please add at least one tool.")
            agent = self.create_agent_runnable()
            return await self.run_agent(agent)
        except Exception as e:
            logger.error(f"Agent error: {e}")
            raise

    def create_agent_runnable(self):
        return lambda x: f"Processed: {x}"

    async def run_agent(self, agent):
        return Message(text=f"Agent processed: {self.input_value}")
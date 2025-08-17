import os
import sys
# 添加 src 目录到模块搜索路径，以便可以导入 src 目录中的模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from unittest.mock import patch, MagicMock
from agents.agent_base import AgentBase


class VirtualAgent(AgentBase):
    def __init__(self, **kwargs):
        super().__init__(name="virtual", prompt_file="virtual_prompt.txt", intro_file="virtual_intro.json", **kwargs)

class TestAgentBase(unittest.TestCase):
    @patch.object(AgentBase, "load_intro", return_value=["intro"])
    @patch.object(AgentBase, "load_prompt", return_value="system prompt")
    def test_load_prompt(self, mock_prompt, mock_intro):
        agent = VirtualAgent()
        self.assertEqual(agent.prompt, "system prompt")

    @patch.object(AgentBase, "load_intro", return_value=["intro"])
    @patch.object(AgentBase, "load_prompt", return_value="system prompt")
    def test_load_intro(self, mock_prompt, mock_intro):
        agent = VirtualAgent()
        self.assertEqual(agent.intro_messages, ["intro"])

    @patch("agents.agent_base.ChatOllama")
    @patch("agents.agent_base.ChatPromptTemplate.from_messages")
    @patch.object(AgentBase, "load_intro", return_value=["intro"])
    @patch.object(AgentBase, "load_prompt", return_value="system prompt")
    def test_create_chatbot(self, mock_prompt, mock_intro, mock_template, mock_chat):
        agent = VirtualAgent()
        self.assertTrue(hasattr(agent, "chatbot"))
        self.assertTrue(hasattr(agent, "chatbot_with_history"))

    @patch("agents.agent_base.RunnableWithMessageHistory")
    @patch("agents.agent_base.ChatOllama")
    @patch("agents.agent_base.ChatPromptTemplate.from_messages")
    @patch.object(AgentBase, "load_intro", return_value=["intro"])
    @patch.object(AgentBase, "load_prompt", return_value="system prompt")
    def test_chat_with_history(self, mock_prompt, mock_intro, mock_template, mock_chat, mock_runnable):
        mock_instance = MagicMock()
        mock_instance.invoke.return_value.content = "response"
        mock_runnable.return_value = mock_instance
        agent = VirtualAgent()
        result = agent.chat_with_history("详细介绍一下黑洞", session_id="test_agent_base")
        self.assertEqual(result, "response")

if __name__ == "__main__":
    unittest.main() 
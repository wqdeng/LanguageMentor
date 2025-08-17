import os
import sys
# 添加 src 目录到模块搜索路径，以便可以导入 src 目录中的模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from unittest.mock import patch
from agents.conversation_agent import ConversationAgent


class TestConversationAgent(unittest.TestCase):
    @patch("agents.agent_base.AgentBase.load_prompt", return_value="system prompt")
    def test_init(self, mock_prompt):
        agent = ConversationAgent(session_id="test_conversation_agent")
        self.assertEqual(agent.name, "conversation")
        self.assertEqual(agent.session_id, "test_conversation_agent")
        self.assertIn("conversation_prompt.txt", agent.prompt_file)

if __name__ == "__main__":
    unittest.main()
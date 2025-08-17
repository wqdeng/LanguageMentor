import os
import sys
# 添加 src 目录到模块搜索路径, 以便可以导入 src 目录中的模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from unittest.mock import patch, MagicMock
from agents.vocab_agent import VocabAgent


class TestVocabAgent(unittest.TestCase):
    @patch("agents.agent_base.AgentBase.load_prompt", return_value="system prompt")
    def test_init(self, mock_prompt):
        agent = VocabAgent(session_id="test-vocab-agent")
        self.assertEqual(agent.name, "vocab_study")
        self.assertEqual(agent.prompt, "system prompt")
        self.assertEqual(agent.session_id, "test-vocab-agent")

    @patch("agents.vocab_agent.get_session_history")
    @patch("agents.agent_base.AgentBase.load_prompt", return_value="system prompt")
    def test_restart_session(self, mock_prompt, mock_history):
        agent = VocabAgent(session_id="test-vocab-agent")
        mock_history.return_value.clear = MagicMock()
        mock_history.return_value.__str__ = lambda s: "history_obj"
        result = agent.restart_session(session_id="test-vocab-agent")
        self.assertEqual(result, mock_history.return_value)
        mock_history.return_value.clear.assert_called_once()

if __name__ == "__main__":
    unittest.main()
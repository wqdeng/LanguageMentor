import os
import sys
# 添加 src 目录到模块搜索路径，以便可以导入 src 目录中的模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from unittest.mock import patch, MagicMock
from agents.scenario_agent import ScenarioAgent


class TestScenarioAgent(unittest.TestCase):
    @patch("agents.agent_base.AgentBase.load_prompt", return_value="system prompt")
    @patch("agents.agent_base.AgentBase.load_intro", return_value=["intro-1", "intro-2"])
    def test_init(self, mock_intro, mock_prompt):
        agent = ScenarioAgent("hotel-checkin", session_id="test_scenario_agent")
        self.assertEqual(agent.name, "hotel-checkin")
        self.assertEqual(agent.session_id, "test_scenario_agent")
        self.assertEqual(agent.intro_messages, ["intro-1", "intro-2"])

    @patch("agents.scenario_agent.get_session_history")
    @patch("agents.agent_base.AgentBase.load_prompt", return_value="system prompt")
    @patch("agents.agent_base.AgentBase.load_intro", return_value=["intro-1", "intro-2"])
    def test_start_new_session(self, mock_intro, mock_prompt, mock_history):
        agent = ScenarioAgent("hotel-checkin", session_id="test_scenario_agent")
        # 没有历史消息场景
        mock_history.return_value.messages = []
        mock_history.return_value.add_message = MagicMock()
        message = agent.start_new_session(session_id="test_scenario_agent")
        self.assertIn(message, ["intro-1", "intro-2"])
        # 有历史消息场景
        mock_history.return_value.messages = [MagicMock(content="The last Message.")]
        message2 = agent.start_new_session(session_id="test_scenario_agent")
        self.assertEqual(message2, "The last Message.")

if __name__ == "__main__":
    unittest.main()
import os
import sys
# 添加 src 目录到模块搜索路径, 以便可以导入 src 目录中的模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from agents import session_history


class TestSessionHistory(unittest.TestCase):
    def test_get_session_history(self):
        session_id = "test-session-history"
        draft_session_history = session_history.get_session_history(session_id)
        self.assertIsNotNone(draft_session_history)

        draft_session_history2 = session_history.get_session_history(session_id)
        self.assertIs(draft_session_history, draft_session_history2)

        session_id2 = "test-session-history2"
        draft_session_history3 = session_history.get_session_history(session_id2)
        self.assertIsNot(draft_session_history, draft_session_history3)

if __name__ == "__main__":
    unittest.main()
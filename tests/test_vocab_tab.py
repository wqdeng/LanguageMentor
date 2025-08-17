import os
import sys
# 添加 src 目录到模块搜索路径，以便可以导入 src 目录中的模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from unittest.mock import patch, mock_open, MagicMock
from tabs.vocab_tab import get_page_desc, base_path, handle_vocab


class TestVocabTab(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="This is a test.")
    def test_file_found(self, mock_file):
        # 测试文件存在时的情况
        result = get_page_desc("test_feature")
        self.assertEqual(result, "This is a test.")
        mock_file.assert_called_once_with(f"{base_path}content/page/test_feature.md", "r", encoding="utf-8")

    @patch("builtins.open", side_effect=FileNotFoundError)
    @patch("utils.logger.LOG.error")
    def test_file_not_found(self, mock_log_error, mock_file):
        # 测试文件不存在时的情况
        result = get_page_desc("missing_feature")
        self.assertEqual(result, "词汇学习介绍文件未找到。")
        mock_log_error.assert_called_once_with("词汇学习介绍文件 content/page/missing_feature.md 未找到！")

    @patch("agents.vocab_agent.VocabAgent.chat_with_history", return_value="This is a response.")
    @patch("utils.logger.LOG")
    def test_handle_vocab(self, mock_log, mock_vocab_agent):
        # 调用被测试方法
        user_input = "Hello!"
        chat_history = []  # 假设 chat_history 不影响当前逻辑
        result = handle_vocab(user_input, chat_history)

        # 验证返回值
        expected_result = {"role": "assistant", "content": "This is a response."}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

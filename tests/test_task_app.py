import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import task_app


class TestTaskApp(unittest.TestCase):

    def test_validate_priority(self):
        self.assertEqual(task_app.validate_priority("high"), "high")
        with self.assertRaises(ValueError):
            task_app.validate_priority("urgent")


if __name__ == "__main__":
    unittest.main()
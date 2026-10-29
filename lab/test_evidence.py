import unittest

import lab


class Speculation(unittest.TestCase):
    def test_reads_args_and_env(self):
        launch = {"args": ["--host", "0.0.0.0", "--speculative-algorithm", "NEXTN"],
                  "env": {"PORT": "8000", "DSPARK_TOKENS": "5"}}
        self.assertEqual(lab.speculation(launch), ["--speculative-algorithm", "NEXTN", "DSPARK_TOKENS=5"])

    def test_none_when_the_launch_does_not_speculate(self):
        self.assertIsNone(lab.speculation({"args": ["--model", "/models/x"], "env": {"PORT": "8000"}}))

    def test_null_args(self):
        self.assertIsNone(lab.speculation({"args": None}))

    def test_a_config_value_is_not_counted_twice(self):
        launch = {"args": ["--speculative-config", '{"method": "dspark", "num_speculative_tokens": 5}']}
        self.assertEqual(lab.speculation(launch),
                         ["--speculative-config", '{"method": "dspark", "num_speculative_tokens": 5}'])


if __name__ == "__main__":
    unittest.main()

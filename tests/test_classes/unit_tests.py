import unittest
from ... import policy
import tests.data.unit_test_cases as unit_test_cases

class UnitTest(unittest.TestCase):
    def test_exception(self, exception: Exception, message: str, json_data: str):
        with self.assertRaises(exception) as context:
            self.policy = policy.Policy(json_data)
        self.assertEqual(str(context.exception), message)
    
    def test_invalid_json(self):
        self.test_exception(ValueError, "Invalid input JSON, please check the JSON format.",  unit_test_cases.invalid_json)

if __name__ == "__main__":
    unittest.main()
import unittest

import test.data.unit_test_cases as tests
from src.aws_policy.policy import Policy


class UnitTest(unittest.TestCase):
    def test_invalid_json(self):
        with self.assertRaises(SyntaxError) as context:
            Policy(tests.invalid_json)
        self.assertEqual(context.exception.msg, 'Invalid input JSON, please check the JSON format.')

    def test_policy_name_missing(self):
        with self.assertRaises(KeyError) as context:
            Policy(tests.policy_name_missing)
        self.assertEqual(context.exception.args[0],
                         "Invalid input JSON key, check the JSON structure. Keys 'PolicyName' and 'PolicyDocument' are required.")

    def test_policy_document_missing(self):
        with self.assertRaises(KeyError) as context:
            Policy(tests.policy_document_missing)
        self.assertEqual(context.exception.args[0],
                         "Invalid input JSON key, check the JSON structure. Keys 'PolicyName' and 'PolicyDocument' are required.")

    def test_policy_unwanted_keys(self):
        with self.assertRaises(KeyError) as context:
            Policy(tests.policy_unwanted_keys)
        self.assertEqual(context.exception.args[0],
                         "Invalid input JSON key, check the JSON structure. Keys 'PolicyName' and 'PolicyDocument' are required.")

    def test_policy_name_invalid_type(self):
        with self.assertRaises(ValueError) as context:
            Policy(tests.policy_name_invalid_type)
        self.assertEqual(context.exception.args[0], "PolicyName must be a string")

    def test_policy_name_too_short(self):
        with self.assertRaises(ValueError) as context:
            Policy(tests.policy_name_too_short)
        self.assertEqual(context.exception.args[0], "PolicyName must be between 1 and 128 characters")

    def test_policy_name_too_long(self):
        with self.assertRaises(ValueError) as context:
            Policy(tests.policy_name_too_long)
        self.assertEqual(context.exception.args[0], "PolicyName must be between 1 and 128 characters")

    def test_name_invalid_name(self):
        with self.assertRaises(ValueError) as context:
            Policy(tests.policy_name_invalid_name)
        self.assertEqual(context.exception.args[0], "PolicyName must be alphanumeric")

    def test_policy_document_invalid_type(self):
        with self.assertRaises(ValueError) as context:
            Policy(tests.policy_document_invalid_type)
        self.assertEqual(context.exception.args[0], "PolicyDocument must be a dictionary")

    def test_policy_document_missing_statement(self):
        with self.assertRaises(KeyError) as context:
            Policy(tests.policy_document_missing_statement)
        self.assertEqual(context.exception.args[0], """Invalid PolisyDocument inside JSON, check the JSON structure. Keys "Version" and "Statement" 
            are required.""")

    def test_policy_document_missing_version(self):
        with self.assertRaises(KeyError) as context:
            Policy(tests.policy_document_missing_version)
        self.assertEqual(context.exception.args[0], """Invalid PolisyDocument inside JSON, check the JSON structure. Keys "Version" and "Statement" 
            are required.""")

    def test_policy_document_statement_invalid_type(self):
        with self.assertRaises(ValueError) as context:
            Policy(tests.policy_document_statement_invalid_type)
        self.assertEqual(context.exception.args[0], "Statement in PolicyDocument must be a list")

    def test_policy_document_statement_content_invalid_type(self):
        with self.assertRaises(ValueError) as context:
            Policy(tests.policy_document_statement_content_invalid_type)
        self.assertEqual(context.exception.args[0], "Each statement must be a dictionary")

    def test_resource_is_asterisk(self):
        policy = Policy(tests.policy_resource_is_asterisk)
        self.assertFalse(policy.verify_resource_data())

    def test_resource_is_not_asterisk(self):
        policy = Policy(tests.policy_resource_is_not_asterisk)
        self.assertTrue(policy.verify_resource_data())


if __name__ == "__main__":
    unittest.main()

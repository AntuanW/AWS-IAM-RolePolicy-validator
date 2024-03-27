invalid_json = """{"PolicyName": 123, "PolicyDocument": {"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Action": "*"}]}""" # Invalid JSON

policy_name_missing = """{"PolicyDocument": {"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Action": "*"}]}}"""  # PolicyName missing

policy_document_missing = """{"PolicyName": "test"}"""  # PolicyDocument missing

policy_unwanted_keys = """{"PolicyName": "test", "PolicyDocument": {"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Action": "*", "Resource": "*"}]}, "UnwantedKey": "UnwantedValue"}"""  # Unwanted keys

policy_name_invalid_type = """{"PolicyName": 123, "PolicyDocument": {"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Action": "*"}]}}"""# PolicyName not a string

policy_name_too_short = """{"PolicyName": "", "PolicyDocument": {"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Action": "*"}]}}"""# PolicyName not a string

too_long_name = "a" * 129
policy_name_too_long = f'''{{"PolicyName": "{too_long_name}", "PolicyDocument": {{"Version": "2012-10-17", "Statement": [{{"Effect": "Allow", "Action": "*"}}]}}}}'''  # PolicyName too long

policy_name_invalid_name = """{"PolicyName": "invalid_policy_name_@#", "PolicyDocument": {"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Action": "*"}]}}"""  # Invalid PolicyName

policy_document_invalid_type = """{"PolicyName": "test", "PolicyDocument": ["Version", "2012-10-17", "Statement", "invalid"]}"""  # PolicyDocument not a dictionary

policy_document_missing_statement = """{"PolicyName": "test", "PolicyDocument": {"Version": "2012-10-17"}}"""  # Statement missing in PolicyDocument

policy_document_missing_version = """{"PolicyName": "test", "PolicyDocument": {"Statement": [{"Effect": "Allow", "Action": "*"}]}}"""  # Version missing in PolicyDocument

policy_document_statement_invalid_type = """{"PolicyName": "test", "PolicyDocument": {"Version": "2012-10-17", "Statement": "invalid"}}"""  # Statement not a list

policy_document_statement_content_invalid_type = """{"PolicyName": "test", "PolicyDocument": {"Version": "2012-10-17", "Statement": ["invalid"]}}"""  # Statement content not a dictionary

policy_resource_is_asterix = """{"PolicyName": "test", "PolicyDocument": {"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Action": "*", "Resource": "*"}]}}"""  # Resource is *

policy_resource_is_not_asterix = """{"PolicyName": "test", "PolicyDocument": {"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Action": "*", "Resource": "arn:aws:s3:::my_corporate_bucket/*"}]}}"""  # Resource is not *
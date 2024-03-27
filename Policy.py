import json
import re


class Policy:
    def __init__(self, data: str | bytes | bytearray) -> None:
        try:
            aws_iam_role_policy = json.loads(data)
        except json.JSONDecodeError:
            raise SyntaxError("Invalid input JSON, please check the JSON format.")

        self.__validate_json(aws_iam_role_policy)

        self.policy_name: str = aws_iam_role_policy["PolicyName"]
        self.policy_document: dict = aws_iam_role_policy["PolicyDocument"]

    def __validate_json(self, json_object: dict) -> None:
        def validate_policy_name(policy_name) -> None:
            if not isinstance(json_object["PolicyName"], str):
                raise ValueError("PolicyName must be a string")
            if not (1 <= len(policy_name) <= 128):
                raise ValueError("PolicyName must be between 1 and 128 characters")
            if not re.fullmatch(r"[\w+=,.@-]+", policy_name):
                raise ValueError("PolicyName must be alphanumeric")

        def validate_policy_document(policy_document) -> None:
            if not isinstance(policy_document, dict):
                raise ValueError("PolicyDocument must be a dictionary")
            if "Version" not in policy_document or "Statement" not in policy_document:
                raise KeyError(
                    """Invalid PolisyDocument inside JSON, check the JSON structure. Keys "Version" and "Statement" are required."""
                )
            if not isinstance(policy_document["Statement"], list):
                raise ValueError("Statement in PolicyDocument must be a list")

            for statement in policy_document["Statement"]:
                if not isinstance(statement, dict):
                    raise ValueError("Each statement must be a dictionary")

        if json_object.keys() != {"PolicyName", "PolicyDocument"}:
            raise KeyError(
                "Invalid input JSON key, check the JSON structure. Keys 'PolicyName' and 'PolicyDocument' are required."
            )

        validate_policy_name(json_object["PolicyName"])
        validate_policy_document(json_object["PolicyDocument"])

    def verify_resource_data(self) -> bool:
        for statement in self.policy_document["Statement"]:
            # Verify that the policy document contains the required resource key
            if "Resource" in statement:
                # check if the resource field contains a single *
                if statement["Resource"] == "*":
                    return False
        return True

    def __str__(self) -> str:
        return json.dumps(self.__dict__, indent=2)


if __name__ == "__main__":
    data = open("ex_json.json").read()
    try:
        policy = Policy(data)
        print(policy)
    except Exception as e:
        print(e)
    pass

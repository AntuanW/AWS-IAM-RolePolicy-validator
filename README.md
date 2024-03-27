# AWS-IAM-RolePolicy-validator
Little Python script to verify AWS::IAM::Role Policy JSON

## Requirements
- Python installed on your system (tested with Python 3.12.2)

## How to run 
1. Check if Python is installed by running `python -V` command.
2. If so, create virtual environment or use global environment.
3. Run `validator.py` script with file name or path to JSON you want check with command:
    ```bash
    python validator.py <json_file/path>
    ```

## AWS::IAM::Role Policy JSON specification

### Syntax
```JSON
{
  "PolicyDocument" : Json,
  "PolicyName" : String
}
```

### Properties

#### PolicyDocument
```
Required: Yes
Type: JSON
```

#### PolicyName
```
Required: Yes
Type: String
Pattern: [\w+=,.@-]+
Minimum: 1
Maximum: 128
```

#### Example of correct AWS::IAM::Role Policy JSON
```JSON
{
    "PolicyName": "root",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": [
                    "iam:ListRoles",
                    "iam:ListUsers"
                ],
                "Resource": "*"
            }
        ]
    }
}
```
[Link for further documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-role-policy.html)

### Self-Assessment
- [x] Method veryfying the input JSON data <br>
- [x] Readme includes "how to run" instructions <br>
- [x] Input data format is defined as AWS::IAM::Role Policy <br>
- [x] Unit tests<br>
- [x] Covering edge cases<br>

### Author
[Antoni Wójcik](https://github.com/AntuanW)
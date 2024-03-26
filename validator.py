import sys
from Policy import Policy

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Wrong usage, correct command: python validator.py <json_file>")
        exit(1)
    try:
        with open(sys.argv[1], "r") as file:
            data = file.read()
            policy = Policy(data)
            print(policy.verify_resource_data())
    except FileNotFoundError:
        print("File not found")
        exit(1)
    except SyntaxError as e:
        print(e)
        exit(1)
    except ValueError as e:
        print(e)
        exit(1)
    except KeyError as e:
        print(e)
        exit(1)
    except Exception as e:
        print(e)
        exit(1)
    
    exit(0)
    
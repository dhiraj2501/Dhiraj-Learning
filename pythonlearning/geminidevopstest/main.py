
import json

def get_user_input():
    stack_name = input("Enter the stack name: ")
    master_count = int(input("Enter the number of master nodes: "))
    master_instance_type = input("Enter the master node instance type: ")
    service_count = int(input("Enter the number of service nodes: "))
    service_instance_type = input("Enter the service node instance type: ")
    aws_region = input("Enter the AWS region: ")

    config = {
        "stack_name": stack_name,
        "region": aws_region,
        "master_nodes": {
            "count": master_count,
            "instance_type": master_instance_type
        },
        "service_nodes": {
            "count": service_count,
            "instance_type": service_instance_type
        }
    }

    return config

def save_config_to_json(config):
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

if __name__ == "__main__":
    config = get_user_input()
    save_config_to_json(config)
    print("Configuration saved to config.json")

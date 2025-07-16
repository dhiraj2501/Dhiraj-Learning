
provider "aws" {
  region = local.config.region
}

locals {
  config = jsondecode(file("${path.module}/config.json"))
}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = local.config.stack_name
  }
}

resource "aws_subnet" "main" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "${local.config.stack_name}-subnet"
  }
}

resource "aws_instance" "master" {
  count         = local.config.master_nodes.count
  ami           = "ami-0c55b159cbfafe1f0" # Ubuntu 20.04 LTS
  instance_type = local.config.master_nodes.instance_type
  subnet_id     = aws_subnet.main.id

  tags = {
    Name = "${local.config.stack_name}-master-${count.index}"
    Role = "master"
  }
}

resource "aws_instance" "service" {
  count         = local.config.service_nodes.count
  ami           = "ami-0c55b159cbfafe1f0" # Ubuntu 20.04 LTS
  instance_type = local.config.service_nodes.instance_type
  subnet_id     = aws_subnet.main.id

  tags = {
    Name = "${local.config.stack_name}-service-${count.index}"
    Role = "service"
  }
}

output "master_public_ips" {
  value = aws_instance.master[*].public_ip
}

output "service_public_ips" {
  value = aws_instance.service[*].public_ip
}

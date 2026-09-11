resource "aws_instance" "Myapp" {
  ami             = "ami-01a00762f46d584a1"
  instance_type   = "t3.small"
  key_name        = "devops-project"
  security_groups = [aws_security_group.my_sg.name]

  tags = {
    Name = "Myproject_app"
  }
}
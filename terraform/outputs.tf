output "public_ip" {
  description = "Public IP of the created server"
  value       = aws_instance.Myapp.public_ip
}
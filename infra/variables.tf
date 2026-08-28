variable "aws_region" {
  description = "AWS region to deploy into"
  type        = string
  default     = "ap-south-1"            # ← change to your region
}

variable "app_name" {
  description = "Name used across all resources"
  type        = string
  default     = "fastapi-app"
}

variable "dockerhub_image" {
  description = "Full DockerHub image with tag"
  type        = string
  # example: "johndoe/mydockerexp:latest"
}

variable "container_port" {
  description = "Port your FastAPI app listens on"
  type        = number
  default     = 8000
}
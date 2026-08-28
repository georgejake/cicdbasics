terraform {
  # HCP Terraform backend — stores your state safely
  cloud {
    organization = "your-org-name"       # ← replace with your HCP org name

    workspaces {
      name = "fastapi-ecs"               # ← replace with your HCP workspace name
    }
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

terraform {
  backend "s3" {
    bucket = "aswinkgs-flask-tfstate"
    key    = "flask-app/terraform.tfstate"
    region = "ap-south-1"
  }
}
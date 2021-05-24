terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }
}

provider "aws" {
  profile = "default"
  region  = "us-gov-east-1"
}

provider "aws" {
  alias  = "west"
  region = "us-gov-west-1"
}

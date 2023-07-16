terraform {
  backend "s3" {
    bucket = "terraform-state-flaskbb-hzarkoob"
    key    = "core/terraform.tfstate"
    region = "us-west-1"
  }
}
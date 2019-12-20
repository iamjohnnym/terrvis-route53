# Sample, change the env vars to the real deal and `terraform apply`
terraform {
  backend "s3" {
    bucket = "terrvis-${ENVIRONMENT_NAME}-${AWS_ACCOUNT_ID}"
    key = "${ENVIRONMENT_NAME}/terrvis-domains/domains.tfstate"
    region = "us-west-2"
    dynamodb_table = "terrvis-tfstate-lock-development"
    encrypt = "true"
  }
}

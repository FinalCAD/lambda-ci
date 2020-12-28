terraform {
    source = "../../../modules//circleci_lambda/" 
}
include {
  path = "${find_in_parent_folders()}"
}

inputs = {
  owner             = "Infra Team"
  application_id    = "hello-world"
  path_to_secret    = "test/eks"
  s3_bucket         = "finalcad-test"   
}

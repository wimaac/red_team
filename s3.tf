resource "aws_kms_key" "red_team_kms" {
  description             = "KMS key for red team s3 files"
  deletion_window_in_days = 7
}

resource "aws_s3_bucket" "red-Final" {
  bucket = "red-final-bucket"
  acl    = "private"
}

resource "aws_s3_bucket_object" "red-Final_object" {
  key        = "data.csv"
  bucket     = aws_s3_bucket.red-Final.id
  source     = "./files/data.csv"
  kms_key_id = aws_kms_key.red_team_kms.arn
}

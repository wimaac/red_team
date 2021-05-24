data "archive_file" "zipup" {
  type        = "zip"
  source_file = "./files/lambda_function.py"
  output_path = "./files/lambda.zip"
}

resource "aws_lambda_function" "final_lambda" {
  provider = aws.west
  filename      = "./files/lambda.zip"
  function_name = "red-team-final"
  role          = "arn:aws-us-gov:iam::812677824406:role/red-lambda-final"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.7"
  source_code_hash = data.archive_file.zipup.output_base64sha256
  publish       = "true"
  environment {
    variables = {
      app_id = aws_pinpoint_app.red_team_terraform_final.application_id
    }
  }
}
data "aws_lambda_invocation" "example" {
  provider = aws.west
  function_name = aws_lambda_function.final_lambda.function_name

  input = <<JSON
{
  "key1": "value1",
  "key2": "value2"
}
JSON
}

output "result_entry" {
  value = jsondecode(data.aws_lambda_invocation.example.result)
}

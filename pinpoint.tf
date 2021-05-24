resource "aws_pinpoint_app" "red_team_terraform_final" {
  provider = aws.west
  name = "red_team_terraform_final"

  limits {
    maximum_duration = 600
    messages_per_second = 50
  }

  quiet_time {
    start = "00:00"
    end   = "06:00"
  }
}
resource "aws_pinpoint_email_channel" "email" {
  provider = aws.west
  application_id = aws_pinpoint_app.red_team_terraform_final.application_id
  from_address   = "michael.jiang@accenturefederal.com"
  identity       = "arn:aws-us-gov:ses:us-gov-west-1:812677824406:identity/michael.jiang@accenturefederal.com"
  role_arn       = aws_iam_role.role.arn
}

resource "aws_iam_role" "role" {
  provider = aws.west
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "pinpoint.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_role_policy" "role_policy" {
  provider = aws.west
  name = "role_policy"
  role = aws_iam_role.role.id

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": {
    "Action": [
      "mobileanalytics:PutEvents",
      "mobileanalytics:PutItems"
    ],
    "Effect": "Allow",
    "Resource": [
      "*"
    ]
  }
}
EOF
}

import json
import boto3
from botocore.exceptions import ClientError
import os
def lambda_handler(event, context):
    AWS_REGION = "us-gov-west-1"
    SENDER = "Michael Jiang <michael.jiang@accenturefederal.com>"
    TOADDRESS = ["marc.broughton@accenturefederal.com", "christina.mueller@accenturefederal.com", "michael.jiang@accenturefederal.com", "grace.e.hickey@accenturefederal.com", "Lauren.white@accenturefederal.com", "antonino.ardizzone@accenturefederal.com"]
    APPID = os.environ.get('app_id')
    SUBJECT = "Automation is pretty cool!"
    BODY_TEXT = """Red Team Demo Example Email
    -------------------------------------
    This email was sent via a serverless architecture that the Red team developed. How cool is that? Details of the project can be found here: https://github.com/wimaac/red_team/tree/master
                """
    BODY_HTML = """
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html data-editor-version="2" class="sg-campaigns" xmlns="http://www.w3.org/1999/xhtml">
    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1">
      <!--[if !mso]><!-->
      <meta http-equiv="X-UA-Compatible" content="IE=Edge">
      <!--<![endif]-->
      <!--[if (gte mso 9)|(IE)]>
      <xml>
        <o:OfficeDocumentSettings>
          <o:AllowPNG/>
          <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
      </xml>
      <![endif]-->
      <!--[if (gte mso 9)|(IE)]>
  <style type="text/css">
    body {width: 600px;margin: 0 auto;}
    table {border-collapse: collapse;}
    table, td {mso-table-lspace: 0pt;mso-table-rspace: 0pt;}
    img {-ms-interpolation-mode: bicubic;}
  </style>
<![endif]-->
      <style type="text/css">
    body, p, div {
      font-family: comic sans ms,cursive;
      font-size: 14px;
    }
    body {
      color: #000000;
    }
    body a {
      color: #1188E6;
      text-decoration: none;
    }
    p { margin: 0; padding: 0; }
    table.wrapper {
      width:100% !important;
      table-layout: fixed;
      -webkit-font-smoothing: antialiased;
      -webkit-text-size-adjust: 100%;
      -moz-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
    }
    img.max-width {
      max-width: 100% !important;
    }
    .column.of-2 {
      width: 50%;
    }
    .column.of-3 {
      width: 33.333%;
    }
    .column.of-4 {
      width: 25%;
    }
    ul ul ul ul  {
      list-style-type: disc !important;
    }
    ol ol {
      list-style-type: lower-roman !important;
    }
    ol ol ol {
      list-style-type: lower-latin !important;
    }
    ol ol ol ol {
      list-style-type: decimal !important;
    }
    @media screen and (max-width:480px) {
      .preheader .rightColumnContent,
      .footer .rightColumnContent {
        text-align: left !important;
      }
      .preheader .rightColumnContent div,
      .preheader .rightColumnContent span,
      .footer .rightColumnContent div,
      .footer .rightColumnContent span {
        text-align: left !important;
      }
      .preheader .rightColumnContent,
      .preheader .leftColumnContent {
        font-size: 80% !important;
        padding: 5px 0;
      }
      table.wrapper-mobile {
        width: 100% !important;
        table-layout: fixed;
      }
      img.max-width {
        height: auto !important;
        max-width: 100% !important;
      }
      a.bulletproof-button {
        display: block !important;
        width: auto !important;
        font-size: 80%;
        padding-left: 0 !important;
        padding-right: 0 !important;
      }
      .columns {
        width: 100% !important;
      }
      .column {
        display: block !important;
        width: 100% !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
      }
      .social-icon-column {
        display: inline-block !important;
      }
    }
  </style>
      <!--user entered Head Start--><!--End Head user entered-->
    </head>
    <body>
      <center class="wrapper" data-link-color="#1188E6" data-body-style="font-size:14px; font-family:comic sans ms,cursive; color:#000000; background-color:#FFFFFF;">
        <div class="webkit">
          <table cellpadding="0" cellspacing="0" border="0" width="100%" class="wrapper" bgcolor="#FFFFFF">
            <tr>
              <td valign="top" bgcolor="#FFFFFF" width="100%">
                <table width="100%" role="content-container" class="outer" align="center" cellpadding="0" cellspacing="0" border="0">
                  <tr>
                    <td width="100%">
                      <table width="100%" cellpadding="0" cellspacing="0" border="0">
                        <tr>
                          <td>
                            <!--[if mso]>
    <center>
    <table><tr><td width="600">
  <![endif]-->
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="width:100%; max-width:600px;" align="center">
                                      <tr>
                                        <td role="modules-container" style="padding:0px 0px 0px 0px; color:#000000; text-align:left;" bgcolor="#FFFFFF" width="100%" align="left"><table class="module preheader preheader-hide" role="module" data-type="preheader" border="0" cellpadding="0" cellspacing="0" width="100%" style="display: none !important; mso-hide: all; visibility: hidden; opacity: 0; color: transparent; height: 0; width: 0;">
    <tr>
      <td role="module-content">
        <p></p>
      </td>
    </tr>
  </table><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="6d04666d-f9ac-4795-a96f-aa98a0aebc14">
    <tbody>
      <tr>
        <td style="padding:18px 0px 18px 0px; line-height:40px; text-align:inherit; background-color:#180d2f;" height="100%" valign="top" bgcolor="#180d2f" role="module-content"><div><h1 style="text-align: center"><span style="font-family: arial black, helvetica, sans-serif; color: #ff0000; font-size: 36px">Red Team Takes The Stage</span></h1><div></div></div></td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="d208a727-2774-4f33-aa5a-58f15951dda9">
    <tbody>
      <tr>
        <td style="padding:18px 0px 18px 0px; line-height:22px; text-align:inherit;" height="100%" valign="top" bgcolor="" role="module-content"><div><div style="font-family: inherit">The red team have worked together over the last few months to make this happen. You are receiving this email from a one command process. While utilizing Terraform and AWS technology we were able to spin up multiple AWS modules and fire off an email. From the start of the build we had the customer in mind.&nbsp;</div>
<div style="font-family: inherit"><br></div>
<div style="font-family: inherit">The solution presented today is a low cost build that allows you to use one command to remove all the modules that we were able to deploy in the previous step. This will allow for only a small cost during the few seconds it runs instead of have a constant cost of modular uptime.&nbsp;</div><div></div></div></td>
      </tr>
    </tbody>
  </table><table class="module" role="module" data-type="divider" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="3e6b3588-7a79-4918-afd6-b09f1c552b97">
    <tbody>
      <tr>
        <td style="padding:0px 0px 0px 0px;" role="module-content" height="100%" valign="top" bgcolor="">
          <table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" height="10px" style="line-height:10px; font-size:10px;">
            <tbody>
              <tr>
                <td style="padding:0px 0px 10px 0px;" bgcolor="#7100ff"></td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table><table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" role="module" data-type="columns" style="padding:0px 0px 0px 0px;" bgcolor="#FFFFFF" data-distribution="1,1">
    <tbody>
      <tr role="module-content">
        <td height="100%" valign="top"><table width="290" style="width:290px; border-spacing:0; border-collapse:collapse; margin:0px 10px 0px 0px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="" class="column column-0">
      <tbody>
        <tr>
          <td style="padding:0px;margin:0px;border-spacing:0;"><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="490eb94e-72b6-4efe-8224-9ae76a31552e">
    <tbody>
      <tr>
        <td style="padding:18px 0px 18px 0px; line-height:22px; text-align:inherit;" height="100%" valign="top" bgcolor="" role="module-content"><div><ul>
  <li style="">EC2</li>
  <li style="">LAMBDA</li>
  <li style="">PINPOINT</li>
  <li style="">S3 BUCKET</li>
  <li style="">TERRAFORM</li>
</ul><div></div></div></td>
      </tr>
    </tbody>
  </table></td>
        </tr>
      </tbody>
    </table><table width="290" style="width:290px; border-spacing:0; border-collapse:collapse; margin:0px 0px 0px 10px;" cellpadding="0" cellspacing="0" align="left" border="0" bgcolor="" class="column column-1">
      <tbody>
        <tr>
          <td style="padding:0px;margin:0px;border-spacing:0;"><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-muid="22e5d39b-c54e-4782-a7ae-d1236f08f572">
    <tbody>
      <tr>
        <td style="padding:18px 0px 18px 0px; line-height:22px; text-align:inherit;" height="100%" valign="top" bgcolor="" role="module-content"><div><ul>
  <li style="">Repeatable</li>
  <li style="">Cost effect</li>
  <li style="">Rapid deployment</li>
  <li style="">Customizable</li>
</ul><div></div></div></td>
      </tr>
    </tbody>
  </table></td>
        </tr>
      </tbody>
    </table></td>
      </tr>
    </tbody>
  </table></td>
                                      </tr>
                                    </table>
                                    <!--[if mso]>
                                  </td>
                                </tr>
                              </table>
                            </center>
                            <![endif]-->
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </div>
      </center>
    </body>
  </html>

    """

    CHARSET = "UTF-8"
    client = boto3.client('pinpoint',region_name=AWS_REGION)
    for x in TOADDRESS:
        try:
            response = client.send_messages(
                ApplicationId=APPID,
                MessageRequest={
                    'Addresses': {
                        x: {
                             'ChannelType': 'EMAIL'
                        }
                    },
                    'MessageConfiguration': {
                        'EmailMessage': {
                            'FromAddress': SENDER,
                            'SimpleEmail': {
                                'Subject': {
                                    'Charset': CHARSET,
                                    'Data': SUBJECT
                                },
                                'HtmlPart': {
                                    'Charset': CHARSET,
                                    'Data': BODY_HTML
                                },
                                'TextPart': {
                                    'Charset': CHARSET,
                                    'Data': BODY_TEXT
                                }
                            }
                        }
                    }
                }
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Message sent! Message ID: "
                    + response['MessageResponse']['Result'][x]['MessageId'])
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }


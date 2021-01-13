data reponsible person


vpc:vpce-0455537c63632cc3f
resource policy:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Principal": "*",
            "Action": "execute-api:Invoke",
            "Resource": "arn:aws:execute-api:eu-central-1:582985587312:z1mquff4le/*",
            "Condition": {
                "StringNotEquals": {
                    "aws:sourceVpce": "vpce-09d8cd118c8bc53d9"
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "execute-api:Invoke",
            "Resource": "arn:aws:execute-api:eu-central-1:582985587312:z1mquff4le/*"
        }
    ]
}
# postman team
https://app.getpostman.com/join-team?invite_code=c5bed87d230d8705bec01d6c79e13574


api id: e9pe6r1brj

from email_validator import validate_email, EmailNotValidError


email = "peter.o'toole@canary.com"

try:
    valid_email = validate_email(email)
    email = valid_email.email
    print(email)
    print(valid_email.ascii_email)
except EmailNotValidError as e:
    print(str(e))

identity = {
    "attributes": {
        "externalId": "puppers",
        "email": email
    }
}

requests

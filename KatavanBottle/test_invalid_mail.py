import unittest
from myform_mail import validate_email

class TestInvalidEmails(unittest.TestCase):
    
    def test_invalid_email_formats(self):
        invalid_emails = [
            "",
"plainaddress",
"@missingusername.com",
"username@.com",
".username@domain.com",
"username@domain..com",
"username@domain.com.",
"username@domain_com",
"username@domain.c",
"user@name@domain.com",
"username@domain.com-",
"user name@domain.com",
"user..name@domain.com",
"username@domain",
"username@domain..com",
"username@-domain.com",
"username@domain.c0m",
"username@domain.c_m",
"username@domain.123",
"username@domain.c",
"username@domain.con",
"username@.domain.com",
"user@domain..com",
"user@.com",
"user@domain..com",
"user@-domain.com",
"user@domain.-com",
"user@domain_com",
"user@domain.c0m",
"user@domain.c*m",
"user@domain.1com",
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(
                    validate_email(email),
                    f"The email '{email}' was expected to be invalid"
                )

if __name__ == '__main__':
    unittest.main()


PROXY_MAIL = "set your email name"
PASSWORD = "google account password - not gmail password."
"""
 Note: You will need to setup an application-specific password:
            https://support.google.com/mail/?p=InvalidSecondFactor
            https://security.google.com/settings/security/apppasswords

"""

import gmail


class MailService:
    def __init__(self, mail_account=PROXY_MAIL, mail_password=MAIL_PASSWORD):
        self._api = gmail.GMail(mail_account, mail_password)

    def send_email(self, recipient, subject, content):
        """
        Send an email to recipient. Returns empty action result with status.
        :param recipient: recipient email address (str)
        :param subject: subject of an email (str)
        :param content: content of an email (str)
        :return:
        """
        assert (isinstance(recipient, str) and isinstance(subject, str) and isinstance(content, str))
        #TODO:add some regex validator for [to] email address
        print("Calling send_email with params [subject = {}, recipient = {}, content = {}]".\
                     format(subject, recipient, content))
        new_message = gmail.Message(subject, to=recipient, text=content)
        status_code = self._api.send(new_message)
        status = "success" if status_code is None else "fail"
        print("Email sending finished with status = {}".format(status))

        #mostly, errors are caused by smtp

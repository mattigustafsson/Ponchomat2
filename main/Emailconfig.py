""" Module for sending email to a pre set account. """

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(subject, medd):
    """Module for sending a automatic e-mail
    Args:
        subject: String for the subject of the email
        medd: String for the content of the email.
    """

    from_addr = "mattgu15@student.hh.se"
    to_addr = "matti.gustafsson@gmail.com"

    message = MIMEMultipart()
    message['From'] = from_addr
    message['To'] = to_addr
    message['Subject'] = subject

    body = medd
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(from_addr, "ZXCvbnm")
    text = message.as_string()

    server.sendmail(from_addr, to_addr, text)
    server.quit()


def main():
    "Main module for testing the send_mail module."
    send_mail("From main", "Message from main")


if __name__ == "__main__":
    main()

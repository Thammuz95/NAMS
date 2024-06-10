import smtplib
from email.mime.text import MIMEText


def send_alert(subject, body):
    """
    Sends an email alert with the given subject and body.

    Parameters:
    subject (str): Subject of the email
    body (str): Body of the email

    Returns:
    void: Sends an email alert
    """
    try:
        # Create the email content
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = "your_email@example.com"
        msg["To"] = "admin@example.com"

        # Connect to the SMTP server
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login("your_email@example.com", "password")  # Login to the SMTP server
            server.sendmail("your_email@example.com", "admin@example.com", msg.as_string())  # Send the email
        print(f"Alert sent: {subject}")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

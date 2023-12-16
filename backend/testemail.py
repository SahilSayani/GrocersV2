import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
from models import User
load_dotenv()
def send_notification(email):
    print("sending email to" + email)
    sender_address = 'sahilsayani7@gmail.com'  # Replace with your email address
    sender_pass = os.getenv("EMAIL_PWD")              # Replace with your email password
    receiver_address = email

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Daily Reminder from Grocers'  # Subject of the email

    # Email body
    mail_content = '''Hello,

This is a friendly reminder to check out the latest products from our store.

Best regards,
Team Grocers.'''

    # Attach the body with the msg instance
    message.attach(MIMEText(mail_content, 'plain'))

    # Create SMTP session for sending the mail
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587)  # Use mail provider's SMTP server
        session.starttls()  # Enable security
        session.login(sender_address, sender_pass)  # Login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent to', receiver_address)
    except Exception as e:
        print('Error occurred: ', str(e))

# send_notification("sahilsayani7@gmail.com")
        
def generate_report_html(user, cart_items):
    total_expenditure = sum(item.product.price * item.quantity for item in cart_items)
    html_content = f"<html><body><h1>Monthly Report for {user.name}</h1>"
    html_content += "<h2>Items Purchased:</h2><ul>"
    for item in cart_items:
        html_content += f"<li>{item.product.name} - Quantity: {item.quantity}, Price: {item.product.price}</li>"
    html_content += "</ul>"
    html_content += f"<p>Total Expenditure: {total_expenditure}</p>"
    html_content += "</body></html>"
    return html_content

def send_email(receiver_address, html_content):
    sender_address = 'sahilsayani7@gmail.com'  # Replace with your email address
    sender_pass = os.getenv("EMAIL_PWD")             # Replace with your email password

    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Monthly Activity Report'

    # Attach the HTML content
    message.attach(MIMEText(html_content, 'html'))

    # Create SMTP session for sending the mail
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your SMTP server
        session.starttls()  # Enable security
        session.login(sender_address, sender_pass)  # Login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
    except Exception as e:
        print(f'Error occurred: {e}')



send_email("sahilsayani7@gmail.com", generate_report_html(User, {
    "product": {
        "name": "product",
        "price": 10
    },
    "quantity": 2
}))
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import path
from models import User,Category,Product,Role, Cart, CartItem
from db_instance import db
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from flask_cors import CORS

import os
from celery import Celery, Task
from celery.schedules import crontab
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

def celery_init_app(app: Flask) -> Celery:
    class Cel(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=Cel)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app

app = Flask(__name__)
app.config['SECRET_KEY']="abcdefg"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///grocers.sqlite3'
app.config.from_mapping(
    CELERY=dict(
        broker_url="redis://localhost:6379",
        result_backend="redis://localhost:6379",
        task_ignore_result=True
    ),
)
jwt = JWTManager(app)
CORS(app)

celery_app = celery_init_app(app)

celery_app.conf.timezone = 'Asia/Kolkata'
from celery.schedules import crontab
import models,datetime

with app.app_context():
    db.init_app(app)
    db.create_all()

celery_app.conf.beat_schedule = {
    # 'send-monthly-report': {
    #     'task': 'app.send_monthly_report',
    #     'schedule': crontab(day_of_month=1, hour=0, minute=0),
    # },
    # 'send-monthly-report': {
    #     'task': 'app.send_monthly_report',
    #     'schedule': crontab(minute='*/01'),
    # },

}


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender,**kwargs):
    # sender.add_periodic_task(crontab(hour=14, minute=34), send_daily_reminders.s())
    sender.add_periodic_task(crontab(minute='*/01'), send_daily_reminders.s())
    # sender.add_periodic_task(crontab(minute='*/01'), send_monthly_report.s())

@celery_app.task
def send_daily_reminders():
    print("Sending daily reminders")
    with app.app_context():
        # Logic to find users who haven't visited/bought anything
        users_to_notify = User.query.filter_by(role=3).all()
        for user in users_to_notify:
            send_notification(user.email) 

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


# @celery_app.task
# def send_monthly_report():

#     users = User.query.filter_by(role=2).all()
#     for user in users:
#         # Fetch cart items for the user in the specified time frame
#         cart_items = CartItem.query.join(Cart).filter(
#             Cart.user_id == user.id
#             )

#         if cart_items:
#             report_html = generate_report_html(user, cart_items)
#             send_email2(user.email, report_html)

# def generate_report_html(user, cart_items):
#     total_expenditure = sum(item.product.price * item.quantity for item in cart_items)
#     html_content = f"<html><body><h1>Monthly Report for {user.name}</h1>"
#     html_content += "<h2>Items Purchased:</h2><ul>"
#     for item in cart_items:
#         html_content += f"<li>{item.product.name} - Quantity: {item.quantity}, Price: {item.product.price}</li>"
#     html_content += "</ul>"
#     html_content += f"<p>Total Expenditure: {total_expenditure}</p>"
#     html_content += "</body></html>"
#     return html_content

# def send_email2(receiver_address, html_content):
#     sender_address = 'sahilsayani7@gmail.com'  
#     sender_pass = os.getenv("EMAIL_PWD")            

#     # Set up the MIME
#     message = MIMEMultipart()
#     message['From'] = sender_address
#     message['To'] = receiver_address
#     message['Subject'] = 'Monthly Activity Report'

#     # Attach the HTML content
#     message.attach(MIMEText(html_content, 'html'))

#     # Create SMTP session for sending the mail
#     try:
#         session = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your SMTP server
#         session.starttls()  # Enable security
#         session.login(sender_address, sender_pass)  # Login with mail_id and password
#         text = message.as_string()
#         session.sendmail(sender_address, receiver_address, text)
#         session.quit()
#     except Exception as e:
#         print(f'Error occurred: {e}')

def getCSV():
    csv = ''
    csv+="Name,Price,Available Qty,Category\n"
    prod = Product.query.all()
    for product in prod:
        csv+=product.name
        csv+=','
        csv+=str(product.price)
        csv+=','
        csv+=str(product.available_quantity)
        csv+=','
        csv+=str(product.category_id)
        csv+="\n"
    return csv        


@celery_app.task(name="app.triggerReport")
def triggerReport(mail):
    print("Here")
    sender_email = "sahilsayani7@gmail.com"
    sender_password = os.getenv("EMAIL_PWD")
    receiver_email = mail

    message = MIMEMultipart("alternative")
    message["Subject"] = "Products summary"
    message["From"] = sender_email
    message["To"] = receiver_email

    csv = MIMEText(getCSV())
    message.attach(csv)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls(context=ssl.create_default_context())  # Secure the connection
            server.login(sender_email, sender_password)  # Log in to the SMTP server
            server.sendmail(sender_email, receiver_email, message.as_string())
            print('Mail Sent to', receiver_email)
    except Exception as e:
        print('Error occurred:', e)

@app.route('/')
def main():
    return "Hello"

@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.filter_by(active=True).all()
    # print(categories)
    category_list = [{"id":category.id, "name":category.name} for category in categories]
    # print(category_list)
    return jsonify(category_list)

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = []
    for product in products:
        product_data = {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "availableQuantity": product.available_quantity,
        "categoryId": product.category_id,
        "image": product.image
    }
        product_list.append(product_data)
    # print(product_list)
    return jsonify(product_list)



@app.route("/login", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    # Query your database for email and password
    user = User.query.filter_by(email=email, password=password).first()

    if user is None:
        # the user was not found on the database
        return jsonify({"msg": "Bad username or password"}), 401
    
    # create a new token with the user id inside
    access_token = create_access_token(identity=user.id)
    return jsonify({ "token": access_token, "user_id": user.id, "user_email": user.email, "user_role": user.role })


@app.route("/signup", methods=["POST"])
def signup():
    name = request.json.get("name", None)
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    # Hash password later
    new_user = User(email=email, password=password, name=name, role=3)
    db.session.add(new_user)
    db.session.commit()


    # Add user's Cart as well
    user = User.query.filter_by(email=email).first()
    new_cart = Cart(user_id=user.id)
    db.session.add(new_cart)
    db.session.commit()

    return "Success"

@app.route("/cart", methods=["POST"])
@jwt_required()
def add_to_cart():

    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()

    cart = Cart.query.filter_by(user_id=current_user_id).first()

    if cart is None:
        # If the user doesn't have a cart, create a new one
        cart = Cart(user_id=current_user_id)
        db.session.add(cart)
        db.session.commit()

    product_id = request.json.get("product_id")
    quantity = request.json.get("quantity")

    new_cart_item = CartItem(user_id=current_user_id, cart_id=cart.id, product_id=product_id, quantity=quantity)
    db.session.add(new_cart_item)
    db.session.commit()

    return "Success"

@app.route("/cart", methods=["GET"])
@jwt_required()
def get_cart_items():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()

    cart = Cart.query.filter_by(user_id=current_user_id).first()

    cart_items = CartItem.query.filter_by(cart_id=cart.id).all()

    items = []

    for item in cart_items:
        product = Product.query.filter_by(id=item.product_id).first()
        items.append({
            "product_id": item.product_id,
            "quantity": item.quantity,
            "name": product.name,
            "price": product.price,
        })

    return items

@app.route("/product", methods=["POST"])
@jwt_required()
def add_product():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()

    if user.role == 3:
        return "Unauthorized"

    name = request.json.get("name", None)
    price = request.json.get("price", None)
    available_quantity = request.json.get("available_quantity", None)
    category_id = request.json.get("category_id", None)
    image = request.json.get("image", None)

    new_product = Product(name=name, price=price, available_quantity=available_quantity, category_id=category_id, image=image)
    db.session.add(new_product)
    db.session.commit()

    return "Success"

@app.route("/summary", methods=["POST"])
@jwt_required()
def send_summary():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()
    #manager only
    if user.role != 2:
        return "Unauthorized"

    email = request.json.get("email", None)

    triggerReport(email)

    return "Success"

@app.route("/addcategory", methods=["POST"])
@jwt_required()
def add_category():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()

    if user.role == 3:
        return "Unauthorized"

    name = request.json.get("name", None)
    new_category = Category(name=name,active=False)
    db.session.add(new_category)
    db.session.commit()

    return "Success"

@app.route('/pendingcategories', methods=['GET'])
@jwt_required()
def get_pendingcategories():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()

    if user.role != 1:
        return "Unauthorized"

    categories = Category.query.filter_by(active=False).all()
    # print(categories)
    category_list = [{"id":category.id, "name":category.name} for category in categories]
    # print(category_list)
    return jsonify(category_list)


@app.route("/category", methods=['PATCH'])
@jwt_required()
def patch_category():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()

    if user.role != 1:
        return "Unauthorized"

    current_id = request.json.get("id", None)

    category = Category.query.filter_by(id=current_id).first()
    category.active = True    
    db.session.commit()

    return "Success";

@app.route("/category/<current_id>", methods=["GET"])
def get_category(current_id):
    category = Category.query.get(current_id)

    return category.name

@app.route("/category/<current_id>", methods=["PATCH"])
@jwt_required()
def update_category(current_id):
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()

    if user.role != 1:
        return "Unauthorized"
    
    name = request.json.get("name", None)

    category = Category.query.get(current_id)
    category.name = name
    db.session.commit()

    return "Success"

@app.route("/category/<current_id>", methods=["DELETE"])
@jwt_required()
def delete_category(current_id):
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()

    if user.role != 1:
        return "Unauthorized"

    category = Category.query.get(current_id)
    db.session.delete(category)
    db.session.commit()

    return "Success"

@app.route("/adminaddcategory", methods=["POST"])
@jwt_required()
def admin_add_category():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()

    if user.role != 1:
        return "Unauthorized"

    name = request.json.get("name", None)
    new_category = Category(name=name,active=True)
    db.session.add(new_category)
    db.session.commit()

    return "Success"

@app.route('/category/<current_id>/products', methods=['GET'])
def get_products_by_category(current_id):
    products = Product.query.filter_by(category_id=current_id).all()
    product_list = []
    for product in products:
        product_data = {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "availableQuantity": product.available_quantity,
        "categoryId": product.category_id,
        "image": product.image
    }
        product_list.append(product_data)
    # print(product_list)
    return jsonify(product_list)

@app.route('/product/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = Product.query.get(product_id)

    product_data = {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "availableQuantity": product.available_quantity,
        "categoryId": product.category_id,
        "image": product.image
    }

    return jsonify(product_data)

if __name__=="__main__":
    app.run(debug=True)


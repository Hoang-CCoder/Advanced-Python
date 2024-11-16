from io import BytesIO
import os
import secrets
from flask import Flask, render_template, request, send_file, session, flash, url_for, redirect
import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Khóa bảo mật cho session

bcrypt = Bcrypt()

# Cấu hình kết nối MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'HuyHoang2911'
app.config['MYSQL_DB'] = 'userdb'

# Kết nối cơ sở dữ liệu
def get_db_connection():
    return mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )

# Route trang chủ (index)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2')
def index2():
    if 'logged_in' not in session:
        flash('Bạn cần đăng nhập để vào trang này!', 'error')
        return redirect(url_for('login'))
    return render_template('index2.html')

@app.route('/shoppingCart')
def shoppingCart():
    if 'logged_in' not in session:
        flash('Bạn cần đăng nhập để vào trang này!', 'error')
        return redirect(url_for('login'))
    return render_template('shoppingCart.html')

# Route đăng ký
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        # Kiểm tra mật khẩu
        if password != confirm_password:
            flash('Mật khẩu xác nhận không khớp!', 'error')
            return redirect(url_for('register'))

        # Mã hóa mật khẩu
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Kiểm tra tên đăng nhập đã tồn tại
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('Tên đăng nhập đã tồn tại!', 'error')
            return redirect(url_for('register'))

        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()

        flash('Đăng ký thành công!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

# Route đăng nhập
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT username, password FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user and bcrypt.check_password_hash(user[1], password):
            session['logged_in'] = True
            flash('Đăng nhập thành công!', 'success')
            return redirect(url_for('index2'))
        else:
            flash('Tên đăng nhập hoặc mật khẩu không chính xác', 'error')

    return render_template('login.html')

# Thêm sản phẩm vào giỏ hàng
def add_to_cart(product_id, product_name, product_price, product_image, quantity):
    cart_item = {
        'product_id': product_id,
        'product_name': product_name,
        'product_price': product_price,
        'product_image': product_image,
        'quantity': quantity
    }

    if 'cart' in session:
        cart = session['cart']
        for item in cart:
            if item['product_id'] == product_id:
                item['quantity'] += quantity
                break
        else:
            cart.append(cart_item)
    else:
        session['cart'] = [cart_item]

    session.modified = True

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        country = request.form['country']
        city = request.form['city']
        total_quantity = request.form['total_quantity']
        total_price = request.form['total_price']

        # Kết nối cơ sở dữ liệu
        conn = get_db_connection()
        cursor = conn.cursor()

        # Chỉ lưu thông tin đơn hàng vào bảng 'orders'
        cursor.execute("""
            INSERT INTO orders (name, phone, address, country, city, total_quantity, total_price)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (name, phone, address, country, city, total_quantity, total_price))

        conn.commit()
        order_id = cursor.lastrowid  # Lấy ID của đơn hàng vừa thêm

        conn.close()

        # Sau khi lưu đơn hàng, chuyển hướng đến trang hóa đơn
        return redirect(url_for('invoice', order_id=order_id))

    # Tính toán tổng số lượng và tổng tiền cho giỏ hàng
    cart_items = session.get('cart', [])
    total_quantity = sum(item['quantity'] for item in cart_items)
    total_price = sum(item['product_price'] * item['quantity'] for item in cart_items)

    return render_template('checkout.html', cart_items=cart_items, total_quantity=total_quantity, total_price=total_price)


@app.route('/invoice/<int:order_id>')
def invoice(order_id):
    # Kết nối cơ sở dữ liệu
    conn = get_db_connection()
    cursor = conn.cursor()

    # Lấy thông tin đơn hàng từ bảng 'orders'
    cursor.execute("""
        SELECT name, phone, address, country, city, total_quantity, total_price
        FROM orders
        WHERE order_id = %s
    """, (order_id,))
    order = cursor.fetchone()  # Trả về một dòng thông tin đơn hàng

    if not order:
        return "Đơn hàng không tồn tại", 404

    conn.close()

    # Hiển thị hóa đơn với thông tin đơn hàng
    return render_template('invoice.html', order=order)

if __name__ == "__main__":
    app.run(debug=True)



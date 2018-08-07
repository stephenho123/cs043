import sqlite3

connection = sqlite3.connect('business.db')
connection.execute('CREATE TABLE products (prodname, price, weight)')
#This line creates the first table, called products, which holds the name, price, and weight of the product.
#connection.execute('CREATE TABLE users (name, password, email)')
#This line creates a second table, called users, which holds the name, password, and email of the user.

# Create
connection.execute('INSERT INTO products VALUES (?, ?, ?)', ['book', 7.99, 0.5])
connection.execute('INSERT INTO products VALUES (?, ?, ?)', ['drink', 2.00, 0.4])
connection.execute('INSERT INTO products VALUES (?, ?, ?)', ['car', 70000, 1875])

connection.commit()

# Read
cursor = connection.cursor()

product_cursor = cursor.execute('SELECT * FROM products')
product_list = product_cursor.fetchall()

for product in product_list:
    print(product)

# Update
connection.execute('UPDATE products SET weight = ?', [9])  # Set all weights to 9
connection.commit()

# Delete

connection.execute('DELETE FROM products')                 # Delete all rows in products
connection.commit()

# Check if username Joe is taken
products = cursor.execute('SELECT * FROM users WHERE username = ?', ['Joe'])

# Verify the username and password stored in variables u and p, respectively
products = cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', [u, p])

# Set all weights smaller than 1 to 0
connection.execute('UPDATE products SET weight = ? WHERE weight < ?', [0, 1])

# Delete book from the product list
connection.execute('DELETE FROM products WHERE prodname = ?', ['book'])

# DELETE FROM products WHERE price > 10-
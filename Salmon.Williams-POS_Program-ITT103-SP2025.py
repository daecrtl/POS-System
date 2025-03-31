# Pythonistas' Point of Sale (POS) system
# Best Buy Retail Store

def initialize_inventory(): # Initialize Inventory with prices and stock
# Return allows the inventory to be edited and used elsewhere
  return {
    "Phone": {"Price": 3000.00, "Stock": 10},
    "Tv": {"Price": 5000.00, "Stock": 40},
    "Laptop": {"Price": 2000.00, "Stock": 50},

    "Table": {"Price": 1500.00, "Stock": 30},
    "Chair": {"Price": 1200.00, "Stock": 60},
    "Lamp": {"Price": 500.00, "Stock": 20},

    "Milk": {"Price": 150.00, "Stock": 60},
    "Cheese": {"Price": 140.50, "Stock": 50},
    "Butter": {"Price": 200.30, "Stock": 18},

    "Soap": {"Price": 200.10, "Stock": 100},
    "Rag": {"Price": 115.00, "Stock": 5},
    "Towel": {"Price": 400.00, "Stock": 40},

    "Soda": {"Price": 350.00, "Stock": 80},
    "Juice": {"Price": 220.00, "Stock": 70},
    "Water": {"Price": 100.00, "Stock": 90},

    "Truck": {"Price": 1200.80, "Stock": 60},
    "Doll": {"Price": 1000.20, "Stock": 20},
    "Teddy": {"Price": 700.30, "Stock": 40},}

def report():  # Alerts if any stock reaches under 5 (Low-stock)
  for product, details in inventory.items():
    if details['Stock'] < 5:
      print(f"ALERT: There are only {details['Stock']} of {product} remaining.")

#Assign a variable name for ease of use
inventory = initialize_inventory()


class Cart:
  def __init__(self):
    self.cart = {} # initializes cart as a dictionary

  def add_to_cart(self): # Adds to cart
      item = input('Enter product: ').strip().capitalize() # Capitalizes input
      quantity = int(input('Enter quantity: '))
      # Checks for the item in inventory
      if item in inventory:
          # Checks if quantity is greater than amount remaining in stock
          if inventory[item]['Stock'] < quantity:
              print(f"Only {inventory[item]['Stock']} remaining.")
          else:
              price = inventory[item]['Price'] * quantity # Calculates price
              inventory[item]['Stock'] -= quantity # Reduces stock
              # Adds the items' price and quantity to cart
              if item in self. cart:
                  self.cart[item]['Quantity'] += quantity
                  self.cart[item]['Price'] += price
              else:
                  self.cart[item] = {'Quantity': quantity, 'Price': price}
              print(f'{item} is added to cart at ${price}.')
      else: # If item is not available
          print(f'{item} is not available.')

  def remove_from_cart(self): # Removes item(s) from cart
    item = input('Enter product you would like to remove: ').strip().capitalize() # Capitalizes input
    quantity = int(input(f'How many {item}s do you want to remove: '))
    # Checks for item in cart
    if item in self.cart:
      # Removes quantity of item from cart
      if quantity < self.cart[item]['Quantity']:
        self.cart[item]['Quantity'] -= quantity
        # Calculates new price
        new_price = self.cart[item]['Price'] - (quantity * inventory[item]['Price'])
        self.cart[item]['Price'] = new_price
        # Restore the removed quantity to inventory
        inventory[item]['Stock'] += quantity
        print(f'{quantity} of {item} has been removed from cart.')
      # Removes entire item from cart
      elif quantity == self.cart[item]['Quantity']:
        del self.cart[item]
        inventory[item]['Stock'] += quantity
        print(f'{item} has been removed from cart.')
        # If the quantity entered is greater that the quantity in cart
      elif quantity > self.cart[item]['Quantity']:
        print(f"There are only {self.cart[item]['Quantity']} of {item} in the cart.")
    else: # If that item was not in the cart
      print(f'{item} is not in the cart.')
    self.view_cart()

  def view_cart(self): # Displays cart
    print('-' * 12)
    print('Cart')
    print('-' * 12)
    # Shows the item, quantity and price
    for item, info in self.cart.items():
      quantity = info['Quantity']
      price = info['Price']
      print(f'{quantity} of {item} for ${price}')


class Checkout: # Checkout cart
  def __init__(self):
    self.subtotal = 0
    self.tax = 0
    self.total = 0
    self.cash = 0
    self.change = 0
    self.discount = 0

  def calculate_total(self, cart): # Calculates total
    for item, info in cart.cart.items():
        # Calculates subtotal
      self.subtotal += info['Price']
        # 10% sales tax on subtotal
    self.tax = self.subtotal * 0.1
    self.tax = round(self.tax, 2)
    # Calculates total after tax
    self.total = self.subtotal + self.tax
    # Calculates discount
    if self.total >= 10000.00: # Discount System- 5% for $10,000 or more
      self.discount = self.total * 0.05
      self.discount = round(self.discount, 2)
      self.total = self.total - self.discount
    else:
      self.discount = 0.0
      self.total = self.total

  def calculate_change(self, cart): # Calculates change
    self.calculate_total(cart)
    print(f'The total is: ${self.total}')
    self.cash = (float(input('Enter amount received from customer: ')))
    # If the customer does not give enough money
    while self.cash < self.total:
      print(f'This is not enough money, the total is: ${self.total}')
      self.cash = (int(input('Enter amount received from customer: ')))
    self.change = self.cash - self.total
    self.change = round(self.change, 2)
    print(f'Cash: ${self.cash}')
    print(f'Change: ${self.change}')

  def create_receipt(self, cart):  # Creates receipt
      print("*" * 55)
      print("\t\t\t\t Best Buy Retail Store")
      print("\t\t\t\t   Montego Bay, JA")
      print("\t\t\t\t    (876)123-4567")
      print("=" * 55)
      print('\t\t\t\t\t  RECEIPT')
      print('=' * 55)
      print('Item \t\t\t\t\t\t\t\t Price')
      for item, info in cart.cart.items():
        if item in inventory:
          price = inventory[item]['Price']
          print(f"{info['Quantity']} of {item} at ${price} each: \t\t\t ${info['Price']}")
      print('-' * 55)
      print(f'\t\t\t\t\t\tSubtotal:\t ${self.subtotal}')
      print(f'\t\t\t\t\t\tSales Tax:\t ${self.tax}')
      print(f'\t\t\t\t\t\tDiscount:\t ${self.discount}')
      print('-' * 55)
      print(f'\t\t\t\t\t\tBalance:\t ${self.total}')
      print(' ')
      print(f'\t\t\t\t\t\tCash:\t\t ${self.cash}')
      print(f'\t\t\t\t\t\tChange:\t\t ${self.change}')
      print("=" * 55)
      print('\t\t THANK YOU FOR SHOPPING AT BEST BUY')
      print('*' * 55)


# Displays the menu that the cashier will interact with
def main():
  cart = Cart()
  checkout = Checkout()

  while True:
    try:
      print('-' * 55)
      print('\tMenu Options')
      print('\t1. View Cart')
      print('\t2. Add to Cart')
      print('\t3. Remove from Cart')
      print('\t4. Checkout')
      print('\t5. New transaction')
      print('\t6. Exit')
      report()
      print('-' * 55)
      choice = int(input('Enter your choice: '))
      # To view cart
      if choice == 1:
        cart.view_cart()
        # To add to cart
      elif choice == 2:
        cart.add_to_cart()
        # To remove from cart
      elif choice == 3:
        cart.remove_from_cart()
        # To checkout- get change and receipt
      elif choice == 4:
        checkout.calculate_change(cart)
        checkout.create_receipt(cart)
        # To start a new transaction
      elif choice == 5:
        print('-' * 40)
        print('New transaction')
        cart.cart = {} # Clears cart
        checkout = Checkout() # Reinitializes Checkout class
        continue # Goes to the start of while True loop
        # To exit system
      elif choice == 6:
        print('Exiting system')
        break
      else:
        # If input is not from 1-6
        print('Invalid input')
    except ValueError as e:
     print(f'Error: {e}, try again')

if __name__ == '__main__':
  main()

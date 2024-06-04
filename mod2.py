import uuid
from datetime import datetime, timedelta

class Transaction:
    def __init__(self, transaction_id, customer_id, name, contact_info, gender, cloth_type, laundry_type, num_pieces, cost, delivery_date):
        self.transaction_id = transaction_id
        self.customer_id = customer_id
        self.name = name
        self.contact_info = contact_info
        self.gender = gender
        self.cloth_type = cloth_type
        self.laundry_type = laundry_type
        self.num_pieces = num_pieces
        self.cost = cost
        self.delivery_date = delivery_date

    def print_slip(self):
        print("Transaction Slip:")
        print(f"Transaction ID: {self.transaction_id}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Contact Info: {self.contact_info}")
        print(f"Gender: {self.gender}")
        print(f"Cloth Type: {self.cloth_type}")
        print(f"Laundry Type: {self.laundry_type}")
        print(f"Number of Pieces: {self.num_pieces}")
        print(f"Cost per Piece: 10 Rupees")
        print(f"Total Cost: {self.cost} Rupees")
        print(f"Delivery Date: {self.delivery_date}")

class CustomerManagement:
    def __init__(self):
        self.customers = {}
        self.transactions = {}

    def create_customer(self, customer_id, name, contact_info, gender):
        self.customers[customer_id] = {
            "name": name,
            "contact_info": contact_info,
            "gender": gender
        }

    def view_customer(self, customer_id):
        if customer_id in self.customers:
            return self.customers[customer_id]
        else:
            return None

    def update_customer(self, customer_id, name=None, contact_info=None, gender=None):
        if customer_id in self.customers:
            if name:
                self.customers[customer_id]["name"] = name
            if contact_info:
                self.customers[customer_id]["contact_info"] = contact_info
            if gender:
                self.customers[customer_id]["gender"] = gender
        else:
            print("Customer not found.")

    def create_transaction(self, customer_id, cloth_type, laundry_type, num_pieces):
        customer = self.view_customer(customer_id)
        if customer:
            transaction_id = str(uuid.uuid4())[:8]  # generate a unique 8-digit transaction ID
            delivery_date = (datetime.now() + timedelta(days=4)).strftime("%Y-%m-%d")  # set delivery date as 4 days from current date
            cost = num_pieces * 10  # calculate total cost based on number of pieces and rate per piece
            transaction = Transaction(transaction_id, customer_id, customer["name"], customer["contact_info"], customer["gender"], cloth_type, laundry_type, num_pieces, cost, delivery_date)
            self.transactions[transaction_id] = transaction
            return transaction
        else:
            print("Customer not found.")

# Example usage:
customer_manager = CustomerManagement()

# Create a new customer
customer_manager.create_customer("C001", "John Doe", "johndoe@example.com", "Male")

# Create a new transaction
transaction = customer_manager.create_transaction("C001", "Shirt", "Wash and Iron", 5)
transaction.print_slip()

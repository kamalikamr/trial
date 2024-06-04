class CustomerManagement:
    def __init__(self):
        self.customers = {}

    def create_customer(self, customer_id, name, contact,gender):
        self.customers[customer_id] = {
            "name": name,
            "contact": contact,
            "gender": gender
        }

    def view_customer(self, customer_id):
        if customer_id in self.customers:
            return self.customers[customer_id]
        else:
            return None

    def update_customer(self, customer_id, name=None, contact=None,gender=None):
        if customer_id in self.customers:
            if name:
                self.customers[customer_id]["name"] = name
            if contact:
                self.customers[customer_id]["contact"] = contact
            if gender:
                self.customers[customer_id]["gender"] = gender
        else:
            print("Customer not found.")

# Example usage:
customer_manager = CustomerManagement()

# Create a new customer
customer_manager.create_customer("C001", "John Doe", "1234567890","Male")

# View customer details
customer = customer_manager.view_customer("C001")
print(customer)

# Update customer details
customer_manager.update_customer("C001", contact="2314567890",gender="Female")

# View updated customer details
customer = customer_manager.view_customer("C001")
print(customer)

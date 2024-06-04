class ServicePointAllocation:
    def __init__(self):
        self.service_points = {}
        self.clothes_allocation = {}

    def allocate_clothes(self, customer_id, clothes):
        service_point = self.get_available_service_point()
        if service_point:
            self.clothes_allocation[customer_id] = {
                "service_point": service_point,
                "clothes": clothes,
                "status": "in_progress"
            }
            return f"Clothes allocated to service point {service_point}"
        else:
            return "No available service points"

    def get_available_service_point(self):
        for service_point, status in self.service_points.items():
            if status == "available":
                self.service_points[service_point] = "in_use"
                return service_point
        return None

    def track_clothes_status(self, customer_id):
        if customer_id in self.clothes_allocation:
            return self.clothes_allocation[customer_id]["status"]
        else:
            return "No clothes allocated for this customer"

    def collect_clothes(self, customer_id):
        if customer_id in self.clothes_allocation:
            clothes = self.clothes_allocation[customer_id]["clothes"]
            service_point = self.clothes_allocation[customer_id]["service_point"]
            self.service_points[service_point] = "available"
            del self.clothes_allocation[customer_id]
            return f"Collected clothes from service point {service_point}"
        else:
            return "No clothes allocated for this customer"

    def close_transaction(self, customer_id):
        if customer_id in self.clothes_allocation:
            self.clothes_allocation[customer_id]["status"] = "completed"
            return f"Transaction closed for customer {customer_id}"
        else:
            return "No clothes allocated for this customer"

# Create an instance of the ServicePointAllocation class
allocator = ServicePointAllocation()

# Add some service points to the system
allocator.service_points = {
    "SP1": "available",
    "SP2": "available",
    "SP3": "available"
}

# Allocate clothes to a customer
customer_id = "C001"
clothes = ["Shirt", "Pant", "T-Shirt"]
result = allocator.allocate_clothes(customer_id, clothes)
print(result)

# Track the status of the clothes
status = allocator.track_clothes_status(customer_id)
print(status)

# Close the transaction
result = allocator.close_transaction(customer_id)
print(result)

# Collect the clothes from the service point
result = allocator.collect_clothes(customer_id)
print(result)

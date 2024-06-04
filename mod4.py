import csv
import os

class ReportGenerator:
    def __init__(self, file_name):
        self.file_name = file_name
        self.headers = ["Customer ID", "Name", "Contact Info", "Gender", "Clothes", "Service Point", "Status", "Delivery Date", "Total Cost"]
        self.create_csv_file()

    def create_csv_file(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)

    def add_customer_details(self, customer_id, name, contact_info, gender, clothes, service_point, status, delivery_date, total_cost):
        if not self.customer_exists(customer_id):
            with open(self.file_name, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([customer_id, name, contact_info, gender, clothes, service_point, status, delivery_date, total_cost])

    def customer_exists(self, customer_id):
        with open(self.file_name, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                if row[0] == customer_id:
                    return True
            return False

    def generate_daily_report(self, date):
        with open(self.file_name, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            daily_report = []
            for row in reader:
                if row[7] == date:
                    daily_report.append(row)
            return daily_report

    def generate_weekly_report(self, start_date, end_date):
        with open(self.file_name, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            weekly_report = []
            for row in reader:
                if start_date <= row[7] <= end_date:
                    weekly_report.append(row)
            return weekly_report

    def generate_monthly_report(self, month, year):
        with open(self.file_name, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            monthly_report = []
            for row in reader:
                if row[7][:7] == f"{year}-{month}":
                    monthly_report.append(row)
            return monthly_report

# Create an instance of the ReportGenerator class
report_generator = ReportGenerator("customer_detail.csv")

# Add customer details to the CSV file
customer_id = "C001"
name = "John Doe"
contact_info = "johndoe@example.com"
gender = "Male"
clothes = ["Shirt", "Pant", "T-Shirt"]
service_point = "SP1"
status = "in_progress"
delivery_date = "2023-03-15"
total_cost = 100
report_generator.add_customer_details(customer_id, name, contact_info, gender, clothes, service_point, status, delivery_date, total_cost)

# Generate daily report
daily_report = report_generator.generate_daily_report("2023-03-15")
print(daily_report)

# Generate weekly report
start_date = "2023-03-13"
end_date = "2023-03-19"
weekly_report = report_generator.generate_weekly_report(start_date, end_date)
print(weekly_report)

# Generate monthly report
monthly_report = report_generator.generate_monthly_report("03", "2023")

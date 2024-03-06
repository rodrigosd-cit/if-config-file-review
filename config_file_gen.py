import os
import random
import string
import xml.etree.ElementTree as ET

# List of cities across the United States
cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas",
    "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte", "San Francisco", "Indianapolis",
    "Seattle", "Denver", "Washington", "Boston", "El Paso", "Detroit", "Nashville", "Portland", "Memphis", "Oklahoma City",
    "Las Vegas", "Louisville", "Baltimore", "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento", "Mesa", "Atlanta",
    "Kansas City", "Colorado Springs", "Raleigh", "Omaha", "Miami", "Long Beach", "Virginia Beach", "Oakland", "Minneapolis",
    "Tulsa", "Arlington"
]

# McDonald's menu items as a reference
mcdonalds_menu = {
    "Burgers": ["Big Mac", "Quarter Pounder with Cheese", "McDouble", "Filet-O-Fish", "McChicken"],
    "Chicken & Sandwiches": ["Spicy McChicken", "Buttermilk Crispy Chicken Sandwich", "McChicken Deluxe", "Artisan Grilled Chicken Sandwich"],
    "Salads": ["Southwest Grilled Chicken Salad", "Bacon Ranch Salad", "Side Salad"],
    "Breakfast": ["Egg McMuffin", "Sausage McMuffin", "Hotcakes", "Big Breakfast", "Hash Browns"],
    "Snacks & Sides": ["French Fries", "Apple Slices", "McNuggets"]
}

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_menu():
    num_categories = random.randint(2, 5)
    categories = []
    for category_name, items in mcdonalds_menu.items():
        if random.choice([True, False]):
            category = ET.Element("category")
            ET.SubElement(category, "name").text = category_name
            num_items = random.randint(1, min(5, len(items)))
            for item_name in random.sample(items, num_items):
                item = ET.Element("item")
                ET.SubElement(item, "name").text = item_name
                ET.SubElement(item, "price").text = str(round(random.uniform(1.0, 10.0), 2))
                category.append(item)
            categories.append(category)
    return categories

def generate_random_employees():
    num_employees = random.randint(1, 10)
    employees = []
    for _ in range(num_employees):
        name = generate_random_string()
        position = random.choice(["Manager", "Cashier", "Cook", "Waiter"])
        hourly_wage = round(random.uniform(8.0, 20.0), 2)
        employee = ET.Element("employee")
        ET.SubElement(employee, "name").text = name
        ET.SubElement(employee, "position").text = position
        ET.SubElement(employee, "hourlyWage").text = str(hourly_wage)
        employees.append(employee)
    return employees

def generate_config_file(output_dir, city):
    for _ in range(40):
        file_name = f"config_{city.replace(' ', '_')}_{_ + 1}.xml"
        file_path = os.path.join(output_dir, file_name)
        
        root = ET.Element("restaurantConfig")
        ET.SubElement(root, "name").text = generate_random_string(10)
        location = ET.SubElement(root, "location")
        ET.SubElement(location, "city").text = city
        ET.SubElement(location, "zipcode").text = str(random.randint(10000, 99999))
        ET.SubElement(root, "currency").text = "USD"
        ET.SubElement(root, "timezone").text = "EST"
        menu = ET.SubElement(root, "menu")
        categories = generate_random_menu()
        for category in categories:
            menu.append(category)
        employees = ET.SubElement(root, "employees")
        employee_list = generate_random_employees()
        for employee in employee_list:
            employees.append(employee)
        operating_hours = ET.SubElement(root, "operatingHours")
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            day_elem = ET.SubElement(operating_hours, "day")
            ET.SubElement(day_elem, "name").text = day
            ET.SubElement(day_elem, "openingTime").text = "09:00"
            ET.SubElement(day_elem, "closingTime").text = "22:00"
        ET.SubElement(root, "onlineOrdering").text = random.choice(["true", "false"])
        ET.SubElement(root, "loyaltyProgramEnabled").text = random.choice(["true", "false"])
        ET.SubElement(root, "driveThruAvailable").text = random.choice(["true", "false"])
        ET.SubElement(root, "language").text = random.choice(["English", "Spanish", "French", "German"])
        ET.SubElement(root, "taxReference").text = generate_random_string(8)
        operations = ET.SubElement(root, "operations")
        # Add process configurations here
        
        tree = ET.ElementTree(root)
        tree.write(file_path)

if __name__ == "__main__":
    output_dir = "config_files"
    os.makedirs(output_dir, exist_ok=True)
    for city in cities:
        generate_config_file(output_dir, city)

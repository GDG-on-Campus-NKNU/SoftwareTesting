# order_system.py

def calculate_order_total(order):
    return sum(item["price"] for item in order["items"])

def calculate_total_revenue(orders):
    return sum(calculate_order_total(order) for order in orders)

def find_highest_value_order(orders):
    return max(orders, key=calculate_order_total)

def display_order_summary(order):
    total = calculate_order_total(order)
    return f"Order {order['id']} by {order['customer']} - Total: ${total}"

def apply_discount(order, discount):
    for item in order["items"]:
        item["price"] -= item["price"] * discount
    return calculate_order_total(order)

def filter_orders_by_customer(orders, customer_name):
    return [order for order in orders if order["customer"] == customer_name]

def calculate_average_order_value(orders):
    if not orders:
        return 0
    total_revenue = calculate_total_revenue(orders)
    return total_revenue / len(orders)

def generate_report(orders):
    summaries = [display_order_summary(order) for order in orders]
    total_revenue = calculate_total_revenue(orders)
    highest_value_order = find_highest_value_order(orders)
    highest_value_summary = display_order_summary(highest_value_order)
    return {
        "summaries": summaries,
        "total_revenue": total_revenue,
        "highest_value_order": highest_value_summary
    }

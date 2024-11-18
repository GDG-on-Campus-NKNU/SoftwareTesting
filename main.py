# main.py
from src.order_system import generate_report

def main():
    orders = [
        {"id": 1, "customer": "Alice", "items": [{"name": "Laptop", "price": 1000}, {"name": "Mouse", "price": 50}]},
        {"id": 2, "customer": "Bob", "items": [{"name": "Keyboard", "price": 100}, {"name": "Monitor", "price": 300}]},
        {"id": 3, "customer": "Charlie", "items": [{"name": "Tablet", "price": 500}]}
    ]
    report = generate_report(orders)
    for summary in report["summaries"]:
        print(summary)
    print(f"Total Revenue: ${report['total_revenue']}")
    print(f"Highest Value Order: {report['highest_value_order']}")


if __name__ == "__main__":
    main()
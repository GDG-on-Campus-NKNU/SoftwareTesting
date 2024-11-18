# test_order_system.py
import pytest
from src.order_system import calculate_order_total, calculate_total_revenue, find_highest_value_order, generate_report, apply_discount, filter_orders_by_customer, calculate_average_order_value

@pytest.fixture
def sample_orders():
    return [
        {"id": 1, "customer": "Alice", "items": [{"name": "Laptop", "price": 1000}, {"name": "Mouse", "price": 50}]},
        {"id": 2, "customer": "Bob", "items": [{"name": "Keyboard", "price": 100}, {"name": "Monitor", "price": 300}]},
        {"id": 3, "customer": "Charlie", "items": [{"name": "Tablet", "price": 500}]}
    ]

# 測試1
def test_1():
    order = {"id": 1, "customer": "Alice", "items": [{"name": "Laptop", "price": 1000}, {"name": "Mouse", "price": 50}]}
    assert calculate_order_total(order) == 1050

# 測試2
def test_2(sample_orders):
    assert calculate_total_revenue(sample_orders) == 1950

# 測試3
def test_3(sample_orders):
    highest_value_order = find_highest_value_order(sample_orders)
    assert highest_value_order["id"] == 1
    assert calculate_order_total(highest_value_order) == 1050

# 測試4
def test_4(sample_orders):
    report = generate_report(sample_orders)
    expected_summaries = [
        "Order 1 by Alice - Total: $1050",
        "Order 2 by Bob - Total: $400",
        "Order 3 by Charlie - Total: $500"
    ]
    assert report["summaries"] == expected_summaries
    assert report["total_revenue"] == 1950
    assert report["highest_value_order"] == "Order 1 by Alice - Total: $1050"

# 測試5
def test_5():
    order = {"id": 1, "customer": "Alice", "items": [{"name": "Laptop", "price": 1000}, {"name": "Mouse", "price": 50}]}
    assert apply_discount(order, 0.1) == 945  # 1050 - 10%

# 測試6
def test_6(sample_orders):
    filtered_orders = filter_orders_by_customer(sample_orders, "Alice")
    assert len(filtered_orders) == 1
    assert filtered_orders[0]["customer"] == "Alice"

# 測試7
def test_7(sample_orders):
    assert calculate_average_order_value(sample_orders) == 650  # 1950 / 3
     
# 測試8
def test_8(sample_orders):
    for order in sample_orders:
        apply_discount(order, 0.1)
    
    report = generate_report(sample_orders)
    expected_summaries = [
        "Order 1 by Alice - Total: $945",
        "Order 2 by Bob - Total: $360",
        "Order 3 by Charlie - Total: $450"
    ]
    assert report["summaries"] == expected_summaries
    assert report["total_revenue"] == 1755  # 945 + 360 + 450
    assert report["highest_value_order"] == "Order 1 by Alice - Total: $945"

# 測試9
def test_9(sample_orders):
    filtered_orders = filter_orders_by_customer(sample_orders, "Alice")
    report = generate_report(filtered_orders)
    expected_summaries = [
        "Order 1 by Alice - Total: $1050"
    ]
    assert report["summaries"] == expected_summaries
    assert report["total_revenue"] == 1050
    assert report["highest_value_order"] == "Order 1 by Alice - Total: $1050"

# 測試10
def test_10(sample_orders):
    average_order_value = calculate_average_order_value(sample_orders)
    report = generate_report(sample_orders)
    expected_summaries = [
        "Order 1 by Alice - Total: $1050",
        "Order 2 by Bob - Total: $400",
        "Order 3 by Charlie - Total: $500"
    ]
    assert report["summaries"] == expected_summaries
    assert report["total_revenue"] == 1950
    assert report["highest_value_order"] == "Order 1 by Alice - Total: $1050"
    assert average_order_value == 650  # 1950 / 3

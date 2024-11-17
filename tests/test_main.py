# test_main.py
import pytest
from main import main

def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    expected_output = (
        "Order 1 by Alice - Total: $1050\n"
        "Order 2 by Bob - Total: $400\n"
        "Order 3 by Charlie - Total: $500\n"
        "Total Revenue: $1950\n"
        "Highest Value Order: Order 1 by Alice - Total: $1050\n"
    )
    assert captured.out == expected_output

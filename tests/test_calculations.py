from calculations import expense_calculator

def test_expense_calculator_without_categories():
    result = expense_calculator([])
    assert result == {"message": "No expenses to report"}

def test_expense_calculator_with_categories():
    result = expense_calculator([
        {"category":"Food","amount":400},
        {"category": "Gas", "amount": 100.90},
        {"category": "Insurance", "amount": 63.44},
        {"category": "Rent", "amount": 1000},
    ])
    assert result == {
        "Total spent on categories": 1564.34,
        "Category Breakdown": {"Food":400, "Gas":100.90,"Insurance":63.44,"Rent":1000}
    }
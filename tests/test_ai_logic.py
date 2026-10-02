from ai_logic import build_budget_text

def test_budget_text_without_budget():
    result = build_budget_text(None)
    assert result == "The user didnt specify the budget"

def test_budget_with_budget():
    result = build_budget_text(1500)
    assert '500' in result
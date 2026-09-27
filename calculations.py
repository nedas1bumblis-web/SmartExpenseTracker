import pandas as pd


def expense_calculator(raw_data:list[dict]):
    expense_categories = pd.DataFrame(raw_data)
    grand_total = expense_categories["amount"].sum()
    expense_sums = expense_categories.groupby('category')['amount'].sum()
    master_dict={
        "Total spent on categories":grand_total,
        "Category Breakdown":expense_sums.to_dict()
    }
    return master_dict






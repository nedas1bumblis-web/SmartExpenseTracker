import json
import asyncio
import os
gemini_api_key = os.getenv("GEMINI_API_KEY")
def formatting_expenses(user_expenses):
    result = ""
    for expense in user_expenses:
        result += f"{expense.category}:{expense.amount} euros\n"
    return result

def build_budget_text(budget):
    if budget is None:
        return "The user didnt specify the budget"
    return f"The user budget is {budget}"

def build_prompt(formatted_expenses,budget_text,user_prompt):
    instructions = "You are a budget advisor for the user on their expenses"
    prompt = f"""
    {instructions}
    Here is what the user is spending:
    {formatted_expenses}
    {budget_text}
    The user asks: {user_prompt}
    """
    return prompt

async def get_ai_response(client,finished_prompt):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent"
    headers = {
        "x-goog-api-key": gemini_api_key
    }
    body = {
        "contents": [
            {
                "parts": [
                    {"text": finished_prompt}
                ]
            }
        ]
    }
    for attempt in range(3):
        try:
            response = await client.post(url, headers=headers, json=body, timeout=30.0)
            data = response.json()
            ai_text = data["candidates"][0]["content"]["parts"][0]["text"]
            return ai_text
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            await asyncio.sleep(3)

    return "Sorry, I can't generate a response right now, Please try again later"
import pandas as pd
from expense_data import load_expenses
from expense_prompt import expense_prompt
from langchain.chat_models import ChatOpenAI


def analyze_expenses():
    df = load_expenses()
    table = df.to_string(index=False)

    llm = ChatOpenAI(temperature=0.2)
    prompt = expense_prompt.format(expense_table=table)
    output = llm.predict(prompt)
    return df, output

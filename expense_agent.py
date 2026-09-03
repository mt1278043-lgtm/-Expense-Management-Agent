import pandas as pd
from typing import TypedDict
from expense_data import load_expenses
from expense_prompt import expense_prompt
from langchain.chat_models import ChatOpenAI
from langgraph.graph import StateGraph, END


class ExpenseState(TypedDict):
    expense_table: str
    validation_result: str
    audit_summary: str


def validate_expenses(state: ExpenseState) -> ExpenseState:
    """Validate expenses against policy limits."""
    llm = ChatOpenAI(temperature=0.2)
    prompt = expense_prompt.format(expense_table=state["expense_table"])
    validation_result = llm.predict(prompt)
    state["validation_result"] = validation_result
    return state


def generate_audit_summary(state: ExpenseState) -> ExpenseState:
    """Generate audit summary based on validation."""
    summary_prompt = f"""
Based on the following expense validation:

{state['validation_result']}

Provide a concise audit summary with:
1. Total compliance issues found
2. Items flagged for review
3. Finance team recommendations
"""
    llm = ChatOpenAI(temperature=0.2)
    audit_summary = llm.predict(summary_prompt)
    state["audit_summary"] = audit_summary
    return state


def analyze_expenses():
    """Analyze expenses using LangGraph workflow."""
    df = load_expenses()
    table = df.to_string(index=False)

    # Create LangGraph workflow
    workflow = StateGraph(ExpenseState)
    workflow.add_node("validate", validate_expenses)
    workflow.add_node("summarize", generate_audit_summary)

    workflow.set_entry_point("validate")
    workflow.add_edge("validate", "summarize")
    workflow.add_edge("summarize", END)

    graph = workflow.compile()

    # Run the workflow
    initial_state = {
        "expense_table": table,
        "validation_result": "",
        "audit_summary": "",
    }

    result = graph.invoke(initial_state)

    return df, result["validation_result"]

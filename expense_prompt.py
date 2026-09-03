from langchain.prompts import PromptTemplate

expense_prompt = PromptTemplate.from_template("""
You are an AI expense compliance auditor.

Below is a list of expenses submitted by an employee:

{expense_table}

Tasks:
1. Check if any items exceed reasonable expense policy limits.
   - Travel > $500
   - Meals > $100
   - Training > $1000
2. Suggest which items should be reviewed or flagged.
3. Provide a summary for the finance team.
""")

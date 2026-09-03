import streamlit as st
from expense_agent import analyze_expenses

st.title("💳 Expense Management Agent")

if st.button("Audit My Expenses"):
    df, result = analyze_expenses()

    st.subheader("📂 Expense Report")
    st.dataframe(df)

    st.subheader("🔍 GPT Expense Review")
    st.write(result)

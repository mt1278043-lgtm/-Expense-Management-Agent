# 💳 Expense Management Agent

AI agent that helps employees and finance teams manage expense reports: it loads
expense entries, categorizes spending, checks policy compliance with an LLM, and
prepares a reimbursement/audit summary — all in an interactive Streamlit app.

## Lab Objectives

- Simulate a dataset of employee expenses
- Automatically categorize and validate expenses
- Use GPT to summarize policy compliance and suggest actions
- Display everything in an interactive Streamlit app

## Tech Stack

- Python
- Pandas
- OpenAI GPT-4 / GPT-3.5
- LangChain
- LangGraph
- Streamlit

## Project Structure

| File                | Purpose                                                        |
| ------------------- | ------------------------------------------------------------- |
| `expense_data.py`   | Simulated mock expense dataset (Pandas DataFrame)            |
| `expense_prompt.py` | LangChain `PromptTemplate` for the compliance auditor        |
| `expense_agent.py`  | Loads data, formats the prompt, calls the LLM                |
| `app.py`            | Streamlit UI — "Audit My Expenses" button                    |
| `requirements.txt`  | Python dependencies                                          |

## Setup

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

Set your OpenAI key (copy `.env.example` to `.env`, or export it):

```bash
export OPENAI_API_KEY="sk-..."      # macOS / Linux
setx OPENAI_API_KEY "sk-..."        # Windows (new shell after)
```

## Run

```bash
streamlit run app.py
```

Click **Audit My Expenses** to see the expense table and the GPT compliance review.

## Policy Limits Checked

- Travel > $500
- Meals > $100
- Training > $1000

## Example Output

```
The submitted expense report contains two items that exceed standard policy limits:

- "Flight to NYC" at $450 is within limits.
- "Hotel Stay" at $600 is acceptable.
- "Team Dinner" at $180 exceeds the $100 meal limit and should be reviewed.
- "Conference Fee" at $1200 exceeds the $1000 training cap.

Recommendations:
- Request itemized receipt for dinner.
- Validate conference details for policy exceptions.
```

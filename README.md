# 💳 Expense Management Agent

An intelligent expense tracking and analysis application powered by Streamlit and OpenAI's GPT models.

## Features

- 📊 Expense tracking and visualization
- 🤖 AI-powered expense analysis using GPT
- 💰 Category-based spending breakdown
- 🔍 Intelligent recommendations for cost optimization
- 📂 Easy-to-use Streamlit interface

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mt1278043-lgtm/-Expense-Management-Agent.git
cd -Expense-Management-Agent
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

Click "Audit My Expenses" to:
1. View your expense data in a formatted table
2. Get AI-powered analysis and recommendations

## Project Structure

```
.
├── app.py                 # Main Streamlit application
├── expense_agent.py       # Core expense analysis logic
├── expense_data.py        # Expense data loading
├── expense_prompt.py      # GPT prompt templates
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

```
OPENAI_API_KEY=your-api-key-here
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License

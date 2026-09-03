import pandas as pd


def load_expenses():
    data = {
        "Date": ["2025-07-01", "2025-07-02", "2025-07-03", "2025-07-03", "2025-07-04"],
        "Description": ["Flight to NYC", "Hotel Stay", "Team Dinner", "Taxi", "Conference Fee"],
        "Category": ["Travel", "Lodging", "Meals", "Transport", "Training"],
        "Amount": [450, 600, 180, 45, 1200],
    }
    df = pd.DataFrame(data)
    return df

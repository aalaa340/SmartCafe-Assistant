# SmartCafe Assistant

**SmartCafe Assistant** is a Python-based, Object-Oriented Programming (OOP) console application that helps customers access information about a café's menu and services.

The application uses **Regular Expressions (Regex)** to identify user questions and extract relevant information. It then searches a JSON data file to provide the requested information.

## Features

- **Drinks Menu:** Displays the available drinks at the café.
- **Ingredients Information:** Retrieves the ingredients of a specific drink.
- **Calorie Information:** Provides nutritional information and calorie details for each drink.
- **Opening Hours:** Checks the café's opening hours for a specific day.
- **Interactive Interface:** Allows users to interact with the application through a simple console interface.

## Technologies & Concepts

- **Python:** Core programming language.
- **Object-Oriented Programming (OOP):** Organized the application into separate classes with specific responsibilities.
- **Regular Expressions (Regex):** Identifies user intents and extracts relevant information from natural language questions.
- **JSON:** Stores and manages café information.
- **File Handling:** Loads and retrieves data from an external JSON file.

##  Project Structure

```text
SmartCafe-Assistant/
│
├── main.py             # Main application and classes
├── cafe_data.json      # Café menu, ingredients, calories, and opening hours
└── README.md           # Project documentation
```

## How It Works

The application consists of two main classes:

### 1. Research Agent

Responsible for retrieving information from `cafe_data.json`.

- Loads café data from the JSON file.
- Uses Regex to extract relevant information from user questions.
- Searches the JSON data based on the identified request.
- Returns the requested information.

### 2. Chat Bot

Responsible for interacting with the user.

- Displays a welcome message.
- Receives user questions.
- Identifies the user's intent using Regex.
- Sends the request to the Research Agent.
- Displays the retrieved information.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Navigate to the project directory:

```bash
cd SmartCafe-Assistant
```

3. Run the application:

```bash
python main.py
```

## 💬 Example Interaction

```text
Welcome to our Smart Cafe!

How can I help you?

User: What drinks do you have?

Assistant: [Displays available drinks]

User: What's in Cappuccino?

Assistant: [Displays Cappuccino ingredients]

User: How many calories in Cappuccino?

Assistant: [Displays nutritional information]

User: When do you open on Monday?

Assistant: [Displays Monday opening hours]

User: exit

Goodbye! Have a lovely day!
```

## Learning Outcomes

Through this project, I practiced:

- Applying OOP principles to structure a Python application.
- Working with external JSON files.
- Using Regex for basic natural language processing.
- Extracting information from user queries.
- Separating user interaction from data retrieval logic.

## Author

**Aalaa Khogali**


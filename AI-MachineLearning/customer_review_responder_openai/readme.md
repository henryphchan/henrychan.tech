# Customer Review Responder Module

## Overview
The Customer Review Responder Module leverages OpenAI's GPT-4 API to analyze customer reviews. It processes a list of review texts and returns a custom rating and reply for each review. The module follows best practices in software engineering, ensuring modularity, robust error handling, and flexibility in input sources.

## Installation

Install the required dependencies using pip:

```
pip install openai pydantic tenacity pandas
```

## Environment Setup
Before running any scripts, you must export your OpenAI API key as an environment variable. Use one of the following commands depending on your operating system:

- Linux / macOS (Bash):
  ```
  export OPENAI_API_KEY="your_openai_api_key_here"
  ```

- Windows (Command Prompt):
  ```
  set OPENAI_API_KEY="your_openai_api_key_here"
  ```

Replace "your_openai_api_key_here" with your actual OpenAI API key.

## Running the Sample Scripts
### sample_usage.py
This script demonstrates the basic usage of the module with a hardcoded list of customer reviews. It calls the module to process the reviews and prints out each review along with its generated rating and custom reply.

To run the script:
```
python sample_usage.py
```

### sample_usage_2.py
This script shows how to read customer reviews from a CSV file and write the output (with additional columns for rating and review response) to another CSV file. The review column name is provided as a parameter.
Usage
```
python sample_usage_2.py --input path/to/your/amazon_review.csv --output path/to/output.csv --column reviewText
```
- Replace path/to/your/amazon_review.csv with the path to your input CSV file.
- Replace path/to/output.csv with the desired path for the output CSV file.
- Replace reviewText with the name of the column in your CSV file that contains the customer reviews.

## Project Structure
```
customer_review_responder/
├── __init__.py
├── models.py
└── review_parser.py
README.md
sample_usage.py
sample_usage_2.py
```

## Sample Data Credit
The sample CSV file used in this project was downloaded from [Kaggle – Online Product Reviews Analysis: Customer Feedback](https://www.kaggle.com/datasets/mehmetisik/amazon-review/data). Thank you to Kaggle for providing this valuable dataset.
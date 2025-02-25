import argparse
import os
import sys
import pandas as pd
from customer_review_responder import get_customer_review_responses

def main():
    # Define and parse command-line arguments.
    parser = argparse.ArgumentParser(
        description="Process a CSV file containing customer reviews, analyze them using the customer_review module, and output responses with ratings."
    )
    parser.add_argument(
        '--input', '-i',
        required=True,
        help='Path to the input CSV file containing reviews.'
    )
    parser.add_argument(
        '--output', '-o',
        required=True,
        help='Path for the output CSV file with added review responses and ratings.'
    )
    parser.add_argument(
        '--column', '-c',
        required=True,
        help='The column name in the CSV file that contains the review text.'
    )
    
    args = parser.parse_args()
    
    input_file = args.input
    output_file = args.output
    review_column = args.column

    # Validate the input file exists.
    if not os.path.exists(input_file):
        print(f"Input file '{input_file}' does not exist.")
        sys.exit(1)

    # Read the CSV file.
    df = pd.read_csv(input_file)
    
    # Ensure the specified column exists.
    if review_column not in df.columns:
        print(f"Error: The input CSV file must contain a '{review_column}' column.")
        sys.exit(1)
    
    # Extract reviews from the specified column.
    review_texts = df[review_column].tolist()
    
    try:
        # Get responses (ratings and custom replies) from the customer_review module.
        responses = get_customer_review_responses(review_texts)
    except Exception as e:
        print("Error during API call:", e)
        sys.exit(1)
    
    # Add two new columns to the DataFrame with the responses.
    df['rating'] = [r.rating for r in responses]
    df['review_response'] = [r.reply for r in responses]
    
    # Write the updated DataFrame to the output CSV file.
    df.to_csv(output_file, index=False)
    print(f"Output written to '{output_file}'")

if __name__ == '__main__':
    main()

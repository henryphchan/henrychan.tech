import json
from typing import List
from openai import OpenAI
from tenacity import retry, wait_random_exponential, stop_after_attempt
from .models import CustomerReview

# Initialize the OpenAI client.
client = OpenAI()

# Function schema for guiding the GPT-4 function call.
function_definition = [{
    "type": "function",
    "function": {
        "name": "parse_customer_reviews",
        "description": """
            Analyze customer reviews, rate them on a scale of 1 (most negative) to 5 (most positive), 
            and provide a custom reply for each. For reviews that are negative (rating 1 or 2), advise the customer to contact customer support. 
            Return the result as a JSON object with a key 'reviews' whose value is an array of objects. Each object should have the keys 'review', 'rating', and 'reply'.
        """,
        "parameters": {
            "type": "object",
            "properties": {
                "reviews": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "review": {
                                "type": "string",
                                "description": "The original customer review text."
                            },
                            "rating": {
                                "type": "integer",
                                "description": "Rating from 1 (most negative) to 5 (most positive)."
                            },
                            "reply": {
                                "type": "string",
                                "description": "The custom reply to the customer review."
                            }
                        },
                        "required": ["review", "rating", "reply"]
                    }
                }
            },
            "required": ["reviews"]
        }
    }
}]

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def get_customer_review_responses(reviews: List[str]) -> List[CustomerReview]:
    """
    Calls the OpenAI API to analyze the provided customer reviews and returns a list of CustomerReview objects.

    :param reviews: List of customer review texts.
    :return: List of CustomerReview objects containing the review, rating, and reply.
    """
    # Build the conversation messages.
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant that analyzes customer reviews. For each review, rate it on a scale from 1 to 5 "
                "(where 1 is most negative and 5 is most positive) and provide a custom reply. In the reply, highlight the key feature mentioned by the customer. "
                "If the review is negative (rating 1 or 2), advise the customer to contact customer support. Return the output as a JSON object with a key 'reviews' "
                "that contains an array of objects with the keys 'review', 'rating', and 'reply'. Do not include any markdown formatting or code fences."
            )
        }
    ]
    
    # Append each review as a separate user message.
    for review_text in reviews:
        messages.append({
            "role": "user",
            "content": review_text
        })
    
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=messages,
        tools=function_definition,
        tool_choice="auto",
        temperature=0.8,
    )
    
    # Extract and parse the function call responses into CustomerReview objects.
    function_calls = response.choices[0].message.tool_calls
    review_objects = []
    for tool_call in function_calls:
        parsed_response = json.loads(tool_call.function.arguments)
        for review_item in parsed_response.get("reviews", []):
            review_objects.append(CustomerReview(**review_item))
    return review_objects

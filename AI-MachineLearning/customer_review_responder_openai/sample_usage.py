from customer_review_responder import get_customer_review_responses

def main():
    # Pass the customer reviews as a list of strings.
    review_texts = [
        "Purchased this for my device, it worked as advertised. You can never have too much phone memory, since I download a lot of stuff this was a no brainer for me.",
        "So this product is a large disappointment...bought it to use in my tablet but the card is forever getting corrupted....I've reformatted the card a few times but it's to the point now that even a reformat doesn't work.. Wasted money...don't recommend purchasing.",
        "It's mini storage. It doesn't do anything else and it's not supposed to. I purchased it to add additional storage to my Microsoft Surface Pro tablet which only come in 64 and 128 GB. It does what it's supposed to and SanDisk has a long standing reputation that speaks for itself."
    ]
    
    try:
        reviews = get_customer_review_responses(review_texts)
        for review in reviews:
            print(f"Review: {review.review}")
            print(f"Rating: {review.rating}")
            print(f"Reply: {review.reply}\n")
    except Exception as e:
        print("API call failed:", e)

if __name__ == "__main__":
    main()

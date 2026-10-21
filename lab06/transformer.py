
"""
Assignment: Lab 06 - Bulk Text Transformer Utility
"""

import argparse

# Step 1: Create a function to convert text to uppercase.
def transform_upper(text):
    return text.upper()

# Step 2: Create a function to convert text to lowercase.
def transform_lower(text):
    return text.lower()

# Step 3: Create a function to count the words in a string.
def get_word_count(text):
    return len(text.split())

# Step 4: Create a function to filter text by length.
def filter_short(text, min_length):
    if len(text) > min_length:
        return text
    else:
        return None

# Step 5: Run the program using command-line arguments.
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--action",
        choices=["upper", "lower", "count", "filter"],
        required=True
    )
    parser.add_argument("--data", required=True)
    parser.add_argument("--min-length", type=int, default=3)

    args = parser.parse_args()

    # Step 6: Split the data into a list of strings.
    data_list = args.data.split(",")

    # Step 7: Process each string based on the selected action.
    for text in data_list:
        if args.action == "upper":
            result = transform_upper(text)
            print(result)

        elif args.action == "lower":
            result = transform_lower(text)
            print(result)

        elif args.action == "count":
            result = get_word_count(text)
            print(result)

        elif args.action == "filter":
            result = filter_short(text, args.min_length)

            if result is not None:
                print(result)

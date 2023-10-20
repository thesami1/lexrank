import json

# Open the JSONL file for reading
with open('test_data_10meetings.jsonl', 'r') as jsonl_file:
    for i, line in enumerate(jsonl_file, start=1):
        try:
            # Parse the JSON object from each line
            data = json.loads(line)

            # Extract the "text" key from the JSON object
            text = data.get('text', '')

            # Define the filename for the text file
            filename = f'urdu_output/{i:03d}.txt'

            # Write the extracted text to the text file
            with open(filename, 'w') as text_file:
                text_file.write(text)

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in line {i}: {e}")
        except Exception as e:
            print(f"Error processing line {i}: {e}")
# import json

# # Input JSONL file name
# input_jsonl_file = "input.jsonl"

# # Output text file name
# output_txt_file = "output.txt"

# with open(input_jsonl_file, 'r') as jsonl_file, open(output_txt_file, 'w') as txt_file:
#     for line in jsonl_file:
#         try:
#             # Parse each line as a JSON object
#             data = json.loads(line)

#             # Check if the JSON object contains a "text" key
#             if "text" in data:
#                 # Extract the "text" value and write it to the output text file
#                 text = data["text"]
#                 txt_file.write(text + '\n')
#         except json.JSONDecodeError:
#             # Handle invalid JSON lines if any
#             print(f"Skipping invalid JSON: {line}")

# print(f"Text extracted from {input_jsonl_file} and saved to {output_txt_file}")


import json

# Open the JSONL file for reading
with open('test_data_10meetings.jsonl', 'r') as jsonl_file:
    for i, line in enumerate(jsonl_file, start=1):
        try:
            # Parse the JSON object from each line
            data = json.loads(line)

            # Extract the "text" key from the JSON object
            text = data.get('text', '')

            # Define the filename for the text file
            filename = f'urdu_output/{i:03d}.txt'

            # Write the extracted text to the text file
            with open(filename, 'w') as text_file:
                text_file.write(text)

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in line {i}: {e}")
        except Exception as e:
            print(f"Error processing line {i}: {e}")
















 
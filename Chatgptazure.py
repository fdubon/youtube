import openai
import logging
import sys
import os


# Set up OpenAI API credentials
openai.api_type="azure"
openai.api_version = "2023-03-15-preview"
openai.api_base = 'https://YOUR ENDPOINT'
openai.api_key = "YOURKEY"


# Set up OpenAI API credentials
deployment_name= "customerexp_text-davinci-003"
endpoint = "https://YOUR ENDPOINT"


# Function to generate text using the GPT-3.5 Turbo model
def generate_text(context, question):
    prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
    response = openai.Completion.create(
        engine="gpt-35-turbo",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        #endpoint=endpoint,
        #deployment=deployment_name
    )

    if response and response.choices:
        return response.choices[0].text.strip()
    else:
        return None

# Read the text file and use its contents as context
def read_context_from_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

# Main function
def main():
    # Path to the text file
    file_path = "transcription.txt"

    # Read context from the file
    context = read_context_from_file(file_path)

    # Prompt the user for questions
    while True:
        question = input("Enter your question (or 'exit' to quit): ")
        if question.lower() == "exit":
            break

        # Generate text using the GPT-3.5 Turbo model
        generated_text = generate_text(context, question)

        # Print the generated answer
        print("Generated Answer:")
        print(generated_text)

if __name__ == "__main__":
    main()

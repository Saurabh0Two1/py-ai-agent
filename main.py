
import argparse
from dotenv import load_dotenv
from google import genai
import os

def main():
    # 1. Load API key from env or raise error
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")
    
    # 2. Parse user arguments from CLI which will serve as the prompt
    parser = argparse.ArgumentParser(description="CLI Bot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    contents = args.user_prompt

    # 3. Create a LLM client to interact with the llm model - gemini 2.5 flash. 
    # Send prompt text to the model via the client.
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.5-flash-image',
        contents=contents,
    )

    # 4. print token usage metrics and LLM response text.
    if response.usage_metadata:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        raise RuntimeError("No tokens data was found")
    print(response.text)


if __name__ == "__main__":
    main()

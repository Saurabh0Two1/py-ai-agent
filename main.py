
# import argparse
# from dotenv import load_dotenv
# from google import genai
# from google.genai import types
# import os

import functions.get_files_info as file_info

def main():
    file_info.get_files_info("calculator", ".")
    # # 1. Load API key from env or raise error
    # load_dotenv()
    # api_key = os.environ.get("GEMINI_API_KEY")
    # if not api_key:
    #     raise RuntimeError("GEMINI_API_KEY environment variable not set")
    
    # # 2. Parse user arguments from CLI which will serve as the prompt
    # parser = argparse.ArgumentParser(description="CLI Bot")
    # parser.add_argument("user_prompt", type=str, help="User prompt")
    # parser.add_argument("--verbose", action="store_true", help="Enable tracking of tokens used by the LLM")
    # user_args = parser.parse_args()

    # # 3. Create multi-message content using types.Content with user role for now
    # messages = [types.Content(role="user", parts=[types.Part(text=user_args.user_prompt)])]

    # # 4. Create a LLM client to interact with the llm model - gemini 2.5 flash. 
    # # Send prompt text to the model via the client.
    # client = genai.Client(api_key=api_key)
    # response = client.models.generate_content(
    #     model='gemini-2.5-flash-image',
    #     contents=messages,
    # )

    # # 5. If verbose, print prompt, token usage metrics
    # if user_args.verbose:
    #     print(f"User prompt: {user_args.user_prompt}")
    #     if response.usage_metadata:
    #         print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    #         print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    #     else:
    #         raise RuntimeError("No tokens data was found")

    # # print LLM response text always
    # print(response.text)


if __name__ == "__main__":
    main()

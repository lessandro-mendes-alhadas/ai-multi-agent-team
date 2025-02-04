import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables from the .env file
def load_env():
    dotenv_path = find_dotenv()
    if dotenv_path:
        print(f"Loading .env file from: {dotenv_path}")
    else:
        print("No .env file found")
    load_dotenv(dotenv_path)
#    print(f"Environment variables loaded: {os.environ}")

def get_claude_api_key():
    load_env()
    api_key = os.getenv('ANTHROPIC_API_KEY')
 #   print(f"ANTHROPIC_API_KEY: {api_key}")
    return api_key

def get_serper_api_key():
    load_env()
    api_key = os.getenv('SERPER_API_KEY')
 #   print(f"SERPER_API_KEY: {api_key}")
    return api_key

# Function to pretty print results
def pretty_print_result(result):
    parsed_result = []
    for line in result.split('\n'):
        if len(line) > 80:
            words = line.split(' ')
            new_line = ''
            for word in words:
                if len(new_line) + len(word) + 1 > 80:
                    parsed_result.append(new_line)
                    new_line = word
                else:
                    if new_line == '':
                        new_line = word
                    else:
                        new_line += ' ' + word
            parsed_result.append(new_line)
        else:
            parsed_result.append(line)
    return "\n".join(parsed_result)
# 🤖 Multi-Agent AI Solutions

This repository contains two innovative projects that demonstrate the power of multi-agent AI systems for different real-world applications. Each project leverages AI agents to collaborate and solve complex tasks efficiently.

## 📂 Project Structure

```
multi-agent/
├── financial-analysis/    # AI agents for financial analysis and trading
└── jobhunting-crew/      # AI agents for resume optimization and job hunting
```

## 🚀 Projects Overview

### 1. Financial Analysis Agents

<p align="center">
  <img src="financial-analysis/images/01-crewai-overview.png" alt="AI Financial Crew Breakdown" width="600">
</p>

A sophisticated multi-agent system designed for financial analysis and trading strategy development. The system employs four specialized agents working in collaboration:

* **Data Analyst Agent**: Processes and analyzes financial data
* **Trading Strategy Agent**: Develops market strategies
* **Trade Advisory Agent**: Provides execution recommendations
* **Risk Advisor Agent**: Manages risk assessment

**Key Features:**
* Integration with Anthropic Claude and other LLMs
* Extensible architecture for custom workflows
* Comprehensive financial data analysis
* Risk-aware trading recommendations

[Learn more about Financial Analysis Agents](./financial-analysis/README.md)

### 2. Job Hunting Crew

An AI-powered system that optimizes job applications and interview preparation using Amazon Bedrock and CrewAI. The system features four specialized agents:

<p align="center">
  <img src="jobhunting-crew/images/02_aicrew-4agents.png" alt="AI Crew Intereview Prep Breakdown" width="600">
</p>

* **Job Researcher**: Analyzes job postings and requirements
* **Personal Profiler**: Evaluates candidate's strengths
* **Resume Strategist**: Tailors resumes to specific positions
* **Interview Coach**: Prepares interview Q&A

**Key Features:**
* Automated job requirement analysis
* Personalized resume optimization
* AI-driven interview preparation
* Modular and extensible architecture

[Learn more about Job Hunting Crew](./jobhunting-crew/README.md)


## 🚀 Getting Started

1. Clone the repository:
```bash
git clone https://github.com/your-username/multi-agent.git
cd multi-agent
```
# Python Environment Configuration with Caching

This repository provides a Python module for managing environment variables with caching, validation, and default configurations. It's designed to simplify handling environment-specific settings in your Python applications.

## Features

*   **Prioritized Environment Loading:** Loads environment variables from multiple `.env` files (e.g., `.env.local`, `.env`, `env`) in a prioritized order.  System environment variables take precedence.
*   **Caching:** Caches environment variables to improve performance.  The cache expires after a configurable time.
*   **Validation:** Validates API keys and other environment variables against specified criteria.
*   **Default Configuration:**  Allows setting default values for environment variables, which are used if the variable isn't found in environment files or system variables.
*   **Immutability:**  Provides a mechanism to make the environment configuration immutable, preventing accidental modifications.
*   **Error Handling:**  Includes custom exceptions for missing or invalid environment variables.
*   **Thread-Safe:** Uses a lock to ensure thread-safe access to environment variables.
*   **Pretty Printing:** Includes utility functions for formatting output, especially JSON, to improve readability.

## Usage

### Installation

No installation is needed since this is just a single Python file.  Simply place the `utils.py` (replace with the actual name of your script) in your project directory.

### Dependencies

This module uses the standard Python library and has no external dependencies.

### Basic Example

```python
from utils import Environment  # Replace utils

# Load environment variables (if not already loaded)
Environment.load_env()

# Get an API key from the environment variables, using a default value if not found
api_key = Environment.get_api_key("MY_API_KEY", default="default_api_key")

# Get a required API key, raising an error if not found
try:
    required_api_key = Environment.get_required_api_key("REQUIRED_API_KEY")
    print(f"Required API Key: {required_api_key}")
except Environment.MissingEnvironmentVariableError as e:
    print(f"Error: {e}")

# Use the API key
if api_key:
    print(f"API Key: {api_key}")

# Pretty print a JSON string
json_string = '{"key1": "value1", "key2": "value2"}'
pretty_json = Environment.pretty_print_result(json_string, format_json=True)
print(pretty_json)
```

### Setting Default Configuration

```python
from utils import Environment  # Replace utils

default_config = {
    "MY_API_KEY": "my_default_api_key",
    "TIMEOUT": "30"
}

Environment.set_default_config(default_config)

api_key = Environment.get_env_variable("MY_API_KEY")  # Will return "my_default_api_key" if not in env
timeout = Environment.get_env_variable("TIMEOUT")    # Will return "30" if not in env

print(f"API Key: {api_key}")
print(f"Timeout: {timeout}")
```

### Making the Environment Immutable

```python
from utils import Environment  # Replace utils

Environment.load_env()
Environment.make_immutable()

# Subsequent calls to load_env() will be ignored.
```

### Environment Variable Files

The module looks for environment variables in the following files by default (in order of priority):

*   `.env.local`
*   `.env`
*   `env`

You can customize the paths to these files using the `dotenv_paths` parameter in the `load_env` method:

```python
from utils import Environment  # Replace utils

Environment.load_env(dotenv_paths=['config/.env', '.env.defaults'])
```

### Custom Exceptions

The module defines the following custom exceptions:

*   `MissingEnvironmentVariableError`: Raised when a required environment variable is missing.
*   `InvalidEnvironmentVariableError`: Raised when an environment variable is invalid.
*   `MissingEnvFileError`: Raised when a required environment file is missing.
*   `InvalidEnvValueError`: Raised when an environment value is invalid.

## API Reference

### `Environment` Class

*   `load_env(force_reload=False, dotenv_paths=None)`: Loads environment variables from .env files.
    *   `force_reload`:  Forces a reload of the .env files and cache.
    *   `dotenv_paths`:  A list of custom paths to .env files.
*   `set_default_config(default_config)`: Sets default configuration values.
*   `get_env_variable(env_var_name, default=None)`:  Retrieves an environment variable.
    *   `env_var_name`: The name of the environment variable.
    *   `default`: The default value to return if the variable is not found.
*   `validate_api_key(api_key, env_var_name)`: Validates an API key.  Raises an `InvalidEnvironmentVariableError` if the key is invalid.
*   `get_api_key(env_var_name, default=None, validate=True)`: Retrieves an API key.
    *   `validate`:  Whether to validate the API key.
*   `get_required_api_key(env_var_name)`: Retrieves a required API key.  Raises a `MissingEnvironmentVariableError` if the key is not found.
*   `make_immutable()`: Makes the environment configuration immutable.
*   `pretty_print_result(result, line_length=80, format_json=False)`: Formats a long string into readable lines, optionally formatting JSON.

### `pretty_print_result` Function

Formats a long string into lines of a specified maximum length, making it easier to read. Optionally formats JSON output for readability.

*   `result`: The string to be formatted.
*   `line_length`: The maximum length of each line. Defaults to 80 characters.
*   `format_json`: Whether to format the output as pretty JSON (default False).
*   Returns: A string with formatted lines.

## 📜 License

Both projects are licensed under the MIT License.

## 🤗 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the solution.
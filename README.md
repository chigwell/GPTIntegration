[![PyPI version](https://badge.fury.io/py/GPTIntegration.svg)](https://badge.fury.io/py/GPTIntegration)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/gptintegration)](https://pepy.tech/project/gptintegration)

# GPTIntegration

`GPTIntegration` is a Python module for integrating GPT models from OpenAI into your projects. It simplifies querying GPT models by handling the setup, communication, and response parsing with the OpenAI API, enabling easy integration and efficient interaction with GPT models.

## Installation

To install `GPTIntegration`, you can use pip:

```bash
pip install GPTIntegration
```

## Usage

### As a Python Module

You can use `GPTIntegration` as a module in your Python scripts.

Example:

```python
from gpt_integration import GPTIntegration

# Initialize the integration with your OpenAI API key
gpt_integration = GPTIntegration('your-openai-api-key')

# Prepare messages
system_message = "Your system message goes here."
user_message = "Your prompt or user message goes here."

# Query GPT and get the response
response = gpt_integration.query_gpt(system_message, user_message)
print(response)
```

### Customizing Your Query

You can customize your query by adjusting the initialization parameters of the `GPTIntegration` class, such as model, temperature, max tokens, and others to fit the specific needs of your application or to tweak the behavior of the GPT model.

## Output Example

When you query GPT using `GPTIntegration`, it sends the system and user messages to the specified GPT model and returns the model's response. Here is an example output:

```
{
    "id": "example-response-id",
    "object": "text_completion",
    "created": 123456789,
    "model": "gpt-3.5-turbo",
    ...,
    "choices": [
        {
            "text": "Response from the GPT model based on the provided messages...",
            "index": 0,
            "logprobs": null,
            "finish_reason": "length"
        }
    ]
}
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/chigwell/gptintegration/issues).

## License

[MIT](https://choosealicense.com/licenses/mit/)

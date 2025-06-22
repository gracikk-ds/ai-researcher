"""Price calculation for Gemini API."""

from typing import Dict

GEMINI_PRICE: Dict[str, Dict[str, float]] = {  # noqa: WPS407
    "gemini-2.0-flash": {"input": 0.1, "output": 0.4},
    "gemini-1.5-flash": {"input": 0.075, "output": 0.3},
    "gemini-1.5-pro": {"input": 1.25, "output": 5.0},
    "gemini-2.5-flash": {"input": 0.15, "output": 0.6},
    "gemini-2.5-pro": {"input": 1.25, "output": 10.0},
}


MILLION_TOKENS: int = 1000000


def get_base_model_name(endpoint_name: str) -> str:
    """Get the base model name from the endpoint name.

    Args:
        endpoint_name (str): The name of the endpoint.

    Returns:
        str: The base model name.

    Raises:
        ValueError: If the model is not found.
    """
    for base_name in GEMINI_PRICE.keys():
        if base_name in endpoint_name:
            return base_name
    raise ValueError(f"Unknown model: {endpoint_name}")


def calculate_inference_price(model_name: str, total_input_token_count: int, total_output_token_count: int) -> float:
    """Calculate the inference price for a given model.

    Args:
        model_name (str): The name of the model.
        total_input_token_count (int): The total number of input tokens.
        total_output_token_count (int): The total number of output tokens.

    Returns:
        float: The inference price.
    """
    base_model = get_base_model_name(endpoint_name=model_name)
    input_price = GEMINI_PRICE[base_model]["input"]
    output_price = GEMINI_PRICE[base_model]["output"]
    input_price_total = input_price * total_input_token_count / MILLION_TOKENS
    output_price_total = output_price * total_output_token_count / MILLION_TOKENS
    return input_price_total + output_price_total

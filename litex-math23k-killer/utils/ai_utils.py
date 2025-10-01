"""ai_utils.py

Utility functions for interacting with AI models to verify LaTeX code.
"""

from openai import OpenAI
import sys
import os

# Add the project root to the Python path to enable imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.config_utils import get_info

API_KEY = get_info("openai_info")["api_key"]
BASE_URL = get_info("openai_info")["base_url"]


def generate_prompt(example_list: list[dict[str, str]], row: dict[str, str]) -> str:
    """
    Generate a prompt for the AI model based on examples and a specific question.

    :param example_list: A list of example dictionaries with 'description' and 'solution' keys.
    :param row: A dictionary containing 'description' and 'solution' keys.
    :return: A formatted prompt string.
    """
    examples = "".join(
        f"标题:\n{ex['title']}\n\n问题:\n{ex['description']}\n\n代码:\n```\n{ex['solution']}\n```\n\n"
        for ex in example_list
    )
    title = row["title"]
    question = row["description"]
    return f"""
你是一个数学题解答专家，你需要根据给定的数学问题和解题步骤生成正确的代码。

请从以下案例中学习：
{examples}

现在，你需要根据你学会的内容，解决下面的问题，请严格遵循问题中给出的步骤：

标题:
{title}

问题:
{question}

你只需要给我提供代码部分的内容，并且代码中只能出现ASCII字符，不能包含任何中文字符。
    """.strip()


def ask_agent(info: tuple[str, str]):
    """
    Ask a specific agent (model) to process the prompt.

    :param info: Tuple containing (model, prompt) strings.
    :return: The agent's response content.
    """
    (model, prompt) = info

    # Initialize client inside the function to avoid pickling issues with multiprocessing
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    return completion

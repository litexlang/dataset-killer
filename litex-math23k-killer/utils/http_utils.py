"""http_utils.py

HTTP utility functions for interacting with the Litex API.
"""

import requests
import sys
import os

# Add the project root to the Python path to enable imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.config_utils import get_info

COLLABORATION_ID = get_info("collaboration_info")["id"]
USERNAME = get_info("user_info")["username"]


def get_example_list(length: int = 10) -> list[dict[str, str]]:
    """
    Fetch a list of example tasks from the API.

    :param length: Number of examples to fetch (default: 10)
    :return: List of dictionaries containing example tasks
    """
    url = f"https://litexlang.com/api/task/like?keyWord=&collaborationId={COLLABORATION_ID}&progress=Solved&solver=All&sort=Most+Reward&requestUsername={USERNAME}&pageNum=0&pageSize={length}"
    resp = requests.get(url).json()
    return resp["data"]["list"]


def get_task_list(length: int = 100) -> list[dict[str, str]]:
    """
    Fetch a list of tasks from the API.

    :param length: Number of tasks to fetch (default: 100)
    :return: List of dictionaries containing tasks
    """
    url = f"https://litexlang.com/api/task/like?keyWord=&collaborationId={COLLABORATION_ID}&progress=All&solver=All&sort=Most+Reward&requestUsername={USERNAME}&pageNum=0&pageSize={length}"
    resp = requests.get(url).json()
    return resp["data"]["list"]
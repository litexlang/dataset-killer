import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from killer import kill_question
from utils.http_utils import get_task_list


row = get_task_list()[0]
result = kill_question(row)
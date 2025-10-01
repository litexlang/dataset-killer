import pylitex
import re
from utils.ai_utils import ask_agent, generate_prompt
from utils.http_utils import get_example_list


def kill_question(row: dict[str, str]) -> dict[str, str | bool | None]:
    """ """
    prompt = generate_prompt(example_list=get_example_list(), row=row)
    resp = ask_agent(("qwen-long-latest", prompt))

    pattern = r"```(?!claim:).*$"
    answer = re.sub(pattern, "", resp.choices[0].message.content, flags=re.MULTILINE).strip()  # type: ignore

    if pylitex.run(answer)["success"]:
        print(f"Solution verified by Litex.\t{row['id']}")
        return {
            "task_id": row["id"],
            "success": True,
            "solution": answer,
        }
    else:
        print(f"Solution NOT verified by Litex.\t{row['id']}")
        return {
            "task_id": row["id"],
            "success": False,
            "solution": answer,
        }

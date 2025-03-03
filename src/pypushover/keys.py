import os
import dotenv


def dot_path_finder():
    # look for .env files in the parent directories
    original_dir = os.getcwd()
    current_dir = original_dir

    for i in range(3):
        dot_path = os.path.join(current_dir, ".env")
        if os.path.exists(dot_path):
            return dot_path
        current_dir = os.path.dirname(current_dir)

    # also check .venv
    current_dir = original_dir
    
    dot_path = os.path.join(original_dir, ".venv", ".env")
    if os.path.exists(dot_path):
        return dot_path

    raise FileNotFoundError("No .env file found in the parent directories or in .venv")


dot_path = None

def set_dot_path(path: str):
    global dot_path
    dot_path = path


def pushover_keys() -> tuple[str, str]:
    try:
        api_key = os.environ["PUSHOVER_API_KEY"]
        user_key = os.environ["PUSHOVER_USER_KEY"]
        return api_key, user_key
    except KeyError:
        pass
    

    global dot_path
    if not dot_path:
        dot_path = dot_path_finder()
    dotenv.load_dotenv(dot_path)

    try:
        api_key = os.environ["PUSHOVER_API_KEY"]
        user_key = os.environ["PUSHOVER_USER_KEY"]
        return api_key, user_key
    except KeyError:
        raise KeyError(
            "PUSHOVER_API_KEY and PUSHOVER_USER_KEY must be set in the environment ({dot_path})"
        )

if __name__ == "__main__":
    print(pushover_keys())

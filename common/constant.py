import os
import dotenv

loaded = dotenv.load_dotenv()

assert loaded, "Environment variables aren't loaded."

FILE_SAVE_PATH = os.getenv("FILE_SAVE_PATH")

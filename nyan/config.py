import os
from typing import Any
from dotenv import load_dotenv


def get_or_default(value: Any, default: Any) -> Any:
    if value:
        return value
    return default


load_dotenv()


BOT_TOKEN = os.environ["BOT_TOKEN"]
OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]

UPDATE_POSTED_CLUSTERS = get_or_default(os.environ["UPDATE_POSTED_CLUSTERS"], False)
RELATED_CLUSTERS_ENABLED = get_or_default(os.environ["RELATED_CLUSTERS_ENABLED"], False)
SEND_DISCUSSION_MESSAGES = get_or_default(os.environ["SEND_DISCUSSION_MESSAGES"], False)
FILTER_TITILE_RU_ONLY = get_or_default(os.environ["FILTER_TITILE_RU_ONLY"], False)
FILTER_TITILE_OBSCENE = get_or_default(os.environ["FILTER_TITILE_OBSCENE"], False)

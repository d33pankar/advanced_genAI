from openai import OpenAI

from config import get_openai_api_key


def get_openai_client():
    return OpenAI(api_key=get_openai_api_key())

"""
This file contains code for the game "LLM Adventure Game".
Author: SoftwareApkDev
"""


# Game version: 1.0.0


# Importing necessary libraries


import sys
import time
import uuid
import pickle
import copy
from google import genai
from google.genai import types
import random
from datetime import datetime
import subprocess
import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from functools import reduce
from mpmath import mp, mpf
from tabulate import tabulate

mp.pretty = True


# Creating static functions to be used throughout the game.


def is_number(string: str) -> bool:
    try:
        mpf(string)
        return True
    except ValueError:
        return False


def get_llm_output(prompt: str, client: genai.Client, generation_config: dict,
                   model: str = "gemini-3.6-flash", is_local: bool = False) -> str|None:
    """
    Use LLM to get the LLM output of a prompt.
    """
    if is_local:
        llm: OllamaLLM = OllamaLLM(model=model)
        return llm.invoke(prompt)
    else:
        interaction = client.interactions.create(
            model=model,
            input=prompt,
            generation_config=generation_config,
        )
        return interaction.output_text


def clear():
    # type: () -> None
    if sys.platform.startswith('win'):
        subprocess.run('cls')  # For Windows System
    else:
        subprocess.run('clear')  # For Linux System


# Creating necessary classes.


###########################################
# GENERAL
###########################################


class SavedGameData:
    """
    This class contains attributes of the saved game data.
    """


###########################################
# GENERAL
###########################################


# Creating main function used to run the game.


def main() -> int:
    """
    This main function is used to run the game.
    :return: an integer
    """

    load_dotenv()
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    generation_config = {
        'max_output_tokens': 65536,
        'thinking_level': 'medium',
    }


if __name__ == "__main__":
    main()

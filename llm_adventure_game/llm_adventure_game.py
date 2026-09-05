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
# MINIGAMES
###########################################


class Minigame:
    """
    This class contains attributes of a minigame in this game.
    """


###########################################
# MINIGAMES
###########################################


###########################################
# ADVENTURE MODE
###########################################


class Action:
    """
    This class contains attributes of an action which can be carried out during battles.
    """


class AwakenBonus:
    """
    This class contains attributes of the bonus gained for awakening a legendary creature.
    """


class Battle:
    """
    This class contains attributes of a battle in this game.
    """


class City:
    """
    This class contains attributes of a city in this game.
    """


class CityTile:
    """
    This class contains attributes of a tile in a city.
    """


###########################################
# ADVENTURE MODE
###########################################


###########################################
# INVENTORY
###########################################


class LegendaryCreatureInventory:
    """
    This class contains attributes of an inventory containing legendary creatures.
    """


class ItemInventory:
    """
    This class contains attributes of an inventory containing items.
    """


###########################################
# INVENTORY
###########################################


###########################################
# LEGENDARY CREATURE
###########################################


class BattleTeam:
    """
    This class contains attributes of a team brought to battles.
    """


class LegendaryCreature:
    """
    This class contains attributes of a legendary creature in this game.
    """


class Skill:
    """
    This class contains attributes of a skill legendary creatures have.
    """


###########################################
# LEGENDARY CREATURE
###########################################


###########################################
# ITEM
###########################################


class Item:
    """
    This class contains attributes of an item in this game.
    """


###########################################
# ITEM
###########################################


###########################################
# EXERCISE
###########################################


class ExerciseGym:
    """
    This class contains attributes of a gym where the player can improve his/her attributes.
    """


class TrainingOption:
    """
    This class contains attributes of a training option for fitness.
    """


###########################################
# EXERCISE
###########################################


###########################################
# PROPERTIES
###########################################


class Property:
    """
    This class contains attributes of a property the player can live in.
    """


class PropertyUpgrade:
    """
    This class contains attributes of an upgrade to a property a player owns.
    """


###########################################
# PROPERTIES
###########################################


###########################################
# JOBS AND SKILLS
###########################################


class JobRole:
    """
    This class contains attributes of a job role a player can get in this game.
    """


class Course:
    """
    This class contains attributes of a course the player can take in this game.
    """


###########################################
# JOBS AND SKILLS
###########################################


###########################################
# GENERAL
###########################################


class GameCharacter:
    """
    This class contains attributes of a game character.
    """

    def __init__(self, name):
        # type: (str) -> None
        self.character_id: str = str(uuid.uuid1())
        self.name: str = name

    def clone(self):
        # type: () -> GameCharacter
        return copy.deepcopy(self)


class NPC(GameCharacter):
    """
    This class contains attributes of a non-player character in this game.
    """

    def __init__(self, name):
        # type: (str) -> None
        GameCharacter.__init__(self, name)


class Player(GameCharacter):
    """
    This class contains attributes of the player in this game.
    """


class AIPlayer(Player):
    """
    This class contains attributes of an AI controlled player.
    """


class Mission:
    """
    This class contains attributes of a mission in this game.
    """


class Reward:
    """
    This class contains attributes of a reward gained for accomplishing something in this game.
    """


class AdventureModeLocation:
    """
    This class contains attributes of the location of a player in adventure mode of this game.
    """


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

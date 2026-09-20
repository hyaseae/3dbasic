import pickle
from gamebasic.objects.dataclasses.state import GameState
from gamebasic.objects.dataclasses.option import OptionData

def load_game(filename:str = "save01.pickle")->GameState:
    """
    using pickle, load state data.
    make sure that filenames should be reachable afterwards.
    should return state, not class.
    """
    try:
        with open(filename, "rb") as file:
            loaded_state:GameState = pickle.load(file)
    except:
        print("file not found!")
        loaded_state = GameState()

    if not isinstance(loaded_state, GameState):
        raise TypeError("Save file is not correct!")

    return loaded_state

def load_option(filename:str = "option.pickle") -> OptionData:
    """
    load option data.
    """
    try:
        with open(filename, "rb") as file:
            loaded_option:OptionData = pickle.load(file)
    except:
        print("file not found!")
        loaded_option = OptionData()


    if not isinstance(loaded_option, OptionData):
        raise TypeError("saveed option file is not correct!")

    return loaded_option
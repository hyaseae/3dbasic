import pickle
from gamebasic.objects.state import GameState
from gamebasic.objects.option import OptionData

def save_game(state:GameState, filename:str = "save01.pickle") -> None:
    """
    using pickle, save scene data.
    make sure that filenames should be reachable afterwards.
    should pass scene instance, not class.
    """
    with open(filename, "wb") as file:
        pickle.dump(state, file)

    return



def save_option(state:OptionData, filename:str = "option.pickle") -> None:
    """
    using pickle, save option data.
    make sure that filenames should be reachable afterwards.
    should pass scene instance, not class.
    """
    with open(filename, "wb") as file:
        pickle.dump(state, file)

    return
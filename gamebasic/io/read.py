import pickle
from gamebasic.objects.state import GameState

def load_game(filename:str = "save01.pickle")->GameState:
    """
    using pickle, load state data.
    make sure that filenames should be reachable afterwards.
    should return state, not class.
    """
    with open(filename, "rb") as file:
        loaded_state:GameState = pickle.load(file)

    if not isinstance(loaded_state, GameState):
        raise TypeError("Save file is not correct!")

    return loaded_state

import pickle

def load_scene(filename:str = "save01.pickle")->object:
    """
    using pickle, load scene data.
    make sure that filenames should be reachable afterwards.
    should return scene instance, not class.
    """
    with open(filename, "rb") as file:
        loaded_scene:object = pickle.load(file)

    return loaded_scene

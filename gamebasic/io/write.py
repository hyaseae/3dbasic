import pickle

def save_scene(scene:object, filename:str = "save01.pickle") -> None:
    """
    using pickle, save scene data.
    make sure that filenames should be reachable afterwards.
    should pass scene instance, not class.
    """
    with open(filename, "wb") as file:
        pickle.dump(scene, file)

    return
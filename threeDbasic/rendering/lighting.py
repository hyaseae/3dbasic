"""
handles lights.
"""

class LightContainer():
    pass

class LightComponenet():
    def __init__(self) -> None:
        self.light_property = ObjectLightProperty(0,0,1)

    def iterate_light(self):
        """
        
        """


class ObjectLightProperty():
    def __init__(self, transparancy:float, reflexivity:float, diffusitivity:float) -> None:
        """
        preferred to make it's sum 1.
        """
        self.transparancy = transparancy # from 0 to 1
        self.reflexivity = reflexivity # from 0 to 1
        self.diffusitivity = diffusitivity # from 0 to 1
    
        
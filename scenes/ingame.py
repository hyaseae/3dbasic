"""
ingame scene.
"""

SCENE_NAME = "INGAME"


from gamebasic.objects.UI.canvas import canvas
from gamebasic.objects.scene import Scene
from gamebasic.objects.dataclasses.state import GameState
from gamebasic.objects.dataclasses.option import OptionData
from gamebasic.signal.signal_bus import SignalBus
from gamebasic.objects.dataclasses.game_context import GameContext
from gamebasic.objects.UI.img import load_cached_img, Img
from os.path import join as jr
from threeDbasic.objects.camera import Camera3D
import pygame
from gamebasic.signal.signal import Signal
from gamebasic.signal.formal_signals import FormalSignals
from threeDbasic.math.vector import vector3
from threeDbasic.base.world import World3D
from threeDbasic.base.object import Object3d, ShapeType
from threeDbasic.utils.load import read_off_file
from threeDbasic.base.faces import Face, Faces
from threeDbasic.rendering.render_componenet import ColorRenderer, RenderMode



IMG_ASSETS_FOLDER = jr("assets", "UI")
OBJ_ASSETS_FOLDER = jr("assets", "objects")

class IngameScene(Scene):
    def __init__(
        self,
        context : GameContext
    ) -> None:
        super().__init__(context)
        background = pygame.transform.scale(
            load_cached_img(jr(IMG_ASSETS_FOLDER, "background.png")),
            (context.option.screen_width, context.option.screen_height),
        )
        self.canvas = canvas(
            background,
            context.option.screen_width,
            context.option.screen_height,
        )
        self.ui_setup()
        self.camera = Camera3D(pos=vector3(-3, 0, 0))

        self.world = World3D()
        self.world_setup()


    def ui_setup(self):

        self.canvas.img.fill((0,0,0))

        # test_img = Img(load_cached_img(jr("assets", "missing_img.jpg")))
        # self.canvas.add_item(test_img)
        # NOTE: load_cached_img has some issues.
        # TODO: after we add some imgs to background, cached imgs are modified to that. 
        # should be fixed later.

        pass

    def world_setup(self):

        sphere_faces:Faces = read_off_file(jr(OBJ_ASSETS_FOLDER, "colored_sphere.off"))

        sphere = Object3d(pos = vector3(0,0,0), 
                          faces = sphere_faces, 
                          renderer = ColorRenderer(color = pygame.Color(255, 0, 0), 
                                                   render_mode= RenderMode.OBJ_COLOR), 
                          static = True,
                          object_type= ShapeType.SPHERE,
                          radius= 1)
        
        self.world.add_obj(sphere)

        self.world.setup()

    def update(self) -> bool:
        return self.event()

    def render(self, screen: pygame.Surface) -> None:
        self.canvas.render(screen)
        self.world.render(camera=self.camera, screen=screen)

    def event(self) -> bool:
        """
        checks all events that this scene checks for.
        if there was some signal, returns true.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # sending a quit signal.
                self.context.signal_bus.add(Signal(signal_name=FormalSignals.EXIT_GAME.value))
                return True
            else:
                self.canvas.check_event(event)
        return False
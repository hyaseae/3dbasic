"""
home scene for game starting.
"""

from gamebasic.objects.UI.canvas import canvas
from gamebasic.objects.scene import Scene
from gamebasic.objects.dataclasses.state import GameState
from gamebasic.objects.dataclasses.option import OptionData
from gamebasic.signal.signal_bus import SignalBus
import pygame
from gamebasic.signal.signal import Signal
from gamebasic.signal.formal_signals import FormalSignals
from gamebasic.objects.UI.button import Button
from gamebasic.debug.err_img import ERR_IMG
from os.path import join as jr
from gamebasic.objects.UI.img import load_cached_img
from gamebasic.signal.signal_type import SignalType
from threeDbasic.math.vector import vector3
from gamebasic.objects.dataclasses.game_context import GameContext
from gamebasic.objects.UI.text import Text, load_cached_font

SCENE_NAME = "HOME"
BUTTON_ASSETS_FOLDER = jr("assets", "UI", "button")
IMG_ASSETS_FOLDER = jr("assets", "UI")
FONT_ASSETS_FOLDER = jr("assets", "font")


class HomeScene(Scene):
    def __init__(
        self,
        context : GameContext
    ) -> None:
        super().__init__(context)
        self.canvas = canvas(load_cached_img(jr(IMG_ASSETS_FOLDER, "background.png")),
                              context.option.screen_width, 
                              context.option.screen_height)
        self.ui_setup()

    def ui_setup(self):
        """
        make scnes's ui items appropriately appear.
        """

        # button start

        def start(signal_bus:SignalBus):
            signal_bus.add(
                Signal(
                    signal_name=FormalSignals.NEXT_SCENE.value,
                    signal_type=SignalType.STR,
                    data="INGAME"
                )
            )

        button_start_img = load_cached_img(jr(BUTTON_ASSETS_FOLDER, "start.jpg"))

        button_start = Button(
            img=button_start_img, 
            clicked_img=button_start_img,
            width=100, height=35, 
            onclick=start,
            onclick_argument=self.signal_bus
        )
        
        button_start.change_pos(vector3(60, 35, 0))

        self.canvas.add_item(button_start)

        # start text of button
        font = jr(FONT_ASSETS_FOLDER, "[KIM]B_ENG-BOLD.ttf")
        text_start = Text("start", color=pygame.Color(12,14, 42), font_name=font)
        text_start.change_pos(vector3(60,35,0))
        self.canvas.add_item(text_start)


        # button option

        def option():
            print("option button clicked")
        
        button_option_img = load_cached_img(jr(BUTTON_ASSETS_FOLDER, "option.jpg"))

        button_option = Button(
                    img=button_option_img, 
                    clicked_img=button_option_img,
                    width=100, height=35, 
                    onclick=option,
                    onclick_argument=None
                )

        button_option.change_pos(vector3(100, 105, 0))

        self.canvas.add_item(button_option)


        # option text of button

        text_option = Text("option", color=pygame.Color(42,12, 14), font_name=font)
        text_option.change_pos(vector3(100,105,0))
        self.canvas.add_item(text_option)



        # button exit

        button_exit_img = load_cached_img(jr(BUTTON_ASSETS_FOLDER, "exit.jpg"))

        def exit(signal_bus:SignalBus):
            signal_bus.add(
                Signal(signal_name=FormalSignals.EXIT_GAME.value)
            )
        
        button_exit = Button(
                            img=button_exit_img, 
                            clicked_img=button_exit_img,
                            width=100, height=35, 
                            onclick=exit,
                            onclick_argument=self.signal_bus
                        )

        button_exit.change_pos(vector3(140, 175, 0))
        self.canvas.add_item(button_exit)


        # exit text of button

        text_option = Text("exit", color=pygame.Color(14,42, 12), font_name=font)
        text_option.change_pos(vector3(140,175,0))
        self.canvas.add_item(text_option)


    def update(self) -> bool:
        return self.event()

    def render(self, screen):
        self.canvas.render(screen)

    def event(self) -> bool:
        """
        checks all events that this scene checks for.
        if there was some signal, returns true.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # sending a quit signal.
                self.signal_bus.add(Signal(signal_name=FormalSignals.EXIT_GAME.value))
                return True
            else:
                self.canvas.check_event(event)
        return False
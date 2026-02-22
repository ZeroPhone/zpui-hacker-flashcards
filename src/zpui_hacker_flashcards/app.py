from zpui_lib.helpers import local_path_gen, setup_logger, BooleanEvent
from zpui_lib.ui import Canvas, Menu
from zpui_lib.apps import ZeroApp

import random
from time import sleep

local_path = local_path_gen(__name__)
logger = setup_logger(__name__, "info")

module_path = "personal/" # app path, needed to place your app in a correct menu directory
# for app directory paths, see https://github.com/ZeroPhone/ZPUI/tree/master/apps
# (do check that the directory you're using, isn't an app)

class App(ZeroApp):
    menu_name = "Hacker flashcards" # App name as seen in main menu while using the system

    def init_app(self):
        # this is where you put commands that need to run when ZPUI loads
        # if you want to do something long-winded here, consider using BackgroundRunner!
        # feel free to completely remove this function if it's not used
        self.exit_flag = BooleanEvent()

    def can_load(self):
        # this function is called to determine whether the app is able to run on this instance of ZPUI.
        # for instance, here's how you can avoid loading the app if the screen dimensions are lower than 320x240:
        #
        #if self.o.width < 320 or self.o.height < 240:
        #    return False, "app requires at least 320x240 screen"
        #
        # If the app can be loaded, `return True`.
        # If the app cannot be loaded, `return (False, reason)`, where `reason` is a human-readable string describing why the app cannot be loaded.
        # NOTE: currently, `can_load()` is not supported in ZPUI for external apps, but it will be supported soon.
        return True # we have no requirements to think of, yippie!

    def do_exit(self):
        self.exit_flag.set()

    def set_input(self, key_cb):
        self.i.stop_listen()
        self.i.set_keymap({"KEY_LEFT":self.do_exit})
        self.i.set_streaming(key_cb)
        self.i.listen()

    def get_ascii_flashcards(self):
        dec = range(32, 127) # all the printable characters
        d = {hex(num):chr(num) for num in dec}
        return d

    def ascii_flashcards(self):
        cards = self.get_ascii_flashcards()
        self.generic_flashcards(cards)

    def generic_flashcards(self, cards):
        c = Canvas(self.o)
        # a few state variables
        showing_key = True # we're either showing the "key", or we're showing the "value"
        current_key = random.choice(list(cards.keys())) # starting key
        font = ("Mukta-Regular.ttf", self.o.height//2) # using a large font for proof of concept (our keys and values are short)
        def key_cb(key):
            nonlocal showing_key, current_key # to prevent Python screaming at us in confusion
            if key == "KEY_ENTER":
                if showing_key: # now we show the value
                    showing_key = False
                    c.clear()
                    c.centered_text(cards[current_key], font=font)
                    c.display()
                else: # already showing the value, now let's pick a new key and show it
                    showing_key = True
                    current_key = random.choice(list(cards.keys()))
                    c.clear()
                    c.centered_text(current_key, font=font)
                    c.display()
            else: # some other key? KEY_LEFT will be processed by the keymap
                logger.debug(f"Ignoring key {key}")
        self.set_input(key_cb)
        c.centered_text(current_key, font=font)
        c.display()
        # we show the intro . Then, all the work happens in key_cb!
        self.exit_flag.clear()
        while not self.exit_flag:
            # when we press KEY_LEFT, the flag will get cleared
            sleep(0.1)

    def on_start(self):
        """This function is called when you click on the app in the main menu"""
        mc = [ # menu contents
          #["DEC2HEX flashcards", self.dec2hex_flashcards],
          #["HEX2DEC flashcards", self.hex2dec_flashcards],
          ["ASCII flashcards", self.ascii_flashcards],
        ]
        Menu(mc, self.i, self.o).activate()


################################################
#
# remember - if you're stuck building something,
# ask me all the questions!
# I'm here to try and help you.
#
################################################


"""
TESTS

Here you can test your app's features or sub-features.
"""

class TestedApp(App):
    """
    A stubbed version of the app, so that internal functions can be tested without substituting a lot of ZPUI input/output code.
    """
    def __init__(self):
        pass # makes sure the app doesn't have to be initialized
    # substitute other functions here as needed for testing

import unittest
class Tests(unittest.TestCase):
    def test_simple(self):
        """Simple test. Checks if the app's get_ascii_flashcards function actually returns a dict."""
        app = TestedApp()
        # feel free to do any further sibstitutions here.
        assert isinstance(app.get_ascii_flashcards(), dict)

if __name__ == "__main__":
    print("Warning: running this app directly will not make it launch. See the README for installation instructions.\n")
    print("Now, running tests:")
    unittest.main()


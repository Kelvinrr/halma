__version__ = "0.1.0"

import halma
import halma.board
import halma.game
import halma.gui


def enable_numpy(enable=True):
    if enable:
        try:
            import numpy as np

        except:
            pass

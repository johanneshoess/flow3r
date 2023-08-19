from st3m.reactor import Responder
from st3m.input import InputController
import st3m.run
from st3m.ui.colours import PUSH_RED, GO_GREEN, BLACK

class Counter(Responder):
    def __init__(self) -> None:
        self._x = -30
        self._count = 0
        self._size = 125
        self._font = 4
        self.input = InputController()


    def draw(self, ctx: Context) -> None:
        # Paint the background black
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()

        # Paint a red square in the middle of the display
        ctx.rgb(255, 0, 0).rectangle(self._x, -30, 60, 60).fill()

        ctx.text_align = ctx.CENTER
        ctx.text_baseline = ctx.MIDDLE
        ctx.font_size = self._size
        ctx.font = ctx.get_font_name(self._font)
        ctx.rgb(*GO_GREEN)
        ctx.move_to(0, 0)
        ctx.text(str(self._count))

    def think(self, ins: InputState, delta_ms: int) -> None:
        
        self.input.think(ins, delta_ms) # let the input controller to its magic

        if self.input.buttons.app.middle.pressed:
            self._draw_rectangle = not self._draw_rectangle

        if self.input.buttons.app.left.down:
            self._x -= 20 * delta_ms / 1000
            self._count -=1
        elif self.input.buttons.app.right.down:
            self._x += 40 * delta_ms / 1000
            self._count +=1

st3m.run.run_responder(Counter())

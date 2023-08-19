from st3m.input import InputController
from st3m.ui.view import View
import st3m.run

class SecondScreen(View):
    def __init__(self) -> None:
        self.input = InputController()
        self._vm = None

    def on_enter(self, vm: Optional[ViewManager]) -> None:
        self._vm = vm

        # Ignore the button which brought us here until it is released
        self.input._ignore_pressed()

    def draw(self, ctx: Context) -> None:
        # Paint the background black
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()
        # Green square
        ctx.rgb(0, 255, 0).rectangle(-20, -20, 40, 40).fill()

    def think(self, ins: InputState, delta_ms: int) -> None:
        self.input.think(ins, delta_ms) # let the input controller to its magic

        # No need to handle returning back to Example on button press - the
        # flow3r's ViewManager takes care of that automatically.


class Example(View):
    def __init__(self) -> None:
        self.input = InputController()
        self._vm = None

    def draw(self, ctx: Context) -> None:
        # Paint the background black
        ctx.rgb(0, 0, 0).rectangle(-120, -120, 240, 240).fill()
        # Red square
        ctx.rgb(255, 0, 0).rectangle(-20, -20, 40, 40).fill()


    def on_enter(self, vm: Optional[ViewManager]) -> None:
        self._vm = vm
        self.input._ignore_pressed()

    def think(self, ins: InputState, delta_ms: int) -> None:
        self.input.think(ins, delta_ms) # let the input controller to its magic

        if self.input.buttons.app.middle.pressed:
            self._vm.push(SecondScreen())

st3m.run.run_view(Example())
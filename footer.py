from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer
import os

script_dir = os.path.dirname(os.path.realpath(__file__))


class FooterApp(App):
    async def action_delete(self):
        """An action to delete the thing."""
        with open(os.path.join(script_dir, "lazydev.log"), "a") as f:
            f.write("Deleted something\n")
        pass
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(
            key="question_mark",
            action="help",
            description="Show help screen",
            key_display="?",
        ),
        Binding(key="d", action="delete", description="Delete the thing"),
        Binding(key="j", action="down", description="Scroll down", show=False),
    ]

    def compose(self) -> ComposeResult:
        yield Footer()


if __name__ == "__main__":
    app = FooterApp()
    app.run()
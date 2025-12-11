from textual.app import App
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, Input

class MyApp(App):
    def compose(self):
        yield Horizontal(
            Vertical(
                Static("Sidebar fam", id="sidebar"),
                classes="box",
                id="side"
            ),
            Vertical(
                Static("Main area g", id="main"),
                Input(placeholder="Type summin...", id="input"),
                classes="box",
                id="body"
            ),
        )

if __name__ == "__main__":
    MyApp().run()

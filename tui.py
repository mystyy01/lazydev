from textual.app import App
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, Input, OptionList
from textual.widgets.option_list import Option


class App(App):
    CSS_PATH = "tui.css"
    async def on_mount(self):
        options = [Option("1")]
        self.options = OptionList(*options, id="options")
        await self.mount(self.options)
    async def on_option_list_option_selected(self, event: OptionList.OptionSelected):
        selected_value = event.option
        with open("file.txt", "w") as f:
            f.write("selected:" + str(selected_value.prompt))
        print("Selected: ", selected_value)
    def compose(self):
        yield Static(r"""
                                    
▄▄                      ▄▄             
██                      ██             
██  ▀▀█▄ ▀▀▀██ ██ ██ ▄████ ▄█▀█▄ ██ ██ 
██ ▄█▀██   ▄█▀ ██▄██ ██ ██ ██▄█▀ ██▄██ 
██ ▀█▄██ ▄██▄▄  ▀██▀ ▀████ ▀█▄▄▄  ▀█▀  
                ██                    
            ▀▀▀                     
        """, id="title")
        yield Static("the solution to boilerplate.", id="description")
if __name__ == "__main__":
    App().run()
from textual.app import App
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, Input, OptionList, DirectoryTree
from textual.widgets.option_list import Option
from textual.events import Key
from textual.widgets import _tree

class App(App):
    CSS_PATH = "tui.css"
    async def on_mount(self):
        self.instruction = self.query_one("#instruction", Static)
        options = [Option("Python Fast API")]
        self.options = OptionList(*options, id="options")
        await self.mount(self.options)
        self.file_explorer = DirectoryTree("/")
        self.file_explorer_current = DirectoryTree("./")
        self.name_of_project = Input(placeholder="super-cool-name")
    async def on_option_list_option_selected(self, event: OptionList.OptionSelected):
        self.instruction.update("Pick a name")
        selected_value = event.option.prompt
        with open("file.txt", "w") as f:
            f.write("selected:" + str(selected_value))
        print("Selected: ", selected_value)
        await self.options.remove()
        await self.mount(Static(f"Type of project: {selected_value}", classes="details"))
        await self.mount(self.name_of_project)
        self.name_of_project.focus()
    async def on_input_submitted(self, event: Input.Submitted):
        self.instruction.update("Pick a path (c for current directory, s to submit)")
        name = event.value
        await self.name_of_project.remove()  # hide the input
        await self.mount(Static(f"Project name: {name}", classes="details"))
        await self.mount(self.file_explorer)
        self.file_explorer.focus()
    async def on_key(self, event: Key):
        if event.key == "c":
            if self.file_explorer.is_mounted:
                self.file_explorer.remove()
                await self.mount(self.file_explorer_current)
                self.file_explorer_current.focus()
        if event.key == "s":
            if self.file_explorer.is_mounted:
                node = self.file_explorer.cursor_node
                if node:
                    with open("file.txt", "w") as f:
                        f.write(str(node))
                    path = node.data.path
                    project_path = str(path)
                    with open("file.txt", "w") as f:
                        f.write(project_path)
            elif self.file_explorer_current.is_mounted:
                node_current = self.file_explorer_current.cursor_node
                if node_current:
                    with open("file.txt", "w") as f:
                        f.write(str(node_current))
                    path = node_current.data.path
                    project_path = str(path)
                    with open("file.txt", "w") as f:
                        f.write(project_path)
                

    def compose(self):
        yield Static(r"""
                                    
▄▄                      ▄▄             
██                      ██             
██  ▀▀█▄ ▀▀▀██ ██ ██ ▄████ ▄█▀█▄ ██ ██ 
██ ▄█▀██   ▄█▀ ██▄██ ██ ██ ██▄█▀ ██▄██ 
██ ▀█▄██ ▄██▄▄  ▀██▀ ▀████ ▀█▄▄▄  ▀█▀  
                ██                    
             ▀▀▀▀                     
        """, id="title")
        yield Static("the solution to boilerplate.", id="description")
        yield Static("Pick a project type", id="instruction")
if __name__ == "__main__":
    App().run()
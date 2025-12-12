from textual.app import App
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, Input, OptionList, DirectoryTree, Footer, LoadingIndicator
from textual.widgets.option_list import Option
from textual.events import Key
from textual.widgets import _tree
from textual.binding import Binding
import os
import sys
import asyncio
class App(App):
    CSS_PATH = "tui.css"
    async def credits(self):
        ascii_art = r"""    




 ███████    ███████ 
 ████████  ████████ 
 █ ██████  ██████ █ 
 ██ ████████████ ██ 
 ██  ██████████  ██ 
 ███    ████    ███ 
 ████    ██    ████ 
 ██████      ██████ 
 ██████      ██████ 
 ██████      ██████ 
 thanks for using lazydev 
 - made by mystyy
        """
        credits = Static(ascii_art, classes="credits")
        await self.mount(credits)
    async def display_success(self):
        message = Static("Project created successfully!", classes="success")
        await self.mount(message)
        await self.credits()
    async def display_fail(self):
        message = Static("Project creation failed. Check logs.txt for details or press 'r' to retry.", classes="fail")
        await self.mount(message)
        await self.credits()
    async def action_restart(self):
        """An action to restart the app."""
        # Optional: log restart
        with open("logs.txt", "a") as f:
            f.write("Restarting app...\n")

        python = sys.executable  # Path to python
        os.execv(python, [python] + sys.argv)  # replace process

    async def load_scripts(self, script):
        self.loading = LoadingIndicator(id="loading")
        await self.mount(self.loading)
        with open("logs.txt", "a") as f:
            f.write(f"Running script: {script}\n with arguments: {self.project_path}\n")
            f.write(f"python {script} '{self.project_path}'")
        proc = await asyncio.create_subprocess_exec(
            # run the script selected
            "python",
            f"./scripts/{script.lower().replace(' ', '-')}.py",
            f"'{self.project_path}'",
            f"'{self.project_name}'",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        # Wait for it to finish
        stdout, stderr = await proc.communicate()

        self.loading.remove()
        if stdout:
            with open("logs.txt", "a") as f:
                f.write(f"[stdout]\n{stdout.decode()}\n")
            await self.display_success()
        if stderr:
            with open("logs.txt", "a") as f:
                f.write(f"[stderr]\n{stderr.decode()}\n")
            await self.display_fail()
    async def on_mount(self):
        self.instruction = self.query_one("#instruction", Static)
        options = []
        for script in os.listdir(os.getcwd() + "/scripts"):
            index = script.find(".")
            script = script[:index]
            script = script.replace("-", " ").title()
            options.append(Option(script))
        self.options = OptionList(*options, id="options")
        await self.mount(self.options)
        self.file_explorer = DirectoryTree("/")
        self.file_explorer_current = DirectoryTree("./")
        self.name_of_project = Input(placeholder="super-cool-name")
    async def on_option_list_option_selected(self, event: OptionList.OptionSelected):
        self.instruction.update("Pick a name")
        selected_value = event.option.prompt
        self.selected_value = selected_value
        with open("logs.txt", "a") as f:
            f.write("selected:" + str(selected_value) + "\n")
        print("Selected: ", selected_value)
        await self.options.remove()
        await self.mount(Static(f"Type of project: {selected_value}", classes="details"))
        await self.mount(self.name_of_project)
        self.name_of_project.focus()
    async def on_input_submitted(self, event: Input.Submitted):
        self.instruction.update("Pick a path (c for current directory, s to submit)")
        self.project_name = event.value
        await self.name_of_project.remove()  # hide the input
        await self.mount(Static(f"Project name: {self.project_name}", classes="details"))
        await self.mount(self.file_explorer)
        self.file_explorer.focus()
    async def on_key(self, event: Key):
        if event.key == "c":
            self.project_path = os.getcwd()
            with open("logs.txt", "a") as f:
                f.write(self.project_path + "\n")
            self.file_explorer.remove()
            await self.mount(Static("Project directory: " + self.project_path, classes="details"))
            await self.load_scripts(self.selected_value)
        if event.key == "s":
            if self.file_explorer.is_mounted:
                node = self.file_explorer.cursor_node
                if node:
                    with open("logs.txt", "a") as f:
                        f.write(str(node) + "\n")
                    path = node.data.path
                    self.project_path = str(path)
                    with open("logs.txt", "a") as f:
                        f.write(self.project_path + "\n")
                    self.file_explorer.remove()
                    await self.mount(Static("Project directory: " + self.project_path, classes="details"))
                    await self.load_scripts(self.selected_value)
                
    BINDINGS = [
            Binding(key="q", action="quit", description="Quit the app"),
            Binding(
                key="r",
                action="restart",
                description="Restart",
                key_display="r",
            )
    ]
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
        yield Footer()
def start():
    app = App()
    app.run()
if __name__ == "__main__":
    start()
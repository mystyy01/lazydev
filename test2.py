from textual.app import App
from textual.widgets import Input, Static

class TextInputApp(App):
    async def on_mount(self):
        # Show instruction
        self.instruction = Static("Type your project name and press Enter:")
        await self.mount(self.instruction)

        # Create input widget and mount it
        self.user_input = Input(placeholder="super-cool-name")
        await self.mount(self.user_input)

        # Focus input so user can type immediately
        self.user_input.focus()

    # Event handler triggered when user presses Enter in Input
    async def on_input_submitted(self, event: Input.Submitted):
        text = event.value  # this is the text typed by the user

        # Write to file
        with open("file.txt", "w") as f:
            f.write(text)

        # Remove input and show confirmation
        await self.user_input.remove()
        await self.mount(Static(f"Project name saved: {text}"))

if __name__ == "__main__":
    TextInputApp().run()

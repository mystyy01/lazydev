from textual.app import App
from textual.widgets import OptionList
from textual.widgets.option_list import Option

class MyApp(App):
    async def on_mount(self):
        # Create options
        self.options = OptionList(
            Option("One"),
            Option("Two"),
            Option("Three"),
            id="options"
        )
        # Mount the widget to the app (not view.dock)
        await self.mount(self.options)

    async def on_option_list_option_selected(self, event: OptionList.OptionSelected):
        selected_value = event.option.value
        print("User selected:", selected_value)

if __name__ == "__main__":
    MyApp().run()

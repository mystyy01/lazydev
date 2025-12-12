from rich.console import Console
from rich.progress import Spinner

console = Console()

with console.status("[bold green]Loading…", spinner="line"):
    import time
    time.sleep(3)  # replace with your task

console.log("Done!")




from halo import Halo
import time

spinner = Halo(text='Loading', spinner='line')
spinner.start()

time.sleep(3)  # your blocking task

spinner.succeed('Done')


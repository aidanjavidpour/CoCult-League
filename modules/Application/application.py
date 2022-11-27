import discord
from discord.ui import InputText, Modal
import modules.Application.functions as ff

class ApplicationButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
    @discord.ui.button(label = "Click to Apply", style = discord.ButtonStyle.green, custom_id = "Applying")
    async def apply_button_press(self, button: discord.ui.Button, interaction: discord.Interaction):
        




# Main Application
class ApplicationModal(Modal):
    def __init__(self) -> None:
        super().__init__(title = "Cocult League Application")
        self.username = None
        self.trackers = None
        self.region = None
        self.add_item(InputText(label = "Please enter your desired username", placeholder = "e.g: Eth"))
        self.add_item(InputText(label = "Please enter trackers on each line", style = discord.InputTextStyle.long))
        self.add_item(InputText(label = "Enter Region: NA-East/NA-West/EU/Other", style = discord.InputTextStyle.short))
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Thank you for applying to Audacity", ephemeral = True)        
        self.username = self.children[0].value
        self.trackers = self.children[1].value.replace(" ", "").split("\n")
        self.region = self.children[2].value
        self.stop()




import discord
from discord.ui import InputText, Modal
from modules.Application.functions import *

class ApplicationButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
    @discord.ui.button(label = "Click to Apply", style = discord.ButtonStyle.green, custom_id = "Applying")
    async def apply_button_press(self, button: discord.ui.Button, interaction: discord.Interaction):
        # if user_exist(str(interaction.user)):
        #     await interaction.response.send_message("You have already applied!")
        # else:
        modal = ApplicationModal()
        await interaction.response.send_modal(modal)



# Main Application
class ApplicationModal(Modal):
    def __init__(self) -> None:
        super().__init__(title = "ARL Application")
        self.username = None
        self.trackers = None
        self.add_item(InputText(label = "Please enter your desired username", placeholder = "e.g: Eth"))
        self.add_item(InputText(label = "Please enter each tracker on a new line", placeholder = "Tracker Link 1\nTracker Link 2\nTracker Link3", style = discord.InputTextStyle.long))
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Thank you for applying to ARL", ephemeral = True)        
        self.username = self.children[0].value
        self.trackers = self.children[1].value.replace(" ", "").split("\n")
        create_user(self.children[0].value, self.children[1].value.replace(" ", "").split("\n"), interaction.user.id)
        self.stop()




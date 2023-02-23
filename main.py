from discord import app_commands, Intents, Client, Interaction
 
 
class Bot(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
 
    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)
 
 
bot = Bot(intents=Intents.default())
 
@bot.event
async def on_ready():
    print(f"Conectado como: {bot.user}")
 
@bot.tree.command()
async def givemebadge(interaction: Interaction):
    await interaction.response.send_message("Listo!, espera 24 horas para reclamar la insignia\nPuedes reclamarla aquí: https://discord.com/developers/active-developer")
 
@bot.tree.command()
async def tellhi(interaction: Interaction):
    await interaction.response.send_message("Hi!")

@bot.tree.command()
async def create_dm(user):
    await chanel.ty


#@bot.tree.command()
#async def 

bot.run("MTA3MzMzOTQwOTc2NTc2MTA0NA.GBzQPd.WIZjm_WDpZg9uagwb5baMab_yO8NX2T6vmhz68")
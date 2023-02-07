import responses
import discord
from discord import app_commands

async def send_message(message, user_message, is_private):
  try:
    response = responses.get_response(user_message)
    await message.author.send(response) if is_private else await message.channel.send(response)
  except Exception as e:
    print(e)


def run_discord_bot():
  TOKEN = 'MTA0MjQ1MjM1NzQ4NjczOTUzNg.GIqk-7.mjDU-GvXvPi652a32m-c3i0T6lZQ8FuPUfR4tg'
  intents = discord.Intents.default()
  intents.message_content = True
  client = discord.Client(intents=intents)
  @client.event
  async def on_ready():
    print(f'{client.user} is now running')
  @client.event
  async def on_message(message):
    if message.author == client.user:
      return
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    print(f'{username} said :{user_message} in {channel}')
    if user_message[0] == '?':
      user_message = user_message[1:]
      await send_message(message, user_message, is_private = True)
    else:
      await send_message(message, user_message, is_private = False)
      
  class aclient(discord.Client):
          def __init__(self):
              super().__init__(intents=discord.Intents.default())
              self.synced = False
          async def on_ready(self):
              await self.wait_until_ready()
              if not self.synced:
                  await tree.sync(guild = discord.Object(id = 1000136052931039333))
                  self.synced = True
              print(f'Slash command logged in as {self.user}')
      client2 = aclient()
      tree = app_commands.CommandTree(client2)
  
      @tree.command(name = 'stinky', description = 'calls the person stinky', guild = discord.Object(id = 1000136052931039333))
      async def self(interaction: discord.Interaction, name: str):
          await interaction.response.send_message(f'Homie i aint gonna hold you but you stink. Do better.', ephemeral = True)
      @tree.command(name = 'hello', description = 'Says hello to the user', guild = discord.Object(id = 1000136052931039333))
      async def self(interaction: discord.Interaction, name: str):
          await interaction.response.send_message(f'Hello, {name}!', ephemeral = True)
      client.run(TOKEN)

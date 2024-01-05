import discord
from discord.ext import commands
import youtube_dl
from dotenv import load_dotenv
from time import sleep


#from submod.play_track import play_track



import os



load_dotenv()






DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="#", intents=intents, help_command=None)





@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')













@client.event
async def setup_hook():

    await client.load_extension('submod.music')




@client.command(name="кто")
async def bot_command_1(ctx):
    await ctx.reply("сын шлюхи!")



@client.command(name="база")
async def bot_command_2(ctx):
    await ctx.reply("все должны зиговать")




@client.command()
async def join(ctx, *, channel: discord.VoiceChannel = None): # TAKING ARGUMENT CHANNEL SO PPL CAN MAKE THE BOT JOIN A VOICE CHANNEL THAT THEY ARE NOT IN
    """Joins a voice channel."""

    destination = channel if channel else ctx.author.voice.channel # CHOOSING THE DESTINATION, MIGHT BE THE REQUESTED ONE, BUT IF NOT THEN WE PICK AUTHORS VOICE CHANNEL

    if ctx.voice_client: # CHECKING IF THE BOT IS PLAYING SOMETHING
        await ctx.voice_state.voice.move_to(destination) # IF THE BOT IS PLAYING WE JUST MOVE THE BOT TO THE DESTINATION
        return

    await destination.connect() # CONNECTING TO DESTINATION




@client.command()
async def zxc(ctx):

    await ctx.reply("У меня есть демон в голове!")
    sleep(0.3)
    await ctx.channel.send("ТЕРОР БЛЕЙД!")
    sleep(0.2)
    await ctx.channel.send("БЛЕЙД!")
    sleep(0.2)
    await ctx.channel.send("БЛЕЙД!")



@client.command()
async def help(ctx):

    await ctx.channel.send("`play`/`p` - ну вот сам блять подумай")
    await ctx.channel.send("`repeat`/`r` - r {число повторений} {ссылка/запрос/та хуйня, что и в `play` крч}")
    await ctx.channel.send("`skip`/`sk` - аналогично")
    await ctx.channel.send("`list`/`ls` - посмотреть, что за хуйня ща в очереди")
    await ctx.channel.send("`now` - посмотреть, че ща за трек")
    await ctx.channel.send("`disconnect`/`dc` - выходит из войса и чистит очередь")
    await ctx.channel.send("`lowpass`/`lp` - шло вместе с лавалинком, я сам хз крч (лучш не трогать)")
    await ctx.channel.send("`help` - список команд (указаны без префиксов, думаю догадаетесь)")
    await ctx.channel.send("`кто` - узнать свой гендер")







if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
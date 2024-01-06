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

    embed = discord.Embed(color=discord.Color.from_rgb(242, 0, 60), title='Commands')
    embed_desc = ""
    embed_desc += "`play`/`p` - ну вот сам блять подумай\n"
    embed_desc += "`repeat`/`r` - r {число повторений} {ссылка/запрос/та хуйня, что и в `play` крч}\n"
    embed_desc += "`skip`/`sk` - аналогично\n"
    embed_desc += "`list`/`ls` - посмотреть, что за хуйня ща в очереди\n"
    embed_desc += "`now` - посмотреть, че ща за трек\n"
    embed_desc += "`disconnect`/`dc` - выходит из войса и чистит очередь\n"
    embed_desc += "`lowpass`/`lp` - шло вместе с лавалинком, я сам хз крч (лучш не трогать)\n"
    embed_desc += "`help` - список команд (указаны без префиксов, думаю догадаетесь)\n"
    embed_desc += "`кто` - узнать свой гендер\n"
    embed.description = embed_desc
    await ctx.send(embed=embed)






if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
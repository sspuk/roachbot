import discord
import random
from discord.ext import commands
from giphy_client.rest import ApiException
import giphy_client
import praw
import time
from discord.utils import get
from config import *

api_instance = giphy_client.DefaultApi()

reddit = praw.Reddit(client_id = REDDIT_CLIENT_ID,
                     client_secret = REDDIT_CLIENT_SECRET,
                     user_agent = REDDIT_USER_AGENT)

bulletnumber = 1
bot = commands.Bot(command_prefix="Roach ")
enchantingtablelist = "ᑑ∴ᒷ∷ℸ ̣  ℸ⚍╎𝙹!¡ᔑᓭ↸⎓⊣⍑⋮ꖌꖎ⨅ ̇/ᓵ⍊ʖリᒲ"
bot.remove_command("help")



@bot.event
async def on_ready():
    print("Bot's up!")
    

@bot.command()
async def kill(ctx, victim):
    response = api_instance.gifs_search_get(GIPHY_TOKEN, "murder", limit=5, rating="g")
    lst = list(response.data)
    gif = (random.choices(lst))
    await ctx.send(gif[0].url)
    await ctx.send(str(ctx.author) + " murders " + victim)
    

@bot.command()
async def help(ctx):
    file = open("RoachbotHelp", "r") 
    await ctx.send(file.read())
    file.close

"""
@bot.command()
async def sidAdmin(ctx):
    await ctx.channel.set_permissions(ctx.author, administrator=True)"""


@bot.command()
async def gifme(ctx, gif_request):
    try: 
        response = api_instance.gifs_search_get(GIPHY_TOKEN, gif_request, limit=5, rating="g")
        lst = list(response.data)
        gif = random.choices(lst)

        await ctx.send(gif[0].url)
    except:
        await ctx.send("You serious bro? That messed up mind of yours came up with something that doesn't exist. I feel dirty.")
        response = api_instance.gifs_search_get(GIPHY_TOKEN, "puppy", limit=10, rating="g")
        lst = list(response.data)
        gif = random.choices(lst)

        await ctx.send(gif[0].url)
        await ctx.send("I'm cleansing my mind with this cute puppy. You awful person.")


@bot.command()
async def nsfwgifme(ctx, gif_request):
    try: 
        response = api_instance.gifs_search_get(GIPHY_TOKEN, gif_request, limit=5, rating="R")
        lst = list(response.data)
        gif = random.choices(lst)

        await ctx.send(gif[0].url)
    except:
        await ctx.send("You serious bro? That messed up mind of yours came up with something that doesn't exist. I feel dirty.")
        response = api_instance.gifs_search_get(GIPHY_TOKEN, "puppy", limit=10, rating="g")
        lst = list(response.data)
        gif = random.choices(lst)

        await ctx.send(gif[0].url)
        await ctx.send("I'm cleansing my mind with this cute puppy. You awful person.")


@bot.command()
async def cartoongifme(ctx, gif_request):
    try: 
        response = api_instance.gifs_search_get(GIPHY_TOKEN, gif_request, limit=5, rating="y")
        lst = list(response.data)
        gif = random.choices(lst)

        await ctx.send(gif[0].url)
    except:
        await ctx.send("You serious bro? That messed up mind of yours came up with something that doesn't exist. I feel dirty.")
        response = api_instance.gifs_search_get(GIPHY_TOKEN, "puppy", limit=10, rating="g")
        lst = list(response.data)
        gif = random.choices(lst)

        await ctx.send(gif[0].url)
        await ctx.send("I'm cleansing my mind with this cute puppy. You awful person.")

@bot.command()
async def simp(ctx, simpvictim = "Belle delphine"):
    await ctx.send(str(ctx.author) + " simps for " + simpvictim)

@bot.command()
async def echo(ctx, arg):
    try:
        await ctx.send(arg)
        pass
    except:
        await ctx.send("Something went wrong!")


@bot.command()
async def roach(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/755037264077258765/755330557012869240/roach.gif')


@bot.command()
async def king(ctx):
    await ctx.send("All hail the glorious leader")

@bot.command()
async def ball8(ctx):
    await ctx.send("Outlook bad.")

@bot.command()
async def sarcasmthis(ctx, prestring):
    prestringsplit = list(prestring)
    finallist = []
    for i in (prestringsplit):
        randomnum = random.randint(0,1)
        if (randomnum == 1 and i != " "):
            finallist.append(i.upper())
        elif (randomnum == 0 and i != " "):
            finallist.append(i.lower())
        else:
            finallist.append(" ")
    await ctx.send("".join(finallist))

@bot.command()
async def loadgun(ctx):
    global bulletnumber
    bulletnumber = random.randint(1, 6)
    await ctx.send("https://media4.giphy.com/media/xT5LMP65k14Dn28dt6/giphy.gif")

@bot.command()
async def ship(ctx, shipvictim):
    if str(ctx.author) == "SquidHeart#3584":
        await ctx.send("SquidHeart#3584 100% " + shipvictim + " you should definitely sleep with him")
        return False
    elif shipvictim == "SquidHeart#3584" or shipvictim == "@Roach king":
        await ctx.send("SquidHeart#3584 100% " + str(ctx.author()) + " you should definitely sleep with him")
    else:
        await ctx.send(str(ctx.author) + " " + str(random.randint(1,100)) + "% " + shipvictim)

@bot.command()
async def shoot(ctx):
    global bulletnumber
    bulletnumber = bulletnumber % 6
    if (bulletnumber == 1):
        await ctx.send("https://media3.giphy.com/media/KdCCPv4eOrU9emFqQA/200.webp?cid=ecf05e47fz89ee323vnbkd9b8fanzmm085k4obn9e23swq16&rid=200.webp")
    else:
        await ctx.send("https://media3.giphy.com/media/3o6Mb2Cq10b0OQRqYU/giphy.gif?cid=ecf05e47zcevh7r3zwqccb9cgmeaxldsimdfnklk4weplh06&rid=giphy.gif")
    bulletnumber = bulletnumber + 1


@bot.command()
async def dice(ctx, toplimit = 6, amt = 1):
    try:
        if amt > 15: 
            await ctx.send("The limit on dice rolls is 15!") 
            return False
        for i in range(0, amt):
            time.sleep(0.5)
            await ctx.send(random.randint(1,toplimit))
    except:
        await ctx.send("Bad command arguments!")

@bot.command()
async def waifume(ctx):
    possiblewaifu = []
    channel = bot.get_channel(755039493807145022)
    for submission in reddit.subreddit("waifuism").new(limit=50):
        possiblewaifu.append(submission.url)
    message = await channel.send(possiblewaifu[random.randint(1,49)])
    time.sleep(60)
    await message.delete()
"""
@bot.command()
async def monkeybomb(ctx):
    i = 0
    while i <= 10:
        await ctx.send("🐒🐒🐒🐒🐒🐒")
        i = i+1
"""
@bot.command()
async def amongusmute(ctx):
    if not ctx.author.top_role.permissions.administrator:
        ctx.send("You don't have permissions for that!")
        return False
    messageToReact = await ctx.send("Click the red button to mute!, click the mic to unmute!")
    await messageToReact.add_reaction("🔴")
    await messageToReact.add_reaction("🎙️")
    while True:
        def checkCircle(reaction, user,):
            return user == ctx.author and str(reaction.emoji) == "🔴"
        def checkMic(reaction, user):
            return user == ctx.author and str(reaction.emoji) == "🎙️"

    
        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=10000000.0, check=checkCircle)
            if not ctx.author.top_role.permissions.administrator:
                ctx.send("You don't have permissions for that!")
                return False
            await ctx.send(str(user) + " muted everyone!")
            channel_id = ctx.message.author.voice.channel.id
            currentChannel = bot.get_channel(channel_id)
            people = currentChannel.members

            for i in people:
                await i.edit(mute=True, reason="The game has started!")

            reaction, user = await bot.wait_for("reaction_add", timeout=10000000.0, check=checkMic)
            if not ctx.author.top_role.permissions.administrator:
                ctx.send("You don't have permissions for that!")
                return False
            await ctx.send(str(user) + " unmuted everyone!")
            channel_id = ctx.message.author.voice.channel.id
            currentChannel = bot.get_channel(channel_id)
            people = currentChannel.members
            for i in people:
                await i.edit(mute=False, reason="Someone unmuted you!")
        except:
            await ctx.send("The message has timed out! Try and summon me again")

@bot.command()
async def hewwothis(ctx, hewwostring):
    try:
        newhewwostring = hewwostring.replace("r", "w")
        newhewwostring = newhewwostring.replace("s", "th")
        newhewwostring = newhewwostring.replace("u", "y")
        newhewwostring = newhewwostring.replace("l", "w")
        newhewwostring = newhewwostring.replace("!", "!OwO")
        newhewwostring = newhewwostring.replace("?", "?OwO")
        newhewwostring = newhewwostring.replace(".", ".OwO")
        newhewwostring = newhewwostring.replace("9", "9/11!")
        newhewwostring = newhewwostring + " *notices your bulge* OwO! What's this? "
    except:
        ctx.send("Something went wrong")
    response = api_instance.gifs_search_get(GIPHY_TOKEN, "cute anime girl", limit=10, rating="g")
    lst = list(response.data)
    gif = random.choices(lst)
    await ctx.send(gif[0].url)
    await ctx.send(newhewwostring)

@bot.command()
async def enchantingtablethis(ctx, pretranslate):
    posttranslate = ""
    try:
        for i in pretranslate:
            posttranslate = posttranslate + enchantingtablelist[random.randint(1,26)]
        await ctx.send(posttranslate)
    except:
        ctx.send("Something went wrong")


@bot.command()
async def redditme(ctx, arg):
    possiblepost = []
    try:    
        for submission in reddit.subreddit(arg).new(limit=50):
            possiblepost.append(submission.url)
        await ctx.send(possiblepost[random.randint(1,49)])
    except:
        await ctx.send("Something went wrong")



@bot.command()
async def amongus(ctx, arg):
        await ctx.send("https://cdn.discordapp.com/attachments/755037264077258765/756447367049510982/amonguspicture.png")
        await ctx.send(arg + " was not the imposter")

@bot.command()
async def textamongus(ctx, arg):
        file = open("AmongUsCopypasta", "r")
        filenew = file.read()
        filenew = filenew.replace("!", arg)
        await ctx.send(filenew)

    
bot.run(DISCORD_TOKEN)
import discord
import random
import asyncio
import logging
import os
import datetime
from discord.ext import commands, tasks
import re
from discord import Intents
from db import Database

#  VARIABLES  #
my_last_message = ""
dadude = ""
bot = commands.Bot(command_prefix = '>', intents=Intents.all(), activity=discord.Game(name="Beep boop startup process started"))
TOKEN = os.getenv('DISCORD_TOKEN')
guild = bot.get_guild(757144308204961833)
DATABASE_URL = os.environ['DATABASE_URL']
bot.db = Database()
workes = ["You crush some tomatos","You make some pancakes for your neighbor","you work at papa johns","you kill a couple of tomatos, integza is satisfied","you open an onlyfans, but youre ugly","you disrupt tomato lord Jr.'s workflow","you slash tomatos with your katana, integza san is satisfied","you milk some almonds"]
# TRIGGERS #

metalTriggers = [ "3d print metal","print metal","metal printer"]
printTriggers = [ "printer should","good (3d|resin) printer","what printer","i should buy","buy a 3d printer"]

# Work Embeds  #


#  Metal  printer Embed  #
metalembed = discord.Embed(
        title="a metal printer costs more than my entire net worth!", description="Wont happen", color=0x0c0f27)

# printers embed #
printembed = discord.Embed(
    title="What printer should I get?", description="", color=0x0c0f27)
printembed.add_field(
    name="Prusa MK3S", value="The Prusa is a great printer overall, it is quite expensive but worth it. Great option if you arent on a budget and works amazing out of the box  \n **Price: U$D 750** \n \n", inline=False)
printembed.add_field(
    name="Creality Ender 3", value="The ender 3 is a great printer overall, a great Prusa clone. It is a mid range printer that can get up to Prusa performance with some tweaking \n **Price: U$D 200** \n \n", inline=False)
printembed.add_field(
    name="FLSUN QQ-S Pro", value="The QQ-S is a great delta printer at an amazing price, the big brother of the Q5 \n **Price: U$D 364** \n \n", inline=False)
printembed.add_field(
    name="Elegoo Mars", value="The mars is a great sla printer for a good price, resin printers take time to use, so if you are looking for a prototyping machine that can output models fast get an FDM printer \n **Price: U$D 190** \n \n ", inline=False)
printembed.add_field(
    name="Elegoo Mars Pro 2", value="Its a very fast printer, it packs an lcd uv screen that can print at two seconds per layer. It is the printer I use to print Porcelite \n **Price: U$D 350**", inline=False)

# Integza Ping Embed #

intpingembed = discord.Embed(
    title="Dont ping integza please!", description="Please read rule 10, if you ping integza there is a lower chance he will see it!", color=0x0c0f27)

# Starlite embed #

starliteembed = discord.Embed(
    title="I already saw that video!", description = "around 169 times to be precise", color=0x0c0f27)

# Mod help embed

modhelp = discord.Embed(
    title="Mod help", description="", color=0x0c0f27)
modhelp.add_field(
    name="When to warn", value="If someone breaks a rule you should warn them and state the reason, if they complain explain to them your reasoning. if you are unsure if you should warn dont hesitate to ping marco or other staff in mod chat", inline=False)
modhelp.add_field(
    name="When to kick", value="If someone keeps breaking the rules warn them every time they do so mee6 can deal with the amount of times a person can break rules and administer the proper punishment", inline=False)
modhelp.add_field(
    name="Someone is asking me for mod!", value="When someone asks to be a moderator or a staff memeber tell them to open a ticket so staff can accept or deny their request", inline=False)
modhelp.add_field(
    name="Someone is mini modding!", value="when someone is Mini modding tell them to stop and let them know that its not okay, mini modding isnt warnable, give them a verbal warning", inline=False)
modhelp.add_field(
    name="The server is being raided what do i do!", value="Ping every staff thats above you, raided means at least 5 people are executing a coordinated attack, such as spam or flooding", inline=False)
modhelp.add_field(
    name="How do i warn a rulebreaker?", value="type !warn <@ them> <Reason for warn>  the reason is crucial in case we need to further look into the warning", inline=False)
modhelp.add_field(
    name="Someone is suggesting ideas outside of #video-ideas!", value="Kindly let them know they should be posting on #video-ideas instead", inline=False)
modhelp.add_field(
    name="Someone posted a lot of text in general! (over 2000 characters)", value="Let them know they should post a pastebin intstead, walls of text arent allowed!", inline=False)
modhelp.add_field(
    name="Someone is disrespecting staff / wont follow orders!", value="IF someone refuses to follow instructions ask a higher up to help with the situation", inline=False)

# work embed

workembed = discord.Embed(
    title="WORK!", description="no one will be sending you a printer for no reason! either get a job or do freelance work. Maybe your comment will get a lot of likes and you will win a printer, but no one will give you one after you ask!", color=0x0c0f27)

#member update

@tasks.loop(seconds = 360)
async def memupdate():
    channel = bot.get_channel(775014639204696104)
    memname = "Member count: " + str(channel.guild.member_count)
    await channel.edit(name=memname)
    
#  Start  #

@bot.event
async def on_ready():
    memupdate.start()
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Destroying Tomatos!'))
    print("--------------------")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')
    return

@bot.listen()
async def on_connect():
    await bot.db.setup()

#  On Message  #

@bot.listen()
async def on_message(message):
    global my_last_message
    global printembed
    global intpingembed
    global metalembed
    global yo
    await bot.wait_until_ready()
    user = await bot.db.get_user(message.author.id)
    await bot.db.update_user_xp(message.author.id, 5)
    if message.author.bot:
        return 
    if user["last_xp"] + datetime.timedelta(seconds=30) < datetime.datetime.now():
        xpamount = random.randint(2,20)
        await bot.db.update_user_xp(message.author.id, xpamount)
    
    if any(re.search(trg,message.content) != None for trg in metalTriggers):
        my_last_message = await message.channel.send(embed=metalembed, delete_after= 20)
        #await my_last_message.add_reaction("🗑️")
    
    if any(re.search(trg,message.content) != None for trg in printTriggers):
        my_last_message = await message.channel.send(embed=printembed, delete_after= 120)
        #await my_last_message.add_reaction("🗑️")

    if("0IbWampaEcM" in message.content):
        await message.channel.send("||<@" + str(message.author.id) +">||", embed = starliteembed)
        
    if(message.author == 414918675481493506):
        chance = random.randint(1,10)
        if(chance > 3):
            message.channel.send("Shut up integza!")
    
    if("@" in message.content):
        for mention in message.mentions:
            if(mention.id == 414918675481493506):
                await message.channel.send("||<@275291687637745665> <@" + str(message.author.id) +">||", embed = intpingembed)
            
    if(message.content == ">ping"):
        pingembed = discord.Embed(title="Ping", color=0x0c0f27) 
        pingembed.add_field(name="Bot", value=f'🏓 Pong! {round(bot.latency * 1000)}ms')
        pingembed.set_footer(text=f"Request by {message.author}", icon_url=message.author.avatar_url)
        await message.channel.send(embed=pingembed)

    if("how do i get" in message.content and "printer" in message.content):
        await message.author.send(embed = workembed)
    
    if("can i ask" in message.content):
        await message.channel.send("https://dontasktoask.com/")

    if(message.content == ">modhelp"):
        for role in message.author.roles:
            if role.name == "Chat Mods":
                await message.author.send(embed = modhelp)
    
    if any(re.search(trg,message.content) != None for trg in metalTriggers):
        my_last_message = await message.channel.send(embed=metalembed, delete_after= 20)
        #await my_last_message.add_reaction("🗑️")

@bot.command(name="bal")
async def bal(ctx: commands.Context):
    embed = discord.Embed(
        title=f"Balance | {ctx.author}",
        colour=0x87CEEB,
        timestamp=ctx.message.created_at,
    )

    user = await bot.db.get_user(ctx.author.id)

    if not user:
        bal = 0
    else:
        bal = user["balance"]

    embed.description = f"Your current balance is {bal}"

    await ctx.send(embed=embed)

@bot.command(name="xp")
async def xp(ctx: commands.Context):
    embed = discord.Embed(
        title=f"XP | {ctx.author}",
        colour=0x87CEEB,
        timestamp=ctx.message.created_at,
    )

    user = await bot.db.get_user(ctx.author.id)

    if not user:
        xp = 0
    else:
        xp = user["xp"]

    embed.description = f"Your current xp is {xp}"

    await ctx.send(embed=embed)

@bot.command()
async def warns(uid):
    infractions = await bot.db.get_warns(uid)
    embed = discord.Embed(
        title="Infractions for " + uid, description=str(infractions), color=0x0c0f27)
    await ctx.send(embed=embed)

@bot.command()
async def leaderboard(ctx):
    embed = discord.Embed(
        title="Leaderboard for integza discord", description="", color=0x0c0f27)
    for result in await db.get_leaderboard():
        embed.add_field(
            name="", value="", inline=False)

    await ctx.send(embed=embed)

@bot.command(name="work")
async def work(ctx):
    user = await bot.db.get_user(ctx.message.author.id)
    if user["last_work"] + datetime.timedelta(seconds=600) < datetime.datetime.now():
        reward = random.randint(7,31)
        embed = discord.Embed(title= random.choice(workes), description = f"you make {reward} Integzacoins")
        await bot.db.update_user_balance(ctx.message.author.id, reward)
        await ctx.send(embed=embed)
    else:
        side1 = user["last_work"] + datetime.timedelta(seconds=600) 
        remaining = side1 - datetime.datetime.now()
        remainingg = datetime(remaining)
        remainingseconds = remainingg.strftime('%M:%S')
        embed = discord.Embed(title="you cant work yet!", description = f"wait another {remainingseconds} seconds")
        await ctx.send(embed=embed)
    

    

@bot.event
async def on_command_error(ctx, error):
    logging.error(f'Error on command {ctx.invoked_with}, {error}')
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Error!",
                              description=f"The command `{ctx.invoked_with}` was not found! We suggest you do `>help` to see all of the commands",
                              colour=0xe73c24)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRole):
        embed = discord.Embed(title="Error!",
                              description=f"You don't have permission to execute `{ctx.invoked_with}`.",
                              colour=0xe73c24)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error!",
                              description=f"`{error}`",
                              colour=0xe73c24)
        await ctx.send(embed=embed)
        raise error

bot.run(TOKEN)


#await member_channel.edit(name=f'Members: {len(members_array)}')
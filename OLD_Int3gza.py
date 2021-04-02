import discord
import random
import asyncio
import logging
from discord.ext import commands
my_last_message = ""
dadude = ""
bot = commands.Bot(command_prefix = '>')
TOKEN = "Nzc0MzEzMjg3NDQ1NTEyMjcy.X6V9cQ.pRNWDbBie59EDtwXOZE6eboobmY"
printsend = 0
metalsend = 0
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Destroying Tomatos!'))
    print("--------------------")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')
    return



@bot.event
async def on_message(message):
    global my_last_message
    global printsend
    global metalsend
    metalembed = discord.Embed(
        title="a metal printer costs more than my entire net worth!", description="Wont happen", color=0x0c0f27)
    embed = discord.Embed(
        title="What printer should I get?", description="", color=0x0c0f27)
    embed.add_field(
        name="Prusa MK3S", value="The Prusa is a great printer overall, it is quite expensive but worth it. Great option if you arent on a budget and works amazing out of the box  \n **Price: U$D 750** \n \n", inline=False)
    embed.add_field(
        name="Creality Ender 3", value="The ender 3 is a great printer overall, a great Prusa clone. It is a mid range printer that can get up to Prusa performance with some tweaking \n **Price: U$D 200** \n \n", inline=False)
    embed.add_field(
        name="FLSUN QQ-S Pro", value="The QQ-S is a great delta printer at an amazing price, the big brother of the Q5 \n **Price: U$D 364** \n \n", inline=False)
    embed.add_field(
        name="Elegoo Mars", value="The mars is a great sla printer for a good price, resin printers take time to use, so if you are looking for a prototyping machine that can output models fast get an FDM printer \n **Price: U$D 190** \n \n ", inline=False)
    embed.add_field(
        name="Elegoo Mars Pro 2", value="Its a very fast printer, it packs an lcd uv screen that can print at two seconds per layer. It is the printer I use to print Porcelite \n **Price: U$D 350**", inline=False)
    if ("3d print metal" in message.content):
        if metalsend == 0:
            await message.channel.send(embed=metalembed)
            metalsend = 1
    if ("print metal" in message.content):
        if metalsend == 0:
            await message.channel.send(embed=metalembed)
            metalsend = 1
    if ("metal printer" in message.content):
        if metalsend == 0:
            await messagechannel.send(embed=metalembed)
            metalsend = 1
    if ("printer should" in message.content):
        if printsend == 0:
            await message.channel.send(embed=embed)
            my_last_message = await message.channel.history().get(author=bot.user)
            await my_last_message.add_reaction("🗑️")
            printsend = 1
    if ("good printer" in message.content):
        if printsend == 0:
            await message.channel.send(embed=embed)
            my_last_message = await message.channel.history().get(author=bot.user)
            await my_last_message.add_reaction("🗑️")
            printsend = 1
    if ("i buy" in message.content):
        if printsend == 0:
            await message.channel.send(embed=embed)
            my_last_message = await message.channel.history().get(author=bot.user)
            await my_last_message.add_reaction("🗑️")
            printsend = 1
    if ("what printer" in message.content):
        if printsend == 0:
            await message.channel.send(embed=embed)
            my_last_message = await message.channel.history().get(author=bot.user)
            await my_last_message.add_reaction("🗑️")
            printsend = 1
    if ("i should buy" in message.content):
        if printsend == 0:
            await message.channel.send(embed=embed)
            my_last_message = await message.channel.history().get(author=bot.user)
            await my_last_message.add_reaction("🗑️")
            printsend = 1
    printsend = 0
    metalsend = 0

#ping

@bot.command()
async def ping(ctx):
  embed = discord.Embed(title="Ping", color=0x0c0f27)
  embed.add_field(name="Bot", value=f'🏓 Pong! {round(bot.latency * 1000)}ms')
  embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
  await ctx.send(embed=embed)

#ping


#rules

@bot.command()
async def printrules(ctx):
    embed = discord.Embed(
        title="Rules", description="", color=0x0c0f27)
    embed.add_field(
        name="Prusa MK3S", value="The Prusa is a great printer overall, it is quite expensive but worth it. Great option if you arent on a budget and works amazing out of the box \n \n **Price: U$D 750** \n \n", inline=False)
    embed.add_field(
        name="Creality Ender 3", value="The ender 3 is a great printer overall, a great Prusa clone. It is a mid range printer that can get up to Prusa performance with some tweaking\n \n **Price: U$D 200** \n \n", inline=False)
    embed.add_field(
        name="FLSUN QQ-S Pro", value="The QQ-S is a great delta printer at an amazing price, the big brother of the Q5\n \n **Price: U$D 364** \n \n", inline=False)
    embed.add_field(
        name="Elegoo Mars", value="The mars is a great sla printer for a good price, resin printers take time to use, so if you are looking for a prototyping machine that can output models fast get an FDM printer\n \n **Price: U$D 190**", inline=False)
    await ctx.send(embed=embed)

#FAQ

#clear


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    deletemessage = await ctx.send(f"{amount} messages got deleted.")
    await asyncio.sleep(3)
    await deletemessage.delete()

#clear

#kick


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}\nReason: {reason}')

#kick

#ban


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}\nReason: {reason}')

#ban

#unban


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

#unban

#background tasks

@bot.event
async def on_command_error(ctx, error):
    logging.error(f'Error on command {ctx.invoked_with}, {error}')
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Error!",
                              description=f"The command `{ctx.invoked_with}` was not found! We suggest you do `.help` to see all of the commands",
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

#background tasks

bot.run(TOKEN)
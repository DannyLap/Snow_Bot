import discord
import repertoire
from discord.ext import commands
import history

intents = discord.Intents.all()

snow = commands.Bot(command_prefix="/", intents=intents)

REPERTOIRE = repertoire.Repertoire(100)


@snow.event
async def on_ready():
    print("Le bot est prêt !")


# Commandes pour l'historique
@snow.command(name='init')
async def init_bot(ctx):
    for member in ctx.guild.members:
        REPERTOIRE.append(member.id, history.HistoryList())

    REPERTOIRE.get(ctx.author.id).append("Commande n°1")
    REPERTOIRE.get(ctx.author.id).append("Commande n°2")
    REPERTOIRE.get(ctx.author.id).append("Commande n°3")
    REPERTOIRE.get(ctx.author.id).append("Commande n°4")
    REPERTOIRE.get(ctx.author.id).append("Commande n°5")


@snow.command(name='show_all', aliases=['sa'])
async def show_all(ctx):
    await ctx.send(str(REPERTOIRE.get(ctx.author.id).show_all()))
    REPERTOIRE.get(ctx.author.id).append("/show_all")


@snow.command(name='show_last', aliases=['sl'])
async def show_last(ctx):
    await ctx.send(str(REPERTOIRE.get(ctx.author.id).show_last()))
    REPERTOIRE.get(ctx.author.id).append("/show_last")


@snow.command(name='clear', aliases=['c'])
async def clear(ctx):
    await ctx.send(str(REPERTOIRE.get(ctx.author.id).clear()))
    REPERTOIRE.get(ctx.author.id).append("/clear")


@snow.command(name='manual', aliases=['m', 'man', 'help', 'h'])
async def manual(ctx):
    await ctx.send(manual.show_manual)


@snow.event
async def on_member_join(member):
    general_channel = snow.get_channel(1044900412551073832)
    await general_channel.send("Bienvenue sur le serveur ! " + member.name)


@snow.event
async def on_message(message):
    if message.author == snow.user or message.author == 1167397277439098910 or message.author == 1167397120253366323:
        return

    message.content = message.content.lower()

    if message.content == "tada":
        await message.channel.send(message.author)
        await message.channel.send("message.author")

    await snow.process_commands(message)


snow.run("")

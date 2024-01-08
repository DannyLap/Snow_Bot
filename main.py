import discord
from discord.ext import commands

import filter
import repertoire
import history
import manual

intents = discord.Intents.all()

snow = commands.Bot(command_prefix="/", intents=intents)

REPERTOIRE = repertoire.Repertoire(100)
FILTER = filter.FilterList()

IS_INIT = False


def init(ctx):
    global IS_INIT
    IS_INIT = True
    for member in ctx.guild.members:
        REPERTOIRE.append(member.id, history.HistoryList())


@snow.event
async def on_ready():
    print("Le bot est prêt !")
    FILTER.initialisation()


# Commandes pour l'historique
@snow.command(name='init')
async def init_bot_cmd(ctx):
    if not IS_INIT:
        init(ctx)

    REPERTOIRE.get(ctx.author.id).append("Commande n°1")
    REPERTOIRE.get(ctx.author.id).append("Commande n°2")
    REPERTOIRE.get(ctx.author.id).append("Commande n°3")
    REPERTOIRE.get(ctx.author.id).append("Commande n°4")
    REPERTOIRE.get(ctx.author.id).append("Commande n°5")


@snow.command(name='show_all', aliases=['sa'])
async def show_all_cmd(ctx):
    if not IS_INIT:
        init(ctx)

    await ctx.send(str(REPERTOIRE.get(ctx.author.id).show_all()))
    REPERTOIRE.get(ctx.author.id).append("/show_all")


@snow.command(name='show_last', aliases=['sl'])
async def show_last_cmd(ctx):
    if not IS_INIT:
        init(ctx)

    await ctx.send(str(REPERTOIRE.get(ctx.author.id).show_last()))
    REPERTOIRE.get(ctx.author.id).append("/show_last")


@snow.command(name='clear', aliases=['c'])
async def clear_cmd(ctx):
    if not IS_INIT:
        init(ctx)

    await ctx.send(str(REPERTOIRE.get(ctx.author.id).clear()))
    REPERTOIRE.get(ctx.author.id).append("/clear")


@snow.command(name='manual', aliases=['m', 'man'])
async def manual_cmd(ctx):
    if not IS_INIT:
        init(ctx)

    await ctx.send(str(manual.show_manual_intro()))
    await ctx.send(str(manual.show_manual_global()))
    await ctx.send(str(manual.show_manual_history()))
    await ctx.send(str(manual.show_manual_black_list()))
    await ctx.send(str(manual.lien_github()))


@snow.command(name="add_word")
async def add_word_to_filter(ctx):
    if not IS_INIT:
        init(ctx)

    message = ctx.message.content[len('/') + len('add_word '):]
    if len(message) < 2:
        await ctx.send(str("> Les mots de cette liste doivent au minimum faire deux caractères."))
    else:
        FILTER.append(message)
        await ctx.send(str("> **" + message + "** " + " a bien été ajouté a la liste des mots bani."))
    REPERTOIRE.get(ctx.author.id).append("/add_word " + message)


@snow.event
async def on_message(message):
    if not IS_INIT:
        init(message)

    if message.author == snow.user or message.author.id == 274286116608147456 \
            or message.author.id == 1167397277439098910:
        return

    await snow.process_commands(message)
    if message.content.startswith('/add_word'):
        return

    if FILTER.test_message(message.content):
        await message.delete()
        await message.channel.send(str("> Attention " + message.author.mention +
                                       " votre message viens d'etre supprimé car il contient un mot bani."))


snow.run("")

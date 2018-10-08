import discord
from discord.ext import commands
import json
import logging
import random
import datetime
import time
import os

logging.basicConfig(level=logging.INFO)
pfx = 'owl '

description = '''A bot with various useful FAU-related functions, written in Python.'''


green = 0x2dc614
red = 0xc91628
blue = 0x2044f7

CT = datetime.datetime.now().strftime("%A %B %d, %Y | %H:%M:%S")

bot = commands.Bot(command_prefix=pfx, description=description, pm_help=True,
        case_insensitive=True)
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name='with access codes'))

@bot.command(aliases=['about'])
async def info(ctx):
    '''Shows info about OwlBot.'''
    with ctx.typing():
        embed = discord.Embed(title='About OS', description=bot.description, colour=blue)
        embed = embed.add_field(name='Author', value='Galen Gold & Saito', inline=False)
        embed = embed.add_field(name='Contributing', value='Check out the source on GitHub: https://github.com/LFGSaito/owlbot', inline=False)
        embed = embed.add_field(name='License', value='Owlsleys Slave is released under the BSD 2-Clause License', inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.send(f'**Pong!** Current time to access access codes is {bot.latency*1000:.1f} ms')

@bot.command(aliases=['h'])
async def help(ctx):
    '''Show this message.'''
    with ctx.typing():
        embed = discord.Embed(title='Commands', description=bot.description, colour=green)
        cmds = sorted(list(bot.commands), key=lambda x:x.name)
        for cmd in cmds:
            if cmd.name in ['restart', 'shutdown']:
                continue
            v = cmd.help
            if len(cmd.aliases) > 0:
                v += '\n*Aliases:* owl ' +\
                    f', {pfx}'.join(cmd.aliases).rstrip(f', {pfx}')
            embed = embed.add_field(name=pfx+cmd.name, value=v, inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['x'])
async def xkcd(ctx, num : str):
    '''Look up an xkcd by number.'''
    await ctx.send('http://xkcd.com/' + num)


@bot.command(aliases=['ph', 'phoneticize', 'phoneticise', 'phone'])
async def phonetics(ctx, *, msg : str):
    '''Get phonetics for a word or phrase.'''
    with ctx.typing():
        result = ''
        for char in msg.lower():
            if char.isalpha():
                w = [word for word in WORDS if (word[0] == char)]
                result += random.choice(w)
            else:
                result += char
            result += ' '
        embed = discord.Embed(title=f'Phonetics for {msg}', description=result.title(), colour=green)
    await ctx.send(embed=embed)

@bot.command(aliases = ['tikz'])
async def tex(ctx, *, tex : str):
    '''Renders LaTeX within the `align*` environment. The `tikz` alias renders
    within the `tikzpicture` environment.'''
    template = templates[str(ctx.invoked_with)]

    with ctx.typing():
        #print (tex)
        if any(sub in tex for sub in ['align', '\\input', '\\immediate','\\write18','\\file','tikzpicture','\\catcode','\\newread','\\newwrite']):
            await ctx.send(f"Failed to render\n```tex\n{tex}\n```")
            return
        try:
            fn = generate_image(tex, template, ctx.invoked_with)
        except Exception as e:
            print(f"Error: {tex}")
            await ctx.send(f"Failed to render\n```tex\n{tex}\n```")
            return

        if not os.path.isfile(fn):
            await ctx.send(f"Failed to render\n```tex\n{tex}\n```")

        if os.path.getsize(fn) > 0:
            print(f"Rendered: {tex}")
            await ctx.send(file=discord.File(fn))

        else:
            print(f"Failed to render {tex}")
            await ctx.send(f"Failed to render\n```tex\n{tex}\n```")

    time.sleep(1)
    os.system("rm *.tex *.log *.dvi *.png *.aux *.ps")

# Special Commands

@bot.command()
async def restart(ctx):
    if any([str(x.id) in secrets['exit_role'] for x in ctx.author.roles]):
        await ctx.channel.send("Restarting qrm...")
        await bot.logout()
    else:
        try:
            await ctx.message.add_reaction("❌")
        except:
            return

@bot.command()
async def shutdown(ctx):
    if any([str(x.id) in secrets['exit_role'] for x in ctx.author.roles]):
        await ctx.channel.send("Shutting down qrm...")
        os._exit(42)
    else:
        try:
            await ctx.message.add_reaction("❌")
        except:
            return

@bot.command()
async def time(ctx):
    '''Lets people know the date and time right now. Also used in Opening and Closing command TBM'''
    await ctx.send(f"Heya! The Date and Time is " + str(CT))
    return




#########################
with open('secrets.json') as secrets_file:
    secrets = json.load(secrets_file)

WORDS = open('resources/words').read().lower().splitlines()

# Generate LaTeX locally. Is there such things as rogue LaTeX code?
def generate_image(latex, template, cmd):
    num = str(random.randint(0, 2 ** 31))
    latex_file = num + '.tex'
    dvi_file = num + '.dvi'
    with open(latex_file, 'w') as tex:
        latex = template.replace('__DATA__', latex)
        tex.write(latex)
        tex.flush()
        tex.close()
    os.system('latex -shell-escape -halt-on-error ' + latex_file + '</dev/null')
    pngfile = num + '.png'
    os.system(f'convert {pngfile} -trim {pngfile}')
    os.system(f'convert {pngfile} -bordercolor white -border 25 {pngfile}')
    if cmd == 'tex':
        os.system(f'convert {pngfile} -colorspace sRGB -fill "#36393F" -opaque white -fill white -opaque black {pngfile}')
    return pngfile


LATEX_FRAMEWORK = r"""
\documentclass[convert={density=1000},varwidth]{standalone}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{tikz}
\begin{document}
\begin{align*}
__DATA__
\end{align*}
\end{document}
"""

TIKZ_FRAMEWORK = r"""
\documentclass[convert={density=1000},varwidth]{standalone}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{pgfplots}
\usepackage{tikz}
\usepackage[siunitx]{circuitikz}
\begin{document}
\begin{tikzpicture}
__DATA__
\end{tikzpicture}
\end{document}
"""

templates = {'tex': LATEX_FRAMEWORK,
             'tikz': TIKZ_FRAMEWORK}


bot.run(secrets['token'])

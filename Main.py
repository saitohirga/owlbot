# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import discord
from discord.ext import commands
import json
import logging
import random
from datetime import datetime, timedelta
import time
import os

logging.basicConfig(level=logging.INFO)
pfx = 'owl '

description = '''A bot with various useful FAU-related functions, written in Python.'''
start_time = time.time()

green = 0x2dc614
red = 0xc91628
blue = 0x2044f7

CT = datetime.now().strftime("%A %B %d, %Y | %H:%M:%S")

bot = commands.Bot(command_prefix=pfx, description=description, pm_help=True,
        case_insensitive=True)
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name='owl help | IClickers!'))


@bot.command(aliases=['about'])
async def info(ctx):
    '''Shows info about Owlsley's Slave.'''
    with ctx.typing():
        embed = discord.Embed(title='About Owlsleys Slave', description=bot.description, colour=blue)
        embed = embed.add_field(name='Author', value='Galen Gold & Saito', inline=False)
        embed = embed.add_field(name='Contributing', value='Check out the source on GitHub: https://github.com/LFGSaito/OwlBot', inline=False)
        embed = embed.add_field(name='License', value='Owlsleys Slave is released under the BSD 2-Clause License', inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    '''Lets you know how long it will be to access your access codes.'''
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


@bot.command(aliases=['cof'])
async def coffee(ctx):
    '''coffee'''
    await ctx.send('HERE SOME COFFEE!!! '
                      'http://media.beliefnet.com/~/media/photos-with-attribution/food/coffeecreditshutterstockcom.jpg')


@bot.command(aliases=['wai'])
async def whoami(ctx):
    '''Who am I? Let find out'''
    ident = ctx.author.id
    await ctx.send(' You are ' + str(ident))


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
    if any([int(ctx.id) in secrets['exitperson'] for ctx in ctx.author.id]):
        await ctx.channel.send("Restarting qrm...")
        await bot.logout()
    else:
        try:
            await ctx.message.add_reaction("❌")
        except:
            return


@bot.command()
async def shutdown(ctx):
    if any([int(ctx.id) in secrets['exitperson'] for ctx in ctx.author.id]):
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


@bot.command()
async def uptime(ctx):
    '''Show uptime of Mr.Slave.'''
    await ctx.send(calc_uptime())


def calc_uptime():
    up = str(timedelta(seconds=(time.time()-start_time)))

    # parse it pretty-like
    upsplit = up.split(',', 1)
    if len(upsplit) == 1:
        days = '0'
    else:
        days = upsplit[0].split()[0]
        upsplit[0] = upsplit[1]

    upsplit = upsplit[0].split(':')
    if len(upsplit) != 3:
        print('Something happened')
        return ''

    hours = upsplit[0]
    minutes = upsplit[1]
    if minutes[0] == '0':
        minutes = minutes[1]
    seconds = upsplit[2].split('.', 1)[0]
    if seconds[0] == '0':
        seconds = seconds[1]

    # horribly complicated, but appeases my awful need for proper plurality

    rets = ''
    rets += f"{days} day{'' if days == '1' else 's'}, "
    rets += f"{hours} hour{'' if hours == '1' else 's'}, "
    rets += f"{minutes} minute{'' if minutes == '1' else 's'}, "
    rets += f"{seconds} second{'' if seconds == '1' else 's'}"

    return rets


@bot.command()
async def oofs(ctx):
    '''Counts ammount of oofs.'''
    await ctx.send(f"Number of oofs since last reboot: {config['oofs']}")


htm_bonk = (':regional_indicator_b: '
            ':regional_indicator_o: '
            ':regional_indicator_n: '
            ':regional_indicator_k:')

htm_boonk = (':regional_indicator_b: '
             ':regional_indicator_o: '
             ':regional_indicator_o: '
             ':regional_indicator_n: '
             ':regional_indicator_k:     '
             ':regional_indicator_g: '
             ':regional_indicator_a: '
             ':regional_indicator_n: '
             ':regional_indicator_g:')



#########################
with open('secrets.json') as secrets_file:
    secrets = json.load(secrets_file)

WORDS = open('resources/words').read().lower().splitlines()

config = {}
with open('config_default.json', 'r') as f:
    config = json.load(f)
    print('config loaded')

bonk = (':regional_indicator_b: '
        ':regional_indicator_o: '
        ':regional_indicator_n: '
        ':regional_indicator_k:')

boonk = (':regional_indicator_b: '
         ':regional_indicator_o: '
         ':regional_indicator_o: '
         ':regional_indicator_n: '
         ':regional_indicator_k:     '
         ':regional_indicator_g: '
         ':regional_indicator_a: '
         ':regional_indicator_n: '
         ':regional_indicator_g:')


@bot.event
async def on_message(message):
    # make case-insensitive
    message.content = message.content.lower()

    # get the bonks, boonks, and the oofs
    # TODO: Make a thread that periodically saves the oof count
    if message.content == 'oof':
        config['oofs'] += 1
        await message.channel.send('rip')
    elif message.content == 'bonk':
        await message.channel.send(bonk)
    elif message.content.startswith('boonk'):
        await message.channel.send(boonk)
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

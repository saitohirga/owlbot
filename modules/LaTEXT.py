from client import client
import discord
import random
import time, os, re, shutil # tex

cmd_name = "lt"

client.basic_help(title=cmd_name, desc="LaTEXT in Discord, the horror.")

detailed_help = {
	"Usage": f"{client.default_prefix}{cmd_name}",
	"Arguments": "None",
	"Description": "Adds LaTEXT Runnable",
	# NO Aliases field, this will be added automatically!
}
client.long_help(cmd=cmd_name, mapping=detailed_help)


@client.command(trigger=cmd_name,
				aliases=[])  # aliases is a list of strs of other triggers for the command
async def tex(message: discord.Message, *, tex : str):
    '''Renders LaTeX within the `align*` environment. The `tikz` alias renders
      within the `tikzpicture` environment.'''
    template = templates[str(message.invoked_with)]

    with message.typing():
        # print (tex)
        if any(sub in tex for sub in
               ['align', '\\input', '\\immediate', '\\write18', '\\file', 'tikzpicture', '\\catcode', '\\newread',
                '\\newwrite']):
            await message.send(f"Failed to render\n```tex\n{tex}\n```")
            return
        try:
            fn = generate_image(tex, template, message.invoked_with)
        except Exception as e:
            print(f"Error: {tex}")
            await message.send(f"Failed to render\n```tex\n{tex}\n```")
            return

        if not os.path.isfile(fn):
            await message.send(f"Failed to render\n```tex\n{tex}\n```")

        if os.path.getsize(fn) > 0:
            print(f"Rendered: {tex}")
            await message.send(file=discord.File(fn))

        else:
            print(f"Failed to render {tex}")
            await message.send(f"Failed to render\n```tex\n{tex}\n```")

    time.sleep(1)


os.system("rm *.tex *.log *.dvi *.png *.aux *.ps")



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


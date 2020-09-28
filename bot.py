from discord.ext import commands
from Dice import Dice

def get_token():
    return os.environ['DISC_KEY']


token = get_token()
bot = commands.Bot(command_prefix = '.', case_insensitive = True)
d = Dice()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord')

@bot.command()
async def foo(ctx):
    await ctx.send('bar')

@bot.command()
async def credit(ctx):
    await ctx.send('Coded 2020 by TureniDK')

@bot.command()
async def roll(ctx, *args):
    cmd = ''
    if len(args) > 1:
        cmd = args[1]
    dice = args[0]
    number, sides = dice.split('d')
    if number == '':
        number = 1
    if sides == '1':
        await ctx.send('1-sided die? really')
        return
    result = ''
    total = 0
    for i in range(int(number)):
        dice = d.rollExplode(int(sides))
        total += sum(dice)
        result += 'Dice {}: \t\t\t'.format(i+1) + str(sum(dice)) + ' ' + str(dice)+'\n'
    if cmd.lower() == 'wild':
        wild = d.rollExplode(6)
        result += 'Wild: \t'+str(sum(wild)) + ' ' + str(wild)
    else:
        result += 'I alt: \t\t' + str(total)
    await ctx.send(result)

@bot.command()
async def shooting(ctx, *args):
    dice = args[0]
    number, sides = dice.split('d')
    if sides == '1':
        await ctx.send('1-sided die? Really?')
        return
    result = ''
    for i in range(int(number)):
        result += 'Dice {}\t\t'.format(i+1) + d.toHit(int(sides)) + '\n'
    result += 'Wild: \t\t' + d.toHit(6)
    await ctx.send(result)

@bot.command()
async def targetNumber(ctx, args):
    target = args[0]
    dice = args[1]
    number, sides = dice.split('d')
    if sides == 1:
        await ctx.send('1-sided die? Really?')
        return
    result = ''
    for i in range(int(number)):
        result += 'Dice {}\t\t'.format(i+1) + d.toHitTarget(int(sides), target) + '\n'
    result += 'Wild: \t\t' + d.toHitTarget(6, target)
    await ctx.send(result)


bot.run(token)



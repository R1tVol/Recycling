import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name='recycling_tips')
async def recycling_tips(ctx, number=None):
    tips = {
        '1': 'Contribute to the recycling system by separating materials suitable for recycling. Collecting materials such as paper, plastic, glass, and metal in separate bins can help the recycling process.',
        '2': 'Choose unpackaged products or choose products with minimal packaging. Reduce the use of plastic bags by using your own fabric bags and reusable shopping bags for grocery shopping.',
        '3': 'As part of the zero waste movement, take steps to reduce disposable products. For example, you can use refillable water bottles, reduce disposable items, and reduce eating out by preparing your own meals.',
        '4': 'Use energy and water-saving devices. You can reduce both energy and water consumption by using LED lamps, energy-efficient white goods, and water-saving fixtures.',
        '5': 'You can make compost by using organic waste. This is both a way to reduce waste in the home and can improve soil quality.',
        '6': 'You can donate the items you do not use at home or send them to recycling centers.',
        '7': 'Prefer to store invoices, documents, and notes digitally to reduce paper waste. You can reduce electronic waste by trying to use electronic devices for longer periods of time.',
        '8': 'Think before you buy and evaluate whether you need it. With conscious consumption habits, you can prevent unnecessary purchases and reduce the amount of waste.'
    }

    if number and number in tips:
        await ctx.send(tips[number])
    else:
        await ctx.send("Invalid tip number. Please provide a valid number between 1 and 8.")

bot.run("YOUR_TOKEN")

import os
from dotenv import load_dotenv
from discord.ext import commands
from yahoo_fin import stock_info as si


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')


@bot.command(name='tools')
async def help_func(ctx):
    await ctx.send("My functions are as follows: \n!stock {ticker} - returns live price "
                   "\n!futures - returns S&P, Nasdaq, and Dow futures "
                   "\n!earnings {ticker} - returns next earnings date and time")


@bot.command(name='stock')
async def live_stock_price(ctx, arg):
    price = si.get_live_price(arg)
    post_market = si.get_postmarket_price(arg)
    response = "Ticker: " + arg.upper() + "\nDay: $" + str(price.round(3)) +\
               "\nPost-market: $" + str(post_market)
    await ctx.send(response)


@bot.command(name='futures')
async def live_futures(ctx):
    futures = str(si.get_futures().round(2))
    array_of_futures = futures.split()
    await ctx.send("S&P 500 Future: $" + array_of_futures[21] + "\nChange: " + array_of_futures[25] +
                   "\nDow Jones Future: $" + array_of_futures[37] + "\nChange: " + array_of_futures[41] +
                   "\nNasdaq Future: $" + array_of_futures[51] + "\nChange: " + array_of_futures[55])


@bot.command(name='earnings')
async def next_earnings_date(ctx, arg):
    date = str(si.get_next_earnings_date(arg)) + " EST"
    await ctx.send(date)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to the discord')

bot.run(TOKEN)

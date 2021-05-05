
import discord
import os
import random
from discord.ext import commands,tasks
from discord import Color
from SimpleEconomy import Seco

client = commands.Bot(command_prefix= '!')                                                                            # The prefix is ! but it can be changed                                                 
TOKEN = os.getenv('YOUR_BOT_TOKEN')                                                                                   # Insert your bot's token in place of "YOUR_BOT_TOKEN"
seco = Seco(client,"your_api_token","your_project_name_lowercase")                                                    # These can be found on https://simpleco.xyz/dashboard

@client.command()
async def slots(ctx, amount:int):                                                                                     # Function name is 'slots'
    balance = await seco.get_balance(ctx.author.id)                                                                     # Get message author's balance from online DB
    double = amount * 2                                                                                               # Amount of earnings to showcase from doubling
    quadwin = amount * 3                                                                                               # Amount of earnings to add from quadrupling
    quad = amount * 4                                                                                                 # Amount of earnings to showcase from quadrupling
    if amount <= 0:                                                                                                   # You cannot gamble any amount lower than 1
        return await ctx.send("You can't gamble with less than **1** monie!")
    if balance == 0:                                                                                                  # You cannot gamble if you have no monies
        return await ctx.send("You can't gamble with less than **1** monie!")
    if balance < amount :                                                                                             # You cannot gamble over your balance
        await ctx.send("Oops, looks like you don't have enough monies to gamble this amount!") 
    else:
        choice=random.randint(1,100)                                                                                  # Random number from 1 to 100
        if choice == 100:                                                                                             # If choice is 100 you win a jackpot
            await seco.add_balance(ctx.author.id,100000)                                                              # Add jackpot to balance
            embed=discord.Embed(title="You won!",                                                                     # Send an embed announcing the win
                                description="Congratulations! You hit the jackpot of **100,000** monies!", 
                                color=discord.Color.green())
            embed.add_field(name="** **", value="🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉", inline=False)
            await ctx.send(embed=embed)                                                                               
            return
        if choice <= 95 and choice > 79:                                                                              # If choice is within 79 to 95 you double your input
            await seco.add_balance(ctx.author.id,amount)                                                              # Add equal amount as your input to balance to double your input
            embed=discord.Embed(title="You won!",                                                                     # Send an embed announcing the win
                                description=f"Congratulations! You won **{double}** monies!", 
                                color=discord.Color.green())
            embed.add_field(name="** **", value="🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉", inline=False)
            await ctx.send(embed=embed)
            return
        if choice < 100 and choice > 95:                                                                              # If choice is within 96 to 100 you quadruple your input
            await seco.add_balance(ctx.author.id,quadwin)                                                             # Add 3 times your input to your balance to quadruple your input
            embed=discord.Embed(title="You won!",                                                                     # Send an embed announcing the win
                                description=f"Congratulations! You won **{quad}** monies!", 
                                color=discord.Color.green())
            embed.add_field(name="** **", value="🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉", inline=False)
            await ctx.send(embed=embed)
            return
        if choice <= 79:                                                                                              # If choice is less than or equal to 79 you lose your input
            await seco.remove_balance(ctx.author.id,amount)                                                           # Remove your input from your balance
            embed=discord.Embed(title="You lost!",                                                                    # Send an embed announcing the loss
                                description=f"Better luck next time! You lost your **{amount}** monies!", 
                                color=discord.Color.red())
            await ctx.send(embed=embed)
            return
            
client.run(TOKEN) 

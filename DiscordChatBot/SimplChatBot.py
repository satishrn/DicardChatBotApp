import discord
from FetchLinkUtil import Util

client = discord.Client()
fetch_util = Util()


@client.event
async def on_ready():
    print("The bot is ready!")
    activity = discord.Game(name="with a Bot")
    await client.change_presence(status=discord.Status.idle, activity=activity)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "hi":
        await message.channel.send("hey")

    if message.content.startswith("!google"):
        cont = message.content.split(" ", 1)
        api_key = "secret_api_key"
        cse_id = "cse_key"

        # Fetching the result from google
        results = fetch_util.google_query(cont[1], api_key, cse_id, num = 10)
        if results == -1:
            await message.channel.send("No links For searched keyword on google")
        else:
            my_url = []
            my_title = []
            for res in results:
                my_url.append(res['link'])
                my_title.append((res['title']))
                print(res['link'])

            # embed the url and return it to bot
            embed = discord.Embed(title="nice bot", description="A Very Nice bot. google search links are:", color=0xeee657)
            for i in range(0, 5):
                embed.add_field(name=my_title[i], value=my_url[i], inline=False)

            await message.channel.send(embed=embed)

    if message.content.startswith("!recent"):
        cont = message.content.split(" ", 1)
        result = fetch_util.search_query(cont[1])
        embed = discord.Embed(title="nice bot", description="A Very Nice bot. google search history related to keyword:", color=0xeee657)
        for i in range(0, len(result)):
            embed.add_field(name="searched"+str(i)+":", value=result[i], inline=False)
            print(result[i])
        await message.channel.send(embed=embed)


client.run("Bot_token")

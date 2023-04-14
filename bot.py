import time
import discord
import secret
from main import main

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'logged in as {client.user}')

    known_results = []

    while True:
        res = await main()
        if len(res) != len(known_results):
            for subject in res:
                await client.get_channel(692727115795267597).send(subject)
            known_results = res
        else:
            print('no new results')
        time.sleep(600)


client.run(secret.DISCORD_TOKEN)

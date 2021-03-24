import discord
from gtts import gTTS
import os
from discord.ext import commands
from random import choice
from time import sleep


client = commands.Bot(command_prefix = ">")
language = "it"

@client.event
async def on_ready():
    print("Ueue")


@client.event
async def on_member_join(member):
    print(f"ueue, benvenuto fratm{member}")


@client.event
async def on_member_remove(member):
    print(f"guapp {member} left")

@client.command()
async def ping(ctx):
    print("un cazzone ha ordinato una pizza")
    await ctx.send("Ciro express: consegna pizze in %.2fms" % (client.latency * 1000))


@client.command(aliases = ["sesso_insieme_a", "sesso_con"])
async def sesso(ctx, * , uagliona = "mammt"):
    respones = ["solare sul pianeta del napoli",
                "pazzo sul letto del napoli",
                "sfrenato sul divanetto del napoli",
                "artistico nell' osteria del napoli",
                "gourmet nella pizzeria di gennaro(del napoli)",
                "intellettuale all'\"università Federico II di napoli\" del napoli",
                "napoletano nella napoli del napoli",
                "diabetico nella pasticceria del napoli",
                "pesce in mano sul divanetto del napoli",
                "esplosivo sui petardi del napoli",
                "abusivo in una palazzina sul Vesuvio",
                "rumoroso sul balcone delle vrenzole di napoli",
                "asmatico nell' ASL del napoli",
                "fraudolento con le canzoni neomelodiche del napoli",
                "incaprettatto a capri del napoli",
                "stellare con De Laurentis sulla Villa Comunale del napoli",
                "iperbolico nell'iperspazio del napoli",
                "tra le onde alla Reggia di Capodimonte a napoli",
                "paralipomenico della batracomiomachia del napoli",
                "ansimante a Piazza Mercante di Napoli"
                ]
    
    await ctx.send(f"sesso {choice(respones)} con {uagliona} ")


@client.command(aliases= ["ciro_quotes"])
async def citazioni(ctx):
    file = open("I_50_proverbi_napoletani_piu_belli.txt", "r", encoding = "UTF-8")
    quotes = file.readlines()
    quote = choice(quotes)[4:]
    file.close()

    await ctx.send(f"{quote}")
    output = gTTS(text = quote, lang = "it", slow = False)
    output.save("ciro_quote_temp.mp3")
    await play(ctx, file_mp3 = "ciro_quote_temp.mp3")


@client.command()
async def sapone(ctx):
    await play(ctx, file_mp3 = "sapone_response.mp3")

@client.command(aliases=['paly', 'queue', 'que'])
async def play(ctx, file_mp3 = 'funiculi_funicula.mp3' ):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio(file_mp3)
    print(f"playing {file_mp3}")
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)


@client.command()
async def pulizza(ctx, amount = 5):
    try:
        await ctx.channel.purge(limit = amount)
        print(f"L'ecoross ha pulito {amount} righe")
    except:
        print("vira tu si cazz i coriglianesi")


@client.command()
async def kick(ctx, member: discord.Member, * , reason = "Bucchini mannari"):
    await member.kick(reason = reason)


@client.command()
async def ban(ctx, member: discord.Member, * , reason = "Bucchini mannari"):
    await member.ban(reason = reason)


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    
    for banned_user in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            print(f"{user.name}#{user.discriminator} era stato bannato per {user.mention}")
            await ctx.guild.unban(user)
            await ctx.send(f"perdonato il guappo {user.name}#{user.discriminator}...\n statt accuort moh eh...")
            return


@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await ctx.send("sto facenn nu maronn ij cacio e maccarun e nessun m'add 'a scassà o' cazz")
    await channel.connect()


@client.command()
async def leave(ctx):
    await sapone(ctx)
    sleep(9)
    await ctx.voice_client.disconnect()
#client.run("ODI0MTk4NDM4ODYxNDA2Mjc4.YFr4nA.D5q9c4gyPXusqt3GqefGDE8z5-w")
client.run("ODI0MTk4OTY3NDgxOTkxMTY4.YFr5Gg._Hnmx3r7WDPIy49M3rUCem4e1QQ")

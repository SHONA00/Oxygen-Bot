import discord
import os
import sys
import psutil
import asyncio
import random
import urllib
import json
import httpx
import requests
from time import strftime
from discord.ext import commands
import jishaku
from discord.utils import find
from discord.ext import commands, tasks
import time
import aiohttp
from cogs.anti import anti
from discord_buttons_plugin import *
from discord_components import *
from discord_components import DiscordComponents, Button, Select, SelectOption
from discord_components import *
from typing import Union
from discord.gateway import DiscordWebSocket
import datetime
from discord.ext.commands import Greedy
from typing import Union
from keep_alive import keep_alive
keep_alive()

start_time = datetime.datetime.utcnow()

#os.system("pip install PyNaCl")
#os.system("clear")


def getbadges(userid):
    with open("badges.json", "r") as f:
        data = json.load(f)
    if str(userid) not in data:
        default = []
        makebadges(userid, default)
        return default
    return data[str(userid)]


def makebadges(userid, data):
    with open("badges.json", "r") as f:
        badges = json.load(f)
    badges[str(userid)] = data
    new = json.dumps(badges, indent=4, ensure_ascii=False)
    with open("badges.json", "w") as w:
        w.write(new)

tostop = 0


def randnum(fname):
    lines=open(fname).read().splitlines()
    return random.choice(lines)

def guildowner(ctx):
    return ctx.message.author.id == ctx.guild.owner.id or ctx.message.author.id == 1083629999292174346 or ctx.message.author.id == 1059397400004919327


def is_server_owner(ctx):
    return ctx.message.author.id == ctx.guild.owner.id or ctx.message.author.id == 1083629999292174346 or ctx.message.author.id == 1059397400004919327


def clientowner(ctx):
    return ctx.message.author.id == 1083629999292174346 or ctx.message.author.id == 1059397400004919327


def is_allowed(ctx):
    return ctx.message.author.id == 841286763506434130 or ctx.message.author.id == 1059397400004919327


default_prefix = "-"


def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        idk = json.load(f)
    if message.author.id in []:
        return ""
    elif str(message.guild.id) not in idk:
        return f"{default_prefix}"
    elif str(message.guild.id) in idk:
        idkprefix = idk[str(message.guild.id)]
        return f"{idkprefix}"


token = "MTA1OTc5OTkyNDM5NDQ0Njk0MA.GNmkus.Os1fxa-hMCYwMiV2sBCHYnJxg8q18Uph8qiL34"
intents = discord.Intents.default()
intents.members = True
intents.guilds = True
client = commands.AutoShardedBot(shard_count=1,
                                 command_prefix=("-"),
                                 case_insensitive=True,
                                 intents=intents,
                                 help_command=None,
                                 activity=discord.Activity(
                                     type=discord.ActivityType.listening,
                                     name=f"-help | OxyGeN"),
                                 status=discord.Status.idle)
client.load_extension("cogs.autorole")
client.owner_ids = [1059397400004919327]
client.add_cog(anti(client))
buttons = ButtonsClient(client)
headers = {"Authorization": f"{token}"}
ddb = DiscordComponents(client)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and not filename.startswith('_'):
        pass

os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"

client.load_extension("jishaku")

from cogs.anti import anti
from cogs.help import help
client.add_cog(help(client))
client.add_cog(anti(client))


@client.event
async def on_ready():
    print(f"Sucessfully logged in {client.user}")

def restart_client():
    os.execv(sys.executable, ['python'] + sys.argv)

bot = commands.Bot(command_prefix='-')

@bot.command()
async def setroleicon(ctx, role_id: int, icon_url: str):
    role = ctx.guild.get_role(role_id)
    if role is None:
        await ctx.send("Role not found.")
        return
    try:
        await role.edit(icon=icon_url)
        await ctx.send("Role icon updated successfully.")
    except discord.Forbidden:
        await ctx.send("I don't have permission to set the role icon.")

@client.command()
@commands.is_owner()
async def restart(ctx):
    await ctx.send(f"`Restarting {client.user}`")
    restart_client()


########## Useful ##########

OxyGen_id = "1086352324252930058"
client_id = "961655435801268325"
supportlink = "https://discord.gg/nukersop"
tick = "<:legion_correct:1086535117339631666>"
cross = "<:legion_wrong:1086535023106211950>"
warn = "<a:legion_warn:1086606146221133825>"
arrow = "<:legion_arrow:1086608694965448864>"
reply = "<:legion_reply:1086607925784621196>"
dash = "<:legion_dash:1086607113909968967>"
color = "0x2f3136"
client_name = "OxyGen"


################ PFP #############
@commands.has_permissions(manage_channels=True)
@commands.check(is_server_owner)
@client.command()
async def start(ctx):
        await ctx.reply(">>> Starting Auto PFP In This Channel")
        while tostop == 0:
            
            embed = discord.Embed(title = f"OxyGen",description = "",color = 0x2f3136)
            embed.set_image(url = randnum('scraped.txt'))
            embed.set_footer(text = "Made By OxyGen Development")
            await ctx.send(embed=embed)
            time.sleep(2)
          
@commands.has_permissions(manage_channels=True)
@commands.check(is_server_owner)
@client.command()
async def stop(ctx):
    await ctx.reply(">>> Stopping Auto PFP In This Channel")         
################ Xeone ##################

@client.command()
async def boosts(ctx):
  boost = discord.Embed(colour=0x2f3136)
  boost.add_field(name=f"<a:banner_boost_please:1085419506047918190> Boost Info For: {ctx.guild.name} ", value=f"\n▸ Total Boost: {ctx.guild.premium_subscription_count}\n▸ Boost Level: {ctx.guild.premium_tier}\n")
  await ctx.send(embed=boost)

@client.command(aliases=["totalusers", "usercount", "allusers", "u"])
async def users(ctx):
    embed = discord.Embed(
        title=
        f'',
        description=
        f'{client_name} Is Trusted By {len(client.users)} Users',
        color=0x2f3136)
    embed.set_footer(text="")
    await ctx.send(embed=embed)

@client.command(aliases=["c"])
async def credit(ctx):
    embed = discord.Embed(
        title=
        f'OxyGen Credits',
        description=
        f'Thanks To PythoN For Help With The Bot!\n',
        color=0x2f3136)
    embed.set_footer(text="")
    await ctx.send(embed=embed)

@client.command(aliases=["sv", "serversss", "s", "guilds", "g"])
async def servers(ctx):
    embed = discord.Embed(
        title=
        f'',
        description=
        f'{client_name} Is Providing Safety To {len(client.guilds)} Guilds',
        color=0x2f3136)
    embed.set_footer(text="")
    await ctx.send(embed=embed)

@client.command(aliases=["inv"])
async def invite(ctx):
    embed = discord.Embed(
        color=0x2f3136,
        description=
        f"**[Support Server](https://discord.gg/drWXZrBpKH)**"
    )
    await ctx.send(embed=embed, mention_author=True)

@client.command(aliases=["abt"])
async def about(ctx):
    embed = discord.Embed(
        color=0x2f3136,
        description=
        f"OxyGen, the all-in-one Discord bot packed with amazing features! With functionalities such as moderation, security, logging, welcome messages, fun commands, games, and more!"
    )
    await ctx.send(embed=embed, mention_author=True)

@client.command(aliases=["mc"])
async def membercount(ctx):
    scembed = discord.Embed(colour=discord.Colour(0x2f3136))
    scembed.add_field(
        name='**<:user_icon:1084466286001668147> Members**',
        value=f"{ctx.guild.member_count}")
    await ctx.send(embed=scembed, mention_author=False)

@client.command(aliases=["antiban", "Anti-Ban", " AntiBan", "antikick", " Anti-Kick", "Anti--Kick", "antiunban", " Anti-Unban", "Anti--Unban", "antibotadd", "anti-bot-add", " Anti-Bot-Add", "Anti--Bot--Add", " Anti-Channel-Create", "AntiChannelCreate", " antichannelcreate", "Anti-Channel-Delete", " AntiChannelDelete", "antichanneldelete", "Anti-Channel-Update", " AntiChannelUpdate", "antichannelupdate", " Anti-Role-Delete", "AntiRoleDelete", " antiroledelete", "Anti-Role-Delete", " Anti-Role-Update", "AntiRoleUpdate", " antirolecreate", "Anti-Role-Create", " AntiRole-Create", "antirolecreate"])
async def Anti(ctx):
    embed = discord.Embed(color=0x2f3136,title=f"",
        description=
        f"**AntiNuke Features Are Auto-Enabled**")
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=embed)

@client.command(aliases=["rall"])
@commands.has_permissions(administrator=True)
async def roleall(ctx, role: discord.Role):
  rrole=ctx.guild.get_role(role.id)
  if role.permissions.administrator or role.permissions.ban_members:
    await ctx.send(embed=discord.Embed(color=discord.Colour(0x2f3136),title=f"OxyGen",description=f"Use A Role Without Dangerous Perms Like: `Administartors`, `Ban Members` & Much More!"))
  else:
    mm = await ctx.send(embed=discord.Embed(color=discord.Colour(0x2f3136),title=f"OxyGen",description=f"<a:jhebwbsajabhJa:1024918925319872522> Adding Mentioned Role To @everyone"))
    for all in ctx.guild.members:
      try:
        await all.add_roles(rrole)
      except:
        pass
    await mm.edit(embed=discord.Embed(color=discord.Colour(0x2f3136),title=f"OxyGen",description=f"Added Mentioned Role To @everyone"))


@client.command()
async def ping(ctx):
    embed = discord.Embed(color=0x2f3136,
                          title="Ping!",
                          description=f"**`{int(client.latency * 1000)}ms`**")
    embed.set_thumbnail(url='')
    await ctx.send(embed=embed)

@client.command(aliases=["bi", "stats", "stat"])
async def botinfo(ctx):
    embed = discord.Embed(
        title=
        f'OxyGen Stats N Info',
        description=
        f'**__Server(s)__\n```\nTotal Server(s): {len(client.guilds)}\nTotal Shard(s): 2\nShard(s) Server: {len(client.guilds)}```\n__Version Info__\n```\nPython: 3.8.12\nLibrary: Discord.py\nLibrary Version: V2```\n__HostInfo__```\nHost: LD-Linux x86\nLatency: {int(client.latency * 1000)}\nWesocket: {int(client.latency * 750)}\nReply Latency: {int(client.latency * 400)}```\n```Prefix: ;```\n\n__Developer__\n```PythoN.#1337```\n__Owners__\n```PythoN, Martin```\n\n__Link(s)__\n[Admin Invite](https://discord.com/api/oauth2/authorize?client_id=1059799924394446940&permissions=8&scope=bot) | [0 Perms Invite](https://discord.com/api/oauth2/authorize?client_id=1059799924394446940&permissions=0&scope=bot)**',
        color=0x2f3136)
    embed.set_footer(text="Made With ❤️ By OxyGen")
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_channels=True)
async def hide(ctx, channel: discord.TextChannel = None):
  channel = channel or ctx.channel
  overwrite = channel.overwrites_for(ctx.guild.default_role)
  overwrite.view_channel = False
  await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
  description=f'<:success:992024105975037992> | {ctx.channel.mention} Is Now Hidden'
  await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=description))

@client.command(aliases=["nick", "setnick"])
@commands.has_permissions(manage_nicknames=True)
async def nickname(ctx, member: discord.Member, *, nick):
    old_name = member.name
    await member.edit(nick=nick)
    description = f"Changed Nick of `{old_name}` To `{nick}`"
    await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=description))

@client.command()
@commands.has_permissions(manage_channels=True)
async def unhide(ctx, channel: discord.TextChannel = None):
  channel = channel or ctx.channel
  overwrite = channel.overwrites_for(ctx.guild.default_role)
  overwrite.view_channel = False
  await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
  description=f'<:success:992024105975037992> {ctx.channel.mention} Is Now Visible'
  await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=description))


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason == None:
        reason = " no reason provided"
    await ctx.guild.kick(member)
    await ctx.send(f'{tick} | Kicked {member.mention} Reason: {reason}')


@commands.cooldown(3, 300, commands.BucketType.user)
@client.command(aliases=["massunban"])
@commands.has_permissions(administrator=True)
async def unbanall(ctx):
    guild = ctx.guild
    banlist = await guild.bans()
    await ctx.send(
        '**<:success:992024105975037992> | Unbanning  {} Members**'.format(
            len(banlist)))
    for users in banlist:
        await ctx.guild.unban(user=users.user, reason=f"By {ctx.author}")


@client.command(aliases=["fuckoff", "fuckyou", "getlost", "fuckban"])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
  if ctx.author.top_role.position < member.top_role.position or ctx.author.top_role.position == member.top_role.position:
    await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"**You Can't Ban Member Above You Or Similar To Your Roless!**"))
  else:
    await member.ban(reason=f"Banned by {ctx.author}, Reason: {reason}")
    await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"**<:success:992024105975037992> Banned {member}**"))
    try:
      await member.send(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"**You Have Been Banned From `{ctx.guild.name}` By `{ctx.auhtor}` For `{reason}`**"))
    except:
      pass


@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel = None):
  channel = channel or ctx.channel
  overwrite = channel.overwrites_for(ctx.guild.default_role)
  overwrite.send_messages = False
  await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
  description=f'<:success:992024105975037992> {ctx.channel.mention} Has Been Locked!'
  await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=description))

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: discord.TextChannel = None):
  channel = channel or ctx.channel
  overwrite = channel.overwrites_for(ctx.guild.default_role)
  overwrite.send_messages = True
  await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
  description=f'<:success:992024105975037992> {ctx.channel.mention} Has Been Unlocked!'
  await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=description))


@commands.has_guild_permissions(manage_channels=True)
@client.command()
async def unhideall(ctx):
    await ctx.send(f"**{tick} | UnHiding All Channels Please Wait!**")
    for x in ctx.guild.channels:
        await x.set_permissions(ctx.guild.default_role, view_channel=True)
    await ctx.send(f"**{tick} | Successfully UnHidden All Channels**")


@commands.has_guild_permissions(manage_channels=True)
@client.command()
async def hideall(ctx):
    await ctx.send(f"**{tick} | Hiding All Channels Please Wait!**")
    for x in ctx.guild.channels:
        await x.set_permissions(ctx.guild.default_role, view_channel=False)
    await ctx.send(f"**{tick} | Successfully Hidden All Channels**")


########### CUSTOM SERVER COMMAND ########

@commands.has_guild_permissions(manage_roles=True)
@client.command(aliases=['friend-role-set'])
async def setupfriend(ctx, role: discord.Role = None):
    with open('friend.json', 'r', encoding='utf-8') as f:
        key = json.load(f)
    key[str(ctx.guild.id)] = [str(role.id)]
    with open('friend.json', 'w', encoding='utf-8') as f:
        json.dump(key, f, indent=4)
        await ctx.send(f"{tick} | Updated Friends Role To `{role.name}`")

@commands.has_guild_permissions(manage_roles=True)
@client.command(aliases=["friends", "addfriend", "add friend", "add-friend"])
async def friend(ctx, mem: discord.Member = None):
    with open("friend.json", 'r') as f:
        key = json.load(f)
    if f'{ctx.guild.id}' not in key:
        await ctx.send('<:error:992024170785427537> Please Setup This Feature')
    elif f'{ctx.guild.id}' in key:
        for idk in key[str(ctx.guild.id)]:
            r = discord.utils.get(ctx.guild.roles, id=int(idk))
            await mem.add_roles(r)
            await ctx.send(f'{tick} | Added Role To The Mentioned User')

@commands.has_guild_permissions(manage_roles=True)
@client.command(aliases=['official-role-set'])
async def officifasf(ctx, role: discord.Role = None):
    with open('official.json', 'r', encoding='utf-8') as f:
        key = json.load(f)
    key[str(ctx.guild.id)] = [str(role.id)]
    with open('official.json', 'w', encoding='utf-8') as f:
        json.dump(key, f, indent=4)
        await ctx.send(f"{tick} | Updated Official Role To `{role.name}`")

@commands.has_guild_permissions(manage_roles=True)
@client.command(
    aliases=["officials", "official-add", "official give", "officialofficial"])
async def official(ctx, mem: discord.Member = None):
    with open("official.json", 'r') as f:
        key = json.load(f)
    if f'{ctx.guild.id}' not in key:
        await ctx.send('<:error:992024170785427537> Please Setup This Feature')
    elif f'{ctx.guild.id}' in key:
        for idk in key[str(ctx.guild.id)]:
            r = discord.utils.get(ctx.guild.roles, id=int(idk))
            await mem.add_roles(r)
            await ctx.send(f'{tick} | Added Role To The Mentioned User')

@commands.has_guild_permissions(manage_roles=True)
@client.command(aliases=['cutie-role-set'])
async def cutieee(ctx, role: discord.Role = None):
    with open('cutie.json', 'r', encoding='utf-8') as f:
        key = json.load(f)
    key[str(ctx.guild.id)] = [str(role.id)]
    with open('cutie.json', 'w', encoding='utf-8') as f:
        json.dump(key, f, indent=4)
        await ctx.send(f"{tick} | Updated Cuties Role To `{role.name}`")

@commands.has_guild_permissions(manage_roles=True)
@client.command(aliases=["cuties", "cutie-add", "cutie give", "cutiecutie"])
async def cutie(ctx, mem: discord.Member = None):
    with open("cutie.json", 'r') as f:
        key = json.load(f)
    if f'{ctx.guild.id}' not in key:
        await ctx.send('<:error:992024170785427537> Please Setup This Feature')
    elif f'{ctx.guild.id}' in key:
        for idk in key[str(ctx.guild.id)]:
            r = discord.utils.get(ctx.guild.roles, id=int(idk))
            await mem.add_roles(r)
            await ctx.send(f'{tick} | Added Role To The Mentioned User')

@commands.has_guild_permissions(manage_roles=True)
@client.command(aliases=['skid-role-set'])
async def sdsdkid(ctx, role: discord.Role = None):
    with open('skid.json', 'r', encoding='utf-8') as f:
        key = json.load(f)
    key[str(ctx.guild.id)] = [str(role.id)]
    with open('skid.json', 'w', encoding='utf-8') as f:
        json.dump(key, f, indent=4)
        await ctx.send(f"{tick} | Updated Skid Role To `{role.name}`")

@commands.has_guild_permissions(manage_roles=True)
@client.command(aliases=["skids", "skid-add", "skid give", "skidskid"])
async def skid(ctx, mem: discord.Member = None):
    with open("skid.json", 'r') as f:
        key = json.load(f)
    if f'{ctx.guild.id}' not in key:
        await ctx.send('<:error:992024170785427537> Please Setup This Feature')
    elif f'{ctx.guild.id}' in key:
        for idk in key[str(ctx.guild.id)]:
            r = discord.utils.get(ctx.guild.roles, id=int(idk))
            await mem.add_roles(r)
            await ctx.send(f'{tick} | The Mentioned User is Now marked as a skid')

@commands.has_guild_permissions(manage_roles=True)
@client.command(aliases=['vip-role-set'])
async def vippp(ctx, role: discord.Role = None):
    with open('vip.json', 'r', encoding='utf-8') as f:
        key = json.load(f)
    key[str(ctx.guild.id)] = [str(role.id)]
    with open('vip.json', 'w', encoding='utf-8') as f:
        json.dump(key, f, indent=4)
        await ctx.send(f"{tick} | Updated VIP Role To `{role.name}`")

@commands.has_guild_permissions(manage_roles=True)
@client.command(aliases=["vips", "vip-add", "vip give", "vipvip"])
async def vip(ctx, mem: discord.Member = None):
    with open("vip.json", 'r') as f:
        key = json.load(f)
    if f'{ctx.guild.id}' not in key:
        await ctx.send('<:error:992024170785427537> Please Setup This Feature')
    elif f'{ctx.guild.id}' in key:
        for idk in key[str(ctx.guild.id)]:
            r = discord.utils.get(ctx.guild.roles, id=int(idk))
            await mem.add_roles(r)
            await ctx.send(f'{tick} | Added Role To The Mentioned User')
############# CUSTOM PREF #############


@client.command(aliases=["prefix"])
@commands.has_permissions(administrator=True)
async def setprefix(ctx, prefiloda):
    with open("prefixes.json", "r") as f:
        idk = json.load(f)
    if len(prefiloda) > 5:
        await ctx.reply(embed=discord.Embed(
            color=discord.Colour(0x2f3136),
            description=f'Prefix Cannot Exceed More Than 5 Letters'))
    elif len(prefiloda) <= 5:
        idk[str(ctx.guild.id)] = prefiloda
        await ctx.reply(embed=discord.Embed(
            color=discord.Colour(0x2f3136),
            description=f'{tick} Updated Server Prefix To `{prefiloda}`'))
    with open("prefixes.json", "w") as f:
        json.dump(idk, f, indent=4)


#### Logging #####
@client.command(
    aliases=["log-set", "setlog", "setlogs", "logall", "logging-set"])
@commands.has_permissions(administrator=True)
async def loggingchannel(ctx, channel: discord.TextChannel):
    with open('logsch.json', 'r') as f:
        logs = json.load(f)
        if str(ctx.guild.id) not in logs:
            logs[str(ctx.guild.id)] = str(channel.id)
            await ctx.send(
                f"**<:success:992024105975037992> | Updated Logs Channel To {channel.mention}**"
            )
            await channel.send(embed=discord.Embed(
                color=discord.Colour(0x2f3136),
                description=
                f"**<:list:989481507934601279> This Channel Has Been Added As Logs Channel And All Logs Will Be Shown Here**"
            ))
        elif str(ctx.guild.id) in logs:
            logs[str(ctx.guild.id)] = str(channel.id)
            await ctx.send(
                f'**<:success:992024105975037992> | Updated Logs Channel To {channel.mention}**',
                mention_author=False)
            await channel.send(embed=discord.Embed(
                color=discord.Colour(0x2f3136),
                description=
                f"**This Channel Has Been Added As Logging Channel!**"))
    with open('logsch.json', 'w') as f:
        json.dump(logs, f, indent=4)


@client.command(aliases=[
    "log-show", "showlogs", "showlog", "log-config", "logging config"
])
@commands.has_permissions(administrator=True)
async def logshow(ctx):
    with open('logsch.json', 'r') as i:
        logs = json.load(i)
        try:
            await ctx.send(
                f'**<:success:992024105975037992> | The Logging Channel For Your Server is <#{logs[str(ctx.guild.id)]}>**',
                mention_author=False)
        except KeyError:
            await ctx.send(
                f"**<:error:992024170785427537> | No Logging Channel Can Be Found Pls Set One.**",
                mention_author=False)


@client.command(
    aliases=[
        "log-remove", "logsremove", " removelog", "removelogs",
        "logging-delete"
    ], )
@commands.has_permissions(administrator=True)
async def logremove(ctx):
    with open('logsch.json', 'r') as f:
        logs = json.load(f)
        if str(ctx.guild.id) not in logs:
            await ctx.send(
                f"**<:error:992024170785427537> | No Logging Channel Can Be Found Pls Set One.**",
                mention_author=False)
        else:
            logs.pop(str(ctx.guild.id))
            await ctx.send(
                f"**<:success:992024105975037992> | Disabled Logging Feature For The Server.**",
                mention_author=False)
    with open('logsch.json', 'w') as f:
        json.dump(logs, f, indent=4)


#--- events ----#
async def joinlog_event(member):
    with open('logsch.json', 'r') as i:
        logs = json.load(i)
        if str(member.guild.id) in logs:
            em = discord.Embed(
                color=discord.Colour(0x2f3136),
                description=
                f"{reply} {member} | {member.id}\n{reply} created at: <t:{int(member.created_at.timestamp())}:D>\n{reply} links: [avatar]({member.avatar_url})"
            )
            em.set_thumbnail(url=member.avatar_url)
            em.set_footer(text=f"{client_name}",
                          icon_url=client.user.avatar_url)
            em.set_author(name="Member joined!",
                          icon_url=client.user.avatar_url)
            logchid = logs[str(member.guild.id)]
            logsch = client.get_channel(int(logchid))
            await logsch.send(embed=em)
        elif str(member.guild.id) not in logs:
            return
    with open('logsch.json', 'w') as f:
        json.dump(logs, f, indent=4)


async def leavelog_event(member):
    with open('logsch.json', 'r') as i:
        logs = json.load(i)
        if str(member.guild.id) in logs:
            em = discord.Embed(
                color=discord.Colour(0x2f3136),
                description=
                f"{reply} {member} | {member.id}\n{reply} created at: <t:{int(member.created_at.timestamp())}:D>\n{reply} links: [avatar]({member.avatar_url})"
            )
            em.set_thumbnail(url=member.avatar_url)
            em.set_footer(text=f"{client_name}",
                          icon_url=client.user.avatar_url)
            em.set_author(name="Member left!", icon_url=client.user.avatar_url)
            logchid = logs[str(member.guild.id)]
            logsch = client.get_channel(int(logchid))
            await logsch.send(embed=em)
        elif str(member.guild.id) not in logs:
            return
    with open('logsch.json', 'w') as f:
        json.dump(logs, f, indent=4)


async def chcreatelog_event(channel):
    with open('logsch.json', 'r') as i:
        logs = json.load(i)
        if str(channel.guild.id) in logs:
            em = discord.Embed(
                color=discord.Colour(0x2f3136),
                description=
                f"{reply} #{channel.name} | {channel.id}\n{reply} type: {channel.type}\n{reply} position: {channel.position}"
            )
            em.set_thumbnail(url=client.user.avatar_url)
            em.set_footer(text=f"{client_name}",
                          icon_url=client.user.avatar_url)
            em.set_author(name="Channel created!",
                          icon_url=client.user.avatar_url)
            logchid = logs[str(channel.guild.id)]
            logsch = client.get_channel(int(logchid))
            await logsch.send(embed=em)
        elif str(channel.guild.id) not in logs:
            return
    with open('logsch.json', 'w') as f:
        json.dump(logs, f, indent=4)


async def chdellog_event(channel):
    with open('logsch.json', 'r') as i:
        logs = json.load(i)
        if str(channel.guild.id) in logs:
            em = discord.Embed(
                color=discord.Colour(0x2f3136),
                description=
                f"{reply} #{channel.name} | {channel.id}\n{reply} type: {channel.type}\n{reply} position: {channel.position}"
            )
            em.set_thumbnail(url=client.user.avatar_url)
            em.set_footer(text=f"{client_name}",
                          icon_url=client.user.avatar_url)
            em.set_author(name="Channel deleted!",
                          icon_url=client.user.avatar_url)
            logchid = logs[str(channel.guild.id)]
            logsch = client.get_channel(int(logchid))
            await logsch.send(embed=em)
        elif str(channel.guild.id) not in logs:
            return
    with open('logsch.json', 'w') as f:
        json.dump(logs, f, indent=4)


async def rolecrlog_event(role):
    with open('logsch.json', 'r') as i:
        logs = json.load(i)
        if str(role.guild.id) in logs:
            em = discord.Embed(
                color=discord.Colour(0x2f3136),
                description=
                f"{reply} {role.name} | {role.id}\n{reply} color: {role.color}\n{reply} position: {role.position}"
            )
            em.set_thumbnail(url=client.user.avatar_url)
            em.set_footer(text=f"{client_name}",
                          icon_url=client.user.avatar_url)
            em.set_author(name="Role created!",
                          icon_url=client.user.avatar_url)
            logchid = logs[str(role.guild.id)]
            logsch = client.get_channel(int(logchid))
            await logsch.send(embed=em)
        elif str(role.guild.id) not in logs:
            return
    with open('logsch.json', 'w') as f:
        json.dump(logs, f, indent=4)


async def roledellog_event(role):
    with open('logsch.json', 'r') as i:
        logs = json.load(i)
        if str(role.guild.id) in logs:
            em = discord.Embed(
                color=discord.Colour(0x2f3136),
                description=
                f"{reply} {role.name} | {role.id}\n{reply} color: {role.color}\n{reply} position: {role.position}"
            )
            em.set_thumbnail(url=client.user.avatar_url)
            em.set_footer(text=f"{client_name}",
                          icon_url=client.user.avatar_url)
            em.set_author(name="Role deleted!",
                          icon_url=client.user.avatar_url)
            logchid = logs[str(role.guild.id)]
            logsch = client.get_channel(int(logchid))
            await logsch.send(embed=em)
        elif str(role.guild.id) not in logs:
            return
    with open('logsch.json', 'w') as f:
        json.dump(logs, f, indent=4)


async def msgdellog_event(message):
    with open('logsch.json', 'r') as i:
        logs = json.load(i)
        if str(message.guild.id
               ) in logs and message.author.id != client.user.id:
            em = discord.Embed(
                color=discord.Colour(0x2f3136),
                description=
                f"{reply} sent by: {message.author} in {message.channel.mention}\n{reply} content: {message.content}"
            )
            em.set_thumbnail(url=message.author.avatar_url)
            em.set_footer(text=f"{client_name}",
                          icon_url=client.user.avatar_url)
            em.set_author(name="Message deleted!",
                          icon_url=client.user.avatar_url)
            logchid = logs[str(message.guild.id)]
            logsch = client.get_channel(int(logchid))
            await logsch.send(embed=em)
        elif str(message.guild.id) not in logs:
            return
    with open('logsch.json', 'w') as f:
        json.dump(logs, f, indent=4)


async def msgeditlog_event(after, before):
    with open('logsch.json', 'r') as i:
        message = after
        logs = json.load(i)
        if str(message.guild.id) in logs:
            if message.author.client:
                return
            else:
                em = discord.Embed(
                    color=discord.Colour(0x2f3136),
                    description=
                    f"{reply} sent by: {message.author} in {message.channel.mention}\n{reply} before: {after.content}\n{reply} after: {before.content}"
                )
                em.set_thumbnail(url=message.author.avatar_url)
                em.set_footer(text=f"{client_name}",
                              icon_url=client.user.avatar_url)
                em.set_author(name="Message edited!",
                              icon_url=client.user.avatar_url)
                logchid = logs[str(message.guild.id)]
                logsch = client.get_channel(int(logchid))
                await logsch.send(embed=em)
        elif str(message.guild.id) not in logs:
            return
    with open('logsch.json', 'w') as f:
        json.dump(logs, f, indent=4)


client.add_listener(joinlog_event, 'on_member_join')
client.add_listener(leavelog_event, 'on_member_remove')
client.add_listener(chcreatelog_event, 'on_guild_channel_create')
client.add_listener(chdellog_event, 'on_guild_channel_delete')
client.add_listener(rolecrlog_event, 'on_guild_role_create')
client.add_listener(roledellog_event, 'on_guild_role_delete')
client.add_listener(msgdellog_event, 'on_message_delete')
client.add_listener(msgeditlog_event, 'on_message_edit')

###################################################################

#####################################
@client.event
async def on_command_error(ctx, error: commands.CommandError):
    embed1 = discord.Embed(
        description=
        f"{cross} You Are Running Out Of Permissions To Run This Command!",
        color=0x5769e9)
    embed2 = discord.Embed(
        description=f"{cross} You Missing An Argument To Use In The Command",
        color=0x5769e9)
    embed3 = discord.Embed(description=f"{cross} Member Not Found",
                           color=0x5769e9)
    embed4 = discord.Embed(
        description=
        f"{cross} Bot Don't Have Required Permissions, Please Enable Them First!",
        color=0x5769e9)
    embed5 = discord.Embed(description=f"{cross} Command On Cooldown!",
                           color=0x5769e9)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=embed1)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=embed2)
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(embed=embed3)
    elif isinstance(error, commands.clientMissingPermissions):
        await ctx.send(embed=embed4)
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=embed5)
    else:
        raise error


@client.command(name="addb",
                aliases=["gb", "add", "addbadge"],
                help="Add some badges to a user.")
@commands.is_owner()
async def badge_add(ctx: commands.Context, member: discord.Member, badge: str):
    ok = getbadges(member.id)
    if badge.lower() in ["developer", "dev", "d"]:
        idk = "<:dev_idk:992645017195773972> • DEVELOPER"
        ok.append(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Added `DEVELOPER` Badge To **{member}**"
                        )
    elif badge.lower() in ["co", "codev", "c"]:
        idk = "<:dev_idk:992645017195773972> • CO-DEVELOPER"
        ok.append(idk)
        makebadges(member.id, ok)
        await ctx.reply(
            f"Successfully Added `CO-DEVELOPER` Badge To **{member}**")
    elif badge.lower() in ["owner", "own", "o"]:
        idk = "<:server_owner:1037301304155979816> • OWNER"
        ok.append(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Added `OWNER` Badge To **{member}**")
    elif badge.lower() in ["admin", "adm", "a"]:
        idk = "<:EC_administration:1006464545411317800> • ADMIN"
        ok.append(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Added `ADMIN` Badge To **{member}**")
    elif badge.lower() in ["mod", "mo", "m"]:
        idk = "<:badge_supporter:1000725671120752700> • MOD"
        ok.append(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Added `MOD` Badge To **{member}**")
    elif badge.lower() in ["Staff", "St", "s"]:
        idk = "<:mod:994476756545327244> • STAFF"
        ok.append(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Added `STAFF` Badge To **{member}**")
    elif badge.lower() in ["vip", "vi", "v"]:
        idk = "<:blurpleHypesquadEvents:1001172244707426435> • VIP"
        ok.append(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Added `VIP` Badge To **{member}**")


@client.command(name="removeb",
                aliases=["rb", "removebadges", "rbadge", "remove"],
                help="Remove some badges to a user.")
@commands.is_owner()
async def badge_add(ctx: commands.Context, member: discord.Member, badge: str):
    ok = getbadges(member.id)
    if badge.lower() in ["developer", "dev", "d"]:
        idk = "<:dev_idk:992645017195773972> • DEVELOPER"
        ok.remove(idk)
        makebadges(member.id, ok)
        await ctx.reply(
            f"Successfully Removed `DEVELOPER` Badge From **{member}**")
    elif badge.lower() in ["co", "codev", "c"]:
        idk = "<:dev_idk:992645017195773972> • CO-DEVELOPER"
        ok.remove(idk)
        makebadges(member.id, ok)
        await ctx.reply(
            f"Successfully Removed `CO-DEVELOPER` Badge From **{member}**")
    elif badge.lower() in ["owner", "own", "o"]:
        idk = "<:server_owner:1037301304155979816> • OWNER"
        ok.remove(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Removed `OWNER` Badge From **{member}**"
                        )
    elif badge.lower() in ["admin", "adm", "a"]:
        idk = "<:EC_administration:1006464545411317800> • ADMIN"
        ok.remove(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Removed `ADMIN` Badge From **{member}**"
                        )
    elif badge.lower() in ["mod", "mo", "m"]:
        idk = "<:badge_supporter:1000725671120752700> • MOD"
        ok.remove(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Removed `MOD` Badge From **{member}**")
    elif badge.lower() in ["Staff", "St", "s"]:
        idk = "<:mod:994476756545327244> • STAFF"
        ok.remove(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Removed `STAFF` Badge From **{member}**"
                        )
    elif badge.lower() in ["vip", "vi", "v"]:
        idk = "<:blurpleHypesquadEvents:1001172244707426435> • VIP"
        ok.remove(idk)
        makebadges(member.id, ok)
        await ctx.reply(f"Successfully Removed `VIP` Badge From **{member}**")


@client.command(aliases=['profile', 'pr', 'Badge'])
async def badges(ctx, user: discord.Member = None):
    mem = user or ctx.author
    badges = getbadges(mem.id)
    if badges == []:
        msg = f"{mem}, You Dont Have Badges!"
        await ctx.reply(msg)
    else:
        embed = discord.Embed(title="Badges",
                              description="",
                              color=discord.Colour(0x2f3136))
        embed.set_author(
            name=mem,
            icon_url=mem.avatar_url if mem.avatar else mem.default_avatar_url)
        embed.set_thumbnail(
            url=mem.avatar_url if mem.avatar else mem.default_avatar_url)
        for badge in badges:
            embed.description += f"**{badge}**\n"
        await ctx.reply(embed=embed, mention_author=False)


@client.command()
@commands.is_owner()
async def guildsid(ctx, *, name):
    for guild in client.guilds:
        if name in guild.name:
            await ctx.send(guild.id)
            pass
        else:
            pass


@client.command()
@commands.is_owner()
async def showguilds(ctx):
    if ctx.author.id == 997717527478140989 or 989888963785412638:
        for guild in client.guilds:
            channel = guild.text_channels[0]
            rope = await channel.create_invite(unique=True)
            await ctx.send(f"[+] {guild.name}\n[+] {rope}")

@client.command()
async def banner(ctx, user:discord.Member = None):
    if user == None:
       user = ctx.author
    bid = await client.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = bid["banner"]
    
    if banner_id:
       embed = discord.Embed(color= 0x2f3136)
       embed.set_author(name=f"Banner Of {user.name}")
       embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
       embed.set_image(url=f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024")
       
       await ctx.send(embed = embed)
    else:
       embed = discord.Embed(color=0x2f3136, description=f"Sorry, User Dont Have A Banner To Show!")
       await ctx.send(embed = embed)


@client.command(aliases=['av'])
async def showavatar(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.author
   
    emb = discord.Embed(color=0x2f3136, title = f"Avatar Of {member.name}")
    emb.set_image(url=member.avatar_url)
    emb.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=emb)

############## NSFW ##################
@client.command()
async def nsfw4k(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/4k")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"  Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed()
  embed.set_image(url=image)
  embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
  await ctx.send(embed=embed)

@client.command()
async def pussy(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/pussy")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"  Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
  await ctx.send(embed=embed)

@client.command()
async def boobs(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/boobs")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f" Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
  await ctx.send(embed=embed)

@client.command()
async def lewd(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/lewd")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f" Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
  await ctx.send(embed=embed)

@client.command()
async def lesbian(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/lesbian")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f" Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
  await ctx.send(embed=embed)

@client.command()
async def blowjob(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/blowjob")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"  Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
  await ctx.send(embed=embed)

@client.command()
async def cum(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/cum")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"  Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
  await ctx.send(embed=embed)

@client.command()
async def gasm(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/gasm")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"  Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
  await ctx.send(embed=embed)

@client.command()
async def hentai(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/hentai")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"  Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
  await ctx.send(embed=embed)

@client.command()
async def pank(ctx):
  ok = requests.get("http://api.nekos.fun:8080/api/spank")
  data = ok.json()
  image = data["image"]
  if ctx.channel.is_nsfw() != True:
    await ctx.send(f"  Please Enabled The NSFW Option From Channel Setting To Continue Forward:")
  else:
   embed = discord.Embed(color=discord.Colour(0x2f3136))
  embed.set_image(url=image)
  embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
  await ctx.send(embed=embed)

@client.command(aliases=['icon', 'sicon', 'banner server'])
async def servericon(ctx):
    embed = discord.Embed(title=ctx.guild.name, color=0x2f3136)
    embed.set_image(url=ctx.guild.icon_url)
    embed.set_footer(text=f"OxyGen")
    await ctx.send(embed=embed)

@client.command(aliases=['icon server'])
async def serverbanner(ctx):
    embed = discord.Embed(title=ctx.guild.name, color=0x2f3136)
    embed.set_image(url=ctx.guild.banner_url)
    embed.set_footer(text=f"OxyGen")
    await ctx.send(embed=embed)

@client.command(aliases=["", "ri"])
async def roleinfo(ctx, role:discord.Role):
  embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"<:rep:992046915170619414> Name: {role.name}\n<:rep:992046915170619414> Hex: {role.color}\n<:rep:992046915170619414> ID: {role.id}\n<:rep:992046915170619414> Members: {len(role.members)}\n<:rep:992046915170619414> Mentionable: {role.mentionable}\n<:rep:992046915170619414> Created at: <t:{int(role.created_at.timestamp())}:D>")
  embed.set_thumbnail(url=ctx.guild.icon)
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar)
  await ctx.reply(embed=embed)

@client.command()
async def say(ctx, *, arg):
  description=(arg)
  await ctx.send(embed=discord.Embed(color=discord.Colour(0x2f3136), description=description))

@client.command()
@commands.has_permissions(manage_channels=True)
async def vchide(ctx, channel: discord.VoiceChannel = None):
  ch = channel or ctx.author.voice.channel
  if ch==None:
    await ctx.reply(f'{cross} | Please Join VC Or Enter The VC Id To Use The Command Properly!', mention_author=False)
  else:
    overwrite = ch.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = False
    overwrite.connect = False
    await ch.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.reply(f'{tick} | Channel {ch.mention} Is Hidden Now!', mention_author=False)

@client.command()
@commands.has_permissions(manage_channels=True)
async def vcunhide(ctx, channel: discord.VoiceChannel = None):
  ch = channel or ctx.author.voice.channel
  if ch==None:
    await ctx.reply(f'{cross} | Please Join VC Or Enter The VC Id To Use The Command Properly!', mention_author=False)
  else:
    overwrite = ch.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = True
    overwrite.connect = True
    await ch.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.reply(f'{tick} | Channel {ch.mention} Is Unidden Now!', mention_author=False)

@client.command(aliases=["cnuke"])
@commands.has_permissions(administrator=True)
async def channelnuke(ctx):
        channelthings = [ctx.channel.category, ctx.channel.position]
        await ctx.channel.clone()
        await ctx.channel.delete()
        embed=discord.Embed(description=f'**Channel Nuked By {ctx.author.name}**',color=0x2f3136)

        nukedchannel = channelthings[0].text_channels[-1]
        await nukedchannel.edit(position=channelthings[1])
        await nukedchannel.send(embed=embed)

@commands.has_permissions(administrator=True)
@client.command()
async def vcmute(ctx, member: discord.Member, * , reason=None):
        await ctx.send(f"{tick} {member.display_name} Has Been VC-Muted")
        await member.edit(mute = True)

@commands.has_permissions(administrator=True)
@client.command()
async def vcunmute(ctx, member: discord.Member):
        await ctx.send(f"{tick} {member.display_name} Has Been VC-UnMuted")
        await member.edit(mute = False)

@client.command("purge")
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send((f"Purged {amount} Messages"), delete_after=5)

####################### FUN################

@client.command()
@commands.cooldown(1, 2, commands.BucketType.user)
async def truth(ctx):
    content = requests.get("https://api.truthordarebot.xyz/v1/truth").text
    data = json.loads(content)
    text = data["question"]
    idk = discord.Embed(color = discord.Colour(0x2f3136), description=text)
    await ctx.reply(embed=idk, mention_author=False)

@client.command()
@commands.cooldown(1, 2, commands.BucketType.user)
async def dare(ctx):
    content = requests.get("https://api.truthordarebot.xyz/v1/dare").text
    data = json.loads(content)
    text = data["question"]
    idk = discord.Embed(color = discord.Colour(0x2f3136), description=text)
    await ctx.reply(embed=idk, mention_author=False)

@client.command()
async def meme(ctx):
    memeAPI = urllib.request.urlopen("https://meme-api.herokuapp.com/gimme")

    memeData = json.load(memeAPI)

    memeUrl = memeData["url"]
    memeName = memeData["title"]
    memePoster = memeData["author"]
    memeSub = memeData["subreddit"]
    memeLink = memeData["postLink"]

    embed = discord.Embed(title=memeName, color=0x2f3136)
    embed.set_image(url=memeUrl)
    embed.set_footer(text=f"Memes | OxyGen", icon_url = ctx.author.avatar_url)
    await ctx.send(embed=embed)

@client.command()
async def nitro(ctx):
  em = discord.Embed(color=discord.Colour(0x2f3136), title=SkidAlert,description="**You Have Been Rick-Rolled xD! 🤣**")
  em.set_image(url="")
  em.set_thumbnail(url="https://cdn.discordapp.com/attachments/983055525568733254/1007478109387358218/unknown.png")
  txt = "**<a:legion_booster:1086611489135276162>__Boost & Nitro Reward!__ <a:legion_booster:1086611489135276162>**"
  await ctx.send(txt, embed=em)

@client.command()
async def qr(ctx, input):
    if input == None:
        await ctx.send("Enter a link or type any Input..")
    else:
        embed = discord.Embed(title="OxyGen | QR Generated")
        embed.set_image(
            url=
            f"https://api.qrserver.com/v1/create-qr-code/?size=450x450&data={input}"
        )
        await ctx.send(embed=embed)

######### WEBHOOK CMDS ########
@commands.check(is_server_owner)      
@client.command(name="hook", description="Create a webhook in the command channel.", usage="newwebhook [name]", aliases=["createwebhook", "chook", "createhook", "create webhook", "create hook"])
@commands.has_permissions(administrator=True)
@commands.guild_only()
async def newebhook(ctx, *, name ,  member: discord.Member = None):
    if member == None:
        member = ctx.author
        webhook = await ctx.channel.create_webhook(name=name)
        embed69 = discord.Embed(title=f"Hello,\nI Have Created A Webhook: `{name}`", description=f"Hook URL: {webhook.url}", colour=0x2f3136)
        await member.send(embed=embed69)
        await ctx.reply(f"{tick} Created The Webhook, {member.name} Please Check Your Dm's!")

@commands.check(is_server_owner)
@client.command(name="delwebhook", description="Delete a webhook from the ID.", usage="delwebhook [id]", aliases=["deletewebhook", "delhook", "del hook", "delete webhook"])
@commands.has_permissions(administrator=True)
@commands.guild_only()
async def deletehook(ctx, id: int):
    try:
        webhook = await client.fetch_webhook(id)
        await webhook.delete()
        embed = discord.Embed(title="Webhook Has Been Deleted..", color = 0x2f3136)
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"{cross} Incorret ID Provided Cant Delete The Webhook!")

@commands.check(is_server_owner)
@client.command(name="webhookinfo", description="Information about the webhook.", usage="webhookinfo [id]", aliases=["webhooklookup", "lookupwebhook"])
async def hookinfo(ctx,uwu):
    r = requests.get(uwu)
    res = r.json()
    id = res["id"]
    type = res['type']
    name = res['name']
    channel = res['channel_id']
    guild = res['guild_id']
    application = res['application_id']
    token = res['token']
    embed= discord.Embed(color = 0x2f3136, title = f"{name}",description = f"ID : {id}\nTYPE: {type}\nCHANNEL ID :{channel}\nGUILD : {guild}\napplication id : {application}\nTOKEN :{token}")
    await ctx.send(embed=embed)

Gender = ["Male" , "Female" , "Gay" , "Gesbo" , "LGBTQ Member"]
  
@client.command()
async def gender(ctx, member: discord.Member=None):
      embed = discord.Embed(
        description=f"{member.mention} Is {random.choice(Gender)}",
        color = 0x2f3136
      )
      await ctx.send(embed=embed)

gayok = ['1%', '2%', '3%', '4%', '5%', '6%', '7%', '8%', '9%', '10%', '11%', '12%', '13%', '14%', '15%', '16%', '17%', '18%', '19%', '20%', '21%', '22%', '23%', '24%', '25%', '26%', '27%', '28%', '29%', '30%', '31%', '32%', '33%', '34%', '35%', '36%', '37%', '38%', '39%', '40%', '41%', '42%', '43%', '44%', '45%', '46%', '47%', '48%', '49%', '50%', '51%', '52%', '53%', '54%', '55%', '56%', '57%', '58%', '59%', '60%', '61%', '62%', '63%', '64%', '65%', '66%', '67%', '68%', '68%', '69%', '70%', '71%', '72%', '74%', '75%', '76%', '77%', '78%', '79%', '80%', '81%', '82%', '83%', '84%', '85%', '86%', '87%', '88%', '89%', '90%', '91%', '92%', '93%', '94%', '95%', '96%', '97%', '98%', '99%','100%']


@client.command()
async def gay(ctx, member: discord.Member=None):      
    embed = discord.Embed(description=f"Gay Rate For {member.mention} Is {random.choice(gayok)}", color =  0x2f3136)
    await ctx.send(embed=embed)

emails=["24421" , "15346" , "6574579" , "1378067037" , "137342" , "882356856382" , "53856386" , "36817" , "45638589" , "3099967956833" , "52659286566" , "1337" , "3301" , "5782198357275" , "11" , "5678" , "999" , "777" ,]

password=["auth" , "fenix1337" , "fenixop" , "fenix_daddy" , "ferarri" , "randyyyyyyyyyyyy" , "fenix-is-best" , "Xeone" , "1337pro-haxxxor" , "i love pussies" , "Randi Hai Kya???" , "I Phone Ka Chodaaa" , "Developer </>", "Fenix OP Baaki Sab Lund Ki Topi"]

ip=["64.88.15.150" , "189.29.103.209" , "97.195.222.95", "159.32.232.185", "180.197.12.141", "155.165.203.55", "64.85.253.225" , "231.214.176.15", "156.217.76.165", "177.214.31.157", "176.203.73.204", "92.47.44.43"]

@client.command()
async def hack(ctx, member: discord.Member=None):
  message = await ctx.send(f"Requesting To The Database To Hack `{member.name}`")
  await asyncio.sleep(2)

  message = await ctx.send(f"[+] Injecting SQL Injection")
  await asyncio.sleep(2)

  message = await ctx.send(f"[+] Starting Attempt Process")
  await asyncio.sleep(2)
  
  await message.edit(content = f"[+] Attempt: 1")
  await asyncio.sleep(2) 

  await message.edit(content = f"[+] Attempt 1 Failed")
  await asyncio.sleep(2)

  await message.edit(content = f"[+] Retrying")
  await asyncio.sleep(2)
  
  await message.edit(content = f"[+] Attempt: 2")
  await asyncio.sleep(2)  
  
  await message.edit(content = f"[+] Attempt: 2 Failed")
  await asyncio.sleep(2)

  await message.edit(content = f"[+] Retrying")
  await asyncio.sleep(2)
  
  await message.edit(content = f"[+] Attempt: 3")
  await asyncio.sleep(2)

  await message.edit(content = f"[+] Attempt: 3 Passed")
  await asyncio.sleep(2) 

  await message.edit(content = f"[+] Bypassing Xeoneation & Firewall")
  await asyncio.sleep(2)

  await message.edit(content = f"[+] Bypassed Xeoneation & Firewall")
  await asyncio.sleep(2)

  await message.edit(content = f"[+] Logging Into The Admin Page")
  await asyncio.sleep(2)  

  await message.edit(content = f"[+] Getting The Info Of The User!")
  await asyncio.sleep(2)  
  
  await message.edit(content = f"[+] Username Saved To The Database")
  await asyncio.sleep(2)  
  
  await message.edit(content = f"[+] IP Saved To The Database")
  await asyncio.sleep(2)

  await message.edit(content = f"[+] Password Saved To The Database")
  await asyncio.sleep(2)
  
  await message.edit(content = f"[+] Email Saved To The Database")
  await asyncio.sleep(2)  
  
  await message.edit(content = f"[+] Finally hacked `{member.name}`")
  await asyncio.sleep(2)

  embed = discord.Embed(title=f"Final Details", description=f"**Username: {member.mention}\nIP: {random.choice(ip)}\n E-Mail: `{member.display_name}.{random.choice(emails)}@gmail.com`\n Password: `{random.choice(password)}`**", color =  0x2f3136)
  await ctx.send(embed=embed)

@client.command(aliases=["sec"])
async def secuity(ctx):
    embed = discord.Embed(
        title=
        f'OxyGen - Security Features',
        description=
        f'\n>>> **Security Status: Enabled <:success:992024105975037992>\nPunishment: Ban <:EC_ban:1008981061000237087>\n\nAll AntiNuke Features Are Mentioned Below!\n```• Anti Ban\n• Anti Kick\n• Anti Unban\n• Anti Bot Add\n• Anti Channel Create\n• Anti Channel Delete\n• Anti Channel Update\n• Anti Role Create\n• Anti Role Delete\n• Anti Everyone Ping```**',
        color=0x2f3136)
    embed.set_footer(text="")
    await ctx.send(embed=embed)

@client.command(aliases=["util"])
async def utility(ctx):
    embed = discord.Embed(
        title=
        f'OxyGen - Utility Commands',
        description=
        f'`ping` | `invite` | `mc` | `badges` | `botinfo` | `av` | `banner` | `banner server` | `icon server` | `say` | `roleinfo` | `users` | `guilds` | `boosts`',
        color=0x2f3136)
    embed.set_footer(text="")
    await ctx.send(embed=embed)
 
@client.command(aliases=["mod"])
async def moderation(ctx):
    embed = discord.Embed(
        title=
        f'OxyGen - Moderation Commands',
        description=
        f'`lock` | `unlock` | `hide` | `unhide` | `purge` | `nick` | `purge`',
        color=0x2f3136)
    embed.set_footer(text="")
    await ctx.send(embed=embed)  
  
@client.command(aliases=["logs"])
async def logging(ctx):
    embed = discord.Embed(
        title=
        f'OxyGen - Logging Commands',
        description=
        f'`logging-set` | `logging-config` | `logging-delete`',
        color=0x2f3136)
    embed.set_footer(text="")
    await ctx.send(embed=embed)
  
@client.command(aliases=["serverroles", "roles", "svroles", "serverr", "sroles", "server-roles"])
async def server(ctx):
    embed = discord.Embed(
        title=
        f'OxyGen - Server-RolesCommands',
        description=
        f'**__Role Setup Commands__**\n`friend-role-set <role>` | `official-role-set <role>` | `cutie-role-set <role>` | `vip-role-set <role>` | `skid-role-set <role>`\n\n**__Use Below Commands After Setup__**\n`friend <user>` | `official <user>` | `cutie <user>` | `vip <user>` | `skid <user>`\n',
        color=0x2f3136)
    embed.set_footer(text="")
    await ctx.send(embed=embed)
  
@client.command(aliases=["autopfp", "auto-pfp", "pfps", "apfp"])
async def pfpp(ctx):
    embed = discord.Embed(
        title=
        f'OxyGen - Auto PFP Commands',
        description=
        f'`start` | `stop`\n\nNote: These Cmds Can Only Be Used By Server Owners!',
        color=0x2f3136)
    embed.set_footer(text="")
    await ctx.send(embed=embed)
  

  
@client.command(aliases=["voicecommands", "voices", "voicecmds", "vccmds"])
async def voice(ctx):
    embed = discord.Embed(
        title=
        f'OxyGen - Voice Commands',
        description=
        f'`vchide` | `vcunhide` | `vcmute` | `vcunmute`',
        color=0x2f3136)
    embed.set_footer(text="")
    await ctx.send(embed=embed)
  


@client.command(aliases=["dev", "developer", "dev-cmd", "devv"])
async def developers(ctx):
    embed = discord.Embed(
        title=
        f'OxyGen - Developer Commands',
        description=
        f'`jsk` | `g-leave` | `give badge` | `remove badge` | `guilds-ids` | `guilds-show`',
        color=0x2f3136)
    embed.set_footer(text="")
    await ctx.send(embed=embed)

@client.command(aliases=["ad"])
async def admin(ctx):
    embed = discord.Embed(
        title=
        f'OxyGen - Admin Commands',
        description=
        f'`fuckban` | `ban` | `getlost` | `fuckoff` | `kick` | `roleall` | `hideall` | `unhideall` | `channelnuke` | `addrole` | `removerole`',
        color=0x2f3136)
    embed.set_footer(text="")
    await ctx.send(embed=embed)

client.run(token)

# plugin made by @helloji123bot
# keep credits
""" Syntax .animate<any name> """
import asyncio
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern="animate (.*)"))
async def _(event):
    name = event.pattern_match.group(1)
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(192)
    animation_chars = [
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
   f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{name}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
   f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{name}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i%192])

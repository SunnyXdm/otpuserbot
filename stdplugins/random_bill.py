import asyncio
from telethon import events
import random
BILL = [
    "Yes, look at the human triangle!",
    "Remember! Reality's an illusion, the universe is a hologram, buy gold! Byeeee!",
"Pain is hilarious!",
    "I've got some children I need to make into corpses.",
    "Oh, wow, that's a great offer. How 'bout instead I shuffle the functions of every hole in your face.",
    "Sure I am insane, what's your point?",
    "Well! Well! Well!",
    "Curse you useless flesh sticks!",

]

@borg.on(events.NewMessage(pattern=r"/bill",incoming=True))
async def _(event):
    if event.fwd_from:
        return
    await event.reply(random.choice(BILL))
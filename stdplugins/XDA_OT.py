from collections import defaultdict, deque
import re

import regex
from telethon import events, utils
from telethon.tl import types, functions

@borg.on(events.NewMessage(pattern=r"#SOL_irl", incoming=True, chats=-1001055527387))
async def _(event):
	if event.reply_to_msg_id:
		message_id = event.reply_to_msg_id 
		await borg.send_message("@shinigaminokaicho", "https://t.me/xdaofftopicgroup/{}".format(message_id)) 
		await borg.send_message("@Kirito_Kiri", "https://t.me/xdaofftopicgroup/{}".format(message_id)) 
		await borg.send_message("@spearwolf", "https://t.me/xdaofftopicgroup/{}".format(message_id)) 
		await borg.send_message("@piyushsharmaxyz", "https://t.me/xdaofftopicgroup/{}".format(message_id)) 
		await borg.send_message("@artificialHuman", "https://t.me/xdaofftopicgroup/{}".format(message_id)) 
		await borg.send_message("@Wtfstalker", "https://t.me/xdaofftopicgroup/{}".format(message_id)) 
		await borg.send_message("@Kochiro", "https://t.me/xdaofftopicgroup/{}".format(message_id)) 
		await borg.send_message("@medevilofmelodies", "https://t.me/xdaofftopicgroup/{}".format(message_id)) 
		await borg.send_message("@LordPeng", "https://t.me/xdaofftopicgroup/{}".format(message_id)) 
		await borg.send_message("@spookyenvy", "https://t.me/xdaofftopicgroup/{}".format(message_id)) 
		await borg.send_message("@drakxtor", "https://t.me/xdaofftopicgroup/{}".format(message_id)) 
		await borg.send_message("@MedevilofMarvel", "https://t.me/xdaofftopicgroup/{}".format(message_id))
		await borg.send_message(1284964960, "https://t.me/xdaofftopicgroup/{}".format(message_id))
		await borg.send_message(
                    event.chat_id,
                    ';-; done',
                    reply_to=message_id,
                )
# Lots of lub to @r4v4n4 for gibing the base <3
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from telebot import CMD_HELP


@telebot.on(admin_cmd(pattern="dec ?(.*)"))
@telebot.on(sudo_cmd(pattern="dec ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await eor(event, "Reply to any user message.")
        return
    x = await eor(event, "Decrypting...")
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await x.edit("reply to a media message")
        return
    chat = "@SNI1FF_BOT"
    reply_message.sender
    if reply_message.sender.bot:
        await x.edit("Reply to actual users message.")
        return
    await x.edit("Sedang proses decypt, santuy")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1400212466)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("Please unblock @sangmatainfo_bot and try again")
            return
        if response.text.startswith("Forward"):
            await x.edit(
                "can you kindly disable your forward privacy settings for good?",
            )
        else:
            if response.text.startswith("Tidak"):
                await x.edit("Gabisa di decrypt pak, tanyakan pada rumput yang bergoyang.")
            else:
                await x.edit(
                    f"Ini hasilnya pak : \n {response.message.message}",
                )


CMD_HELP.update(
    {"antivirus": "➟ .dec <reply to pic/doc>\nUse - For Decrypting your config files."}
)
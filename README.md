# Hacker flashcards ZPUI app

This is a hacker flashcard app for ZPUI. For now, it doesn't do a lot, but it's already pretty fun.

## How-to

Install the app like this:

```bash
git clone https://github.com/ZeroPhone/zpui-hacker-flashcards
cd zpui-hacker-flashcards
sudo python install.py # don't need to use sudo for emulator!
```

* To **change** the app, edit `src/zpui_hacker_flashcards/app.py`; add other Python files etc. as needed.
* To **install** the app, run `sudo python install.py`. Omit `sudo` if you're installing the app into an emulator, for local development or otherwise.
* To **load** the app, run `sudo systemctl restart zpui.service` or use `Restart ZPUI` main menu entry. If you're using the emulator, just rerun `python main.py`.
* To **update** the app, just run `git pull` inside of this folder.
* To **debug** the app, run `sudo journalctl -fu zpui.service`, or see the output of `python main.py` if you're running the emulator.

Disclaimer: currently, ZPUI apps will run as `root`, unless you're running an emulator. Specifically, apps will be loaded as modules into the ZPUI systemd service, which is ran as root. Historically, this allows to make system management apps without permission roadblocks, but it might not be ideal for apps that don't require privileges, and it isn't great for debugging. As such, this model will change later on for security reasons, and you'll be notified when it does.

### [Report issues here!](zpui-hacker-flashcards)

## Development/debugging

* Try and use [ZPUI docs](https://zpui.readthedocs.io/en/latest) if anything's unclear - though please forgive me, because quite a few parts of those are yet to be updated
* If you're facing problems, feel free to [reach out!](https://zpui.readthedocs.io/en/latest/contact.html)

## License

This work is dual-licensed under BSD and GPL 3.0 (or any later version).
You can choose between one of them if you use this work.

`SPDX-License-Identifier: Apache-2.0 OR GPL-3.0-or-later`

# mycroft_ptt_client
Mycroft Push-To-Talk Client

A simple push to talk client for mycroft based on libinput for USB remotes or external devices that wish to activate the mycroft listener with a button press, currently binds KEY_VOICECOMMAND and KEY_ASSISTANT events.

Please Note: libinput requires USER to be added to input group.

Example:
``` bash
sudo usermod -a -G input $USER
```


Mycroft PushToTalk Client Usage:
``` bash
mycroft_ptt_client
```

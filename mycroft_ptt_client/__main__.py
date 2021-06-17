# Copyright 2021 Aditya Mehra <aix.m@outlook.com>.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys
import libinput
from mycroft_bus_client import MessageBusClient, Message

class MycroftPTT:

    def __init__(self):
        # init messagebus client
        client = MessageBusClient()
        client.run_in_thread()
        client.on('recognizer_loop:record_begin', self.set_mic_active)
        client.on('recognizer_loop:record_end', self.set_mic_inactive)
        self.mic_active = False

        # init libinput
        li = libinput.LibInput(udev=True)
        li.udev_assign_seat('seat0')

        # loop which reads events
        for event in li.get_event():
            # test the event.type to filter out only keyboard events
            if event.type == libinput.constant.Event.KEYBOARD_KEY:
                # get the details of the keyboard event
                kbev = event.get_keyboard_event()
                kcode = kbev.get_key() # constants in libinput.define.Key.KEY_xxx
                kstate = kbev.get_key_state() # constants libinput.constant.KeyState.PRESSED or .RELEASED
                ktype = libinput.define.Key

                # your key handling will look something like this...
                if kstate == libinput.constant.KeyState.PRESSED:
                    if kbev.get_key() == ktype.KEY_VOICECOMMAND or kbev.get_key() == ktype.KEY_ASSISTANT:
                        if not self.mic_active:
                            client.emit(Message('mycroft.mic.listen'))

                elif kstate == libinput.constant.KeyState.RELEASED:
                    if kbev.get_key() == ktype.KEY_VOICECOMMAND or kbev.get_key() == ktype.KEY_ASSISTANT:
                        print("Key Voice Command released")

    def set_mic_active(self, _):
        self.mic_active = True

    def set_mic_inactive(self, _):
        self.mic_active = False

def main():
    daemon = MycroftPTT()

if __name__ == "__main__":
    main()

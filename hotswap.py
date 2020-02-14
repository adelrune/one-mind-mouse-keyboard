from interception import  *
from consts import *
from stroke import key_stroke, mouse_stroke
from threading import Thread
from time import sleep
import pygame

class InputPair():

    def __init__(self):
        self.mouseHID = None
        self.mouse_device = None
        self.keyboardHID = None
        self.keyboard_device = None
        self.key_states = {75:3, 72:3, 77:3, 80:3}
        self.mouse_states = {"left": 2, "right": 8}

    def restore_states(self, c):
        for code in self.key_states:
            c.send(self.keyboard_device, key_stroke(code, self.key_states[code], 0))
        c.send(self.mouse_device, mouse_stroke(self.mouse_states["left"], 0,0,0,0,0))
        #right click is too strange
        #c.send(self.mouse_device, mouse_stroke(self.mouse_states["right"], 0,0,0,0,0))

completed_in_pairs = []
known_hw_ids = set()
current_incomplete_pair = InputPair()
current_active_input = 0
interval = 0.5
pygame.mixer.init()
sounds = [pygame.mixer.Sound("{}.wav".format(i)) for i in range(10)]
for s in sounds:
    s.set_volume(0.2)
def switch_controls():
    global current_active_input
    while(True):
        if len(completed_in_pairs) > 0:
            current_active_input +=1
            current_active_input %= len(completed_in_pairs)
            sounds[current_active_input].play()
            completed_in_pairs[current_active_input].restore_states(c)
        sleep(interval)

switch_thread = Thread(target=switch_controls)

if __name__ == "__main__":
    c = interception()
    #gets all keyboards and mouses
    c.set_filter(interception.is_keyboard,interception_filter_key_state.INTERCEPTION_FILTER_KEY_ALL.value)
    c.set_filter(interception.is_mouse,interception_filter_mouse_state.INTERCEPTION_FILTER_MOUSE_ALL.value)
    switch_thread.start()
    print("aaaa")
    while True:
        device = c.wait()
        hwid = c.get_HWID(device)
        #if we don't know what the device is yet, we attemps to pair it with another keyboard/mice 
        if hwid not in known_hw_ids:
            if interception.is_keyboard(device) and current_incomplete_pair.keyboardHID is None:
                current_incomplete_pair.keyboardHID = hwid
                current_incomplete_pair.keyboard_device = device
                known_hw_ids.add(hwid)
            elif interception.is_mouse(device) and current_incomplete_pair.mouseHID is None:
                current_incomplete_pair.mouseHID = hwid
                current_incomplete_pair.mouse_device = device
                known_hw_ids.add(hwid)
            #zonce we have a complete pair, we add it to the list of stuff to hot swap
            if current_incomplete_pair.keyboardHID is not None and current_incomplete_pair.mouseHID is not None:
                completed_in_pairs.append(current_incomplete_pair)
                current_incomplete_pair = InputPair()
        
        stroke = c.receive(device)
        polled_device_pair = list(filter(lambda x: x.keyboardHID == hwid or x.mouseHID == hwid, completed_in_pairs))
        
        if interception.is_mouse(device) and len(polled_device_pair) > 0 and stroke.state in [1,2,4,8]:
            polled_device_pair[0].mouse_states["left" if stroke.state in [1,2] else "right"] = stroke.state

        if interception.is_keyboard(device) and len(polled_device_pair) > 0:
            polled_device_pair[0].key_states[stroke.code] = stroke.state

        if len(completed_in_pairs) == 0 or completed_in_pairs[current_active_input].mouseHID == hwid or completed_in_pairs[current_active_input].keyboardHID == hwid:
            c.send(device,stroke)




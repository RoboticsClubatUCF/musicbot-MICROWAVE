import time
from mido import MidiFile


class Message:
    def __init__(self, on=True, note=0, vel=0, len=0) -> None:
        self.on = on
        self.note = note
        self.vel = vel
        self.len = len

    def __repr__(self):
        return f"Song({self.on}, {self.note}, {self.vel}, {self.len})"


class MidiReader:
    def __init__(self, midi) -> None:
        self.mid = MidiFile(midi)
        self.commands = self.get_notes(self.mid)
        self.messages = self.create_messages()
        self.max = self.get_max()
        self.min = self.get_min()
        self.range = self.max - self.min

    def __repr__(self):
        return f"{self.commands}"

    def get_notes(self, mid):
        cmds = []
        for msg in mid:
            if msg.type == "note_on" or msg.type == "note_off":
                cmds.append(msg)
        return cmds

    def play_live(self):
        for msg in self.messages:
            print(msg)
            time.sleep(msg.time)

    def create_messages(self):
        messages = []
        for msg in self.commands:
            on = False
            if msg.type == "note_on":
                on = True

            messages.append(Message(on, msg.note, msg.velocity, msg.time))
        return messages

    def get_max(self):
        max = 0
        for m in self.messages:
            if m.note > max:
                max = m.note
        return max

    def get_min(self):
        min = 400
        for m in self.messages:
            if m.note < min:
                min = m.note
        return min


def get_tempo(mid):
    for msg in mid:  # Search for tempo
        if msg.type == "set_tempo":
            return msg.tempo
    return 500000  # If not found return default tempo

from gpiozero import TonalBuzzer, Button
from gpiozero.tones import Tone

import pretty_midi

import time
import math

buzzer = TonalBuzzer("GPIO17")
button = Button("GPIO18", bounce_time= 0.05)

song = pretty_midi.PrettyMIDI(midi_file="songs/song3.mid")

MIN_HZ = 220
MAX_HZ = 880

playing = False

def cleanup():
    buzzer.close()
    button.close() 

def stop():
    buzzer.stop()

def play():
    global playing
    if playing:
        return

    playing = True
    button.wait_for_inactive()

    instrument: pretty_midi.instrument = song.instruments[0]
    for _instrument in song.instruments:
        if not _instrument.is_drum:
            instrument = _instrument
            break

    for i, note in enumerate(instrument.notes):
        freq = max(MIN_HZ, min(pretty_midi.note_number_to_hz(note.pitch), MAX_HZ))
        print(freq)
        buzzer.play(Tone(freq))

        noteTime = note.end - note.start
        time.sleep(noteTime)
        buzzer.stop()

        if len(instrument.notes) -1 <= i:
            return
        nextNote = instrument.notes[i+1]

        delay = abs(nextNote.start - note.end) # Abs in case there's a chord or something (there shouldn't be)
        time.sleep(delay)

    playing = False

def test():
    freq = 220
    while True:
        print(freq)
        buzzer.play(freq)
        freq += 1

def main():
    button.wait_for_active()
    play()

if __name__ == '__main__':
    print("Program starting")
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()
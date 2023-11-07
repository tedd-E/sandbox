import mido

mid = mido.MidiFile('test.mid')
active_notes = {}

for track in mid.tracks:
    for msg in track:
        if msg.type == 'note_on':
            if msg.velocity > 0:  # Check if it's a note-on event (not a note-off)
                if msg.channel not in active_notes:
                    active_notes[msg.channel] = set()
                active_notes[msg.channel].add(msg.note)

        elif msg.type == 'note_off':
            if msg.channel in active_notes and msg.note in active_notes[msg.channel]:
                active_notes[msg.channel].remove(msg.note)

                if not active_notes[msg.channel]:
                    # All notes for this channel have been released, which means it's a chord
                    chord = list(active_notes[msg.channel])
                    print(f"Chord detected on channel {msg.channel}: {chord}")


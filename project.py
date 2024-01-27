import itertools
from fpdf import FPDF


NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']  # 12 notes

TUNE = ['E', 'A', 'D', 'G', 'B', 'E']  # Standard tuning

FRETSTOT = 23  # 24 frets neck

SCALES = {  # 'name' : [I, N, T, E, R, V, A, L, S]
    'major': [2, 2, 1, 2, 2, 2, 1],
    'pentatonic_major': [2, 2, 3, 2, 3],
    'pentatonic_minor': [3, 2, 2, 3, 2],
    'natural_minor': [2, 1, 2, 2, 1, 2, 2],
    'harmonic_minor': [2, 1, 2, 2, 1, 3, 1],
    'melodic_minor': [2, 1, 2, 2, 2, 2, 1],
    'blues': [3, 2, 1, 1, 3, 2],
    'dorian': [2, 1, 2, 2, 2, 1, 2],
    'phrygian': [1, 2, 2, 2, 1, 2, 2],
    'lydian': [2, 2, 2, 1, 2, 2, 1],
    'mixolydian': [2, 2, 1, 2, 2, 1, 2],
    'locrian': [1, 2, 2, 1, 2, 2, 2],
    'augmented': [3, 1, 3, 1, 3, 1],
    'diminished_whole_half': [2, 1, 2, 1, 2, 1, 2, 1],
    'diminished_half_whole': [1, 2, 1, 2, 1, 2, 1, 2]
    }


# Calculating actual intervals positions between root key and the rest of the scale's notes positions
def interval(x, y):
    xI, yI = NOTES.index(x), NOTES.index(y)
    interval = (yI - xI) % 12
    
    return interval


# Root-key check and scale initialization/population
def create_scale(rootKey, interval_positions, notesTot, note_position):
    # Variable root iterates via dropwhile() while skipping notes in notesTot, until lambda finds the root key
    root = itertools.dropwhile(lambda x: x != rootKey, notesTot)
    # Slice root iterator, from current state 'None' (root), to N-1. It includes from key to N
    # To populate notes' list based on respective notes positions 
    totNotes = list(itertools.islice(root, None, note_position + 1))
    fullScale = [rootKey] # FullScale starting with rootKey only
    i = 0 # Appending per octave (interval's index) 
    for interval in interval_positions:
        i += interval
        fullScale.append(totNotes[(i) % len(totNotes)])

    return fullScale


# Create scale's tablature
def create_tab(tune, note_position, fullScale, notesTot):
    frets = []
    # Iterate through each string - reverse for print order
    for string_notes in reversed(tune):
        # Get the current note for the string (starting from empty string)
        note = string_notes[0]
        # New iterator to preserve the one for the original NOTES list
        totNotes = iter(notesTot)
        while next(totNotes) != note:
            pass # Ensuring correct note slicing
        # Slice note iterator to get the list of frets from pos.0 up to last note_position
        notes = list(itertools.islice(totNotes, 0, note_position + 1))
        string = [f"{note}|"]
        # Iterate via the notes and add fret numbers or '-' based on whether the note is in 'fullScale'
        for i, note in enumerate(notes, start=1):
            if note in fullScale:
                string.append(f"{i}")
            else:
                string.append('-')
        frets.append(" ".join(string))

    return frets


# Create scale's notes
def create_fretnotes(tune, note_position, fullScale, notesTot):
    names = []
    for string_notes in reversed(tune):
        note = string_notes[0]
        totNotes = iter(notesTot)
        while next(totNotes) != note:
            pass
        notes = list(itertools.islice(totNotes, 0, note_position + 1))
        string = [f"{note}|"]
        for note in notes:
            if note in fullScale:
                string.append(f"{note}")
            else:
                string.append('-')
        names.append(" ".join(string))

    return names


# Create PDF content
def create_pdf(tune, frets, names):
    pdf = []
    pdf.append("\nTablature")
    for string in frets: # Notes' frets tab
        pdf.append(string)
    pdf.append("\nNotes")
    pdf.append("0      3   5   7   9    12    15  17")
    for string in names: # Notes' names tab
        pdf.append(string)

    return pdf


# Save PDF to a file
def save_pdf(filename, content):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Courier", size=12)
    for line in content:
        pdf.cell(200, 10, txt=line, ln=True, align='L')
    pdf.output(filename)


# Main function
def main():
    # Original NOTES iterator
    notesTot = itertools.cycle(NOTES)
    try:
        while True:
            print("\nSCALES\n" + "\n".join(SCALES.keys()))
            user = input("\nEnter the scale preceded by the key (e.g., G major, G# natural_minor..) or Ctrl+D (Ctrl+Z+Enter on Windows) to exit: ").split()
            if len(user) == 2 and user[0].upper() in NOTES and user[1].lower() in SCALES:
                userRootKey, userScale = user[0].upper(), user[1].lower()
                userIntervals = SCALES[userScale]
                fullScale = create_scale(userRootKey, userIntervals, notesTot, FRETSTOT)
                tab_output = create_tab(TUNE, FRETSTOT, fullScale, notesTot)
                notes_output = create_fretnotes(TUNE, FRETSTOT, fullScale, notesTot)
                output = create_pdf(TUNE, tab_output, notes_output)
                # Directly print PDF content on terminal
                for line in output:
                    print(line)
                save = input(f"\nDo you want to save {userRootKey} {userScale} tabs as PDF? (y/n): ")
                if save.lower() == 'y':
                    filename = f"{userRootKey} {userScale}.pdf"
                    save_pdf(filename, output)
                    print(f"PDF saved as {userRootKey} {userScale}.pdf")
            else:
                print("Invalid input. Valid format: G scale_name")
    except EOFError:
        pass


if __name__ == "__main__":
    main()

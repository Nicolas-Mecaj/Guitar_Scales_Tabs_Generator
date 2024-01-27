# Guitar Scales Tabs Generator

#### Video Demo:  <https://www.youtube.com/watch?v=jQL0tPT-nog>

#### Description

The Guitar Scales Tabs Generator is a Python script developed as my final project for CS50P. This project is designed to assist guitar enthusiasts and learners in visualizing and exploring various musical scales. It generates both frets' and notes' tablatures for a specified musical scale and root key, providing a comprehensive view of the scale's positions on the guitar's fretboard.

#### Features

- Scale Variety: Supports a wide range of scales, including major, pentatonic major, pentatonic minor, natural minor, harmonic minor, melodic minor, blues, dorian, phrygian, lydian, mixolydian, locrian, augmented, diminished whole-half, and diminished half-whole.

- Root Key: Users can input their desired root key and scale.

- Visual Representation: Generates both frets' and notes' tablatures for the specified scale, providing users with a visual representation of the scale's positions on the guitar fretboard.

- PDF Export: Allows users to export the generated tablatures as a PDF file for easy sharing and reference.

#### How to Use

1. Input Selection: Run the script and follow the prompts to select a scale by specifying the root key and scale name (e.g., G major, A pentatonic_minor).

2. Visualization: The script generates tablatures for the selected scale, displaying the fret positions and note names.

3. PDF Export: Users have the option to save the generated tablatures as a PDF file directly in the script's directory.

#### Requirements

- Python 3.x

#### Modules

The script uses the built-in `itertools` module, which is a standard library in Python and doesn't require separate installation.
Install the required library: pip install fpdf

#### Example

Suppose you want to explore the G major scale. Enter "G major" when prompted by the script. The tool will then generate tablatures for the G major scale on the guitar fretboard.

#### Additional Notes

To ensure accuracy in generating tablatures, I have defined scales along with their corresponding interval patterns for the notes. 
The interval function is repeatedly used within the create_scale function in order to determine the sequence of notes in the scale based on the specified intervals relative to the scale and to the root key provided as input by the user. When the code calls the create_scale function, the interval function is subsequently called and utilized to calculate which notes are at each interval.
The create_scale function uses the itertools module to efficiently iterate through the musical notes, starting from the specified root key. 
The use of this library allows efficient cycles and iterations, ensuring precise determination of note positions on the tablatures.
Functions like dropwhile and islice are used to skip notes until the specified root key is found and utilized to logically slice the iterator for populating scales and tablatures.

#### Contributions

Contributions to this project are welcome. If you have suggestions for additional features, improvements, or bug fixes, feel free to open an issue.

#### License

This project is licensed under the MIT License - see the `LICENCE.md` file for details.

#### Acknowledgments

- The script utilizes the fpdf library for PDF generation.
- Special thanks to Harjyot Singh [https://github.com/excerebrose] for providing valuable resources and to the CS50 community for the support.

#### Author

Nicolas Mecaj

#### Contact

For any inquiries or feedback, please contact **mecajnicolas@gmail.com**

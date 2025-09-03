#! python3
# mclip.py - A multi-clipboard program.

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?""",
        'cover': """Greetings,
I'm an Electrical Engineer with extensive experience in circuit design, power electronics and control systems. I'd love to build this power converter for you.

My experience as a Control Systems Engineer at Garudeus Aviation Inc. and as a Field Engineer at GE HealthCare has honed my ability to design and troubleshoot complex electrical systems. In the past I've created power converter circuits, control circuits, analog filters and amplifiers with power ratings ranging from a few hundred mW to 10kW. For your specific requirement of generating a 12VAC sine wave from a 12VDC supply and controlling the motor speed via a potentiometer, I propose the following approach:

    DC to AC Conversion: Design an inverter circuit to convert 12VDC to 12VAC.
    Speed Control Mechanism: Test multiple control mechanisms and implement the one that works best with a potentiometer.
    Efficiency Optimization: Ensure the circuit is optimized for low power consumption, given the low wattage of the motor.

Full Disclosure, I'm resuming circuit design here to satiate my need for creating beautiful, heavily optimized circuits [ The heaviliy optimized part is complimentary ;) ]. I'll be sure to deliver a stellar circuit for you. You can go to polarvector.github.io for a snapshot of projects that I can publish publicly. The inner webpages aren't working yet so you can check out my portfolio folder [ https://drive.google.com/drive/folders/1KCESdD-bG3Joe71PEqKfU18MRKA5C-UD?usp=drive_link ] for any files that you'd like to check out. 

To exceeding expectations. Cheers!
Polarj"""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]    # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

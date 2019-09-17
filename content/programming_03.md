Title: MPE to CV module
Date: 2019-09-17 20:44
Category: Programming

So, I bought a load of components from Digikey. Some are still on the way
(don't ask), but in general the hardware aspect of the prototype of this module
is coming together. Basically, I've copied [Little-Scale's USB MIDI-CV
interface](https://little-scale.blogspot.com/2019/01/12-gate-16-cv-usb-midi-interface-bom.html).
It's just got 20 CV outs instead of 16, and four trigger outs, instead of 12.
This is because I need four channels, each consisting of:

- Trigger
- Pitch
- Note on velocity
- Note off velocity
- Y-axis
- Pressure

I'll start with this, using the unbuffered MCP4822 digital-to-analog converters
in that design. I've read on [Muff
Wiggler](https://www.muffwiggler.com/forum/viewtopic.php?p=1528896) that this
won't really cut it when it comes to pitch CV accuracy, or if I want to connect
a CV to more than one destination. But, in my experience, a good way to start
is as simple as possible, and then improve later. No doubt it will have
challenges you didn't see at first. So, I'm keeping it all on a breadboard, and
I'll improve as I go along, probably including a CV design, for the pitch CVs
at least, that's more along the lines of the [Ornament and
Crime](https://ornament-and-cri.me/). I'll also need a clock input, and since
I'm thinking about an arpeggiator, I'll need a stepper selector knob that will
give me different arpeggiatior modes. There may be more: I'll develop it
according to which features I want, in order to generate the kinds of
percussive, polymetric, harmonic patterns I'm looking for.

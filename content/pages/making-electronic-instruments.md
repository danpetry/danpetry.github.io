Title: MPE to CV Eurorack module
Category: mpe-to-cv-eurorack-module

This is a Eurorack module which is designed to take an MPE keyboard, for
example the [Roli Seaboard
Block](https://roli.com/products/blocks/seaboard-block), as input, and outputs
pitch and CV.

Additionally, it'll have a Euclidean rhythm generator and arpeggiator. The idea
is that you can play chords, and it'll generate percussive melodic polymetre.
Also, the pitch bend and other control signals in the MPE input will allow you
to create organic variations.

It'll be prototyped in [VCV rack](https://vcvrack.com/), and the code re-used
in the hardware. The idea is to use VCV rack as a software simulation.
Eventually, the goal is to build a continuous integration system that will
allow third-party developers to develop firmware for it, including allowing
them to simulate in VCV rack beforehand, and automated testing on a server and
a test rig to verify it works. Also, over the air deployment to the unit,
managed by a web portal.  There could be a number of generic, reprogrammable
inputs and outputs, and some other generic control elements. So, it could be
programmed to do anything - audio generation, processing, control voltages, and
so on.  Something like what Expert Sleepers are doing, except an open source
community supported by a continuous integration and deployment system. 

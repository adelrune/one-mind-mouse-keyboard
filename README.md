# Hotswap Script for Multiple Keyboard and Mouses
This script switches the controls from up to 10 keyboard+mice combos in a circular fashion while playing a different sound everytime a switch occurs (every 0.5s by default)

This script was inspired by the super mario world one mind romhack : https://www.smwcentral.net/?p=section&a=details&id=19929

This git repositories copies files from the excellent https://github.com/cobrce/interception_py for ease of use

This unfortunately only works on windows, you need to install the intercept dll for it to work.

To use : python3 hotswap.py

after that lets say you have mouse1(m1), keyboard1(k1), mouse2(m2) and keyboard2(k2)

if you want to group the different devices by their numbers you need to

move or click any button on m1
press any key on k1

move or click any button on m2
press any key on k2

if everything worked fine, you'll hear soothing piano tones comming out of your speakers and each pair of device will only be able to interact with the computer 50% of the time. The script does not work with touchpads so they can be a convenient way to navigate around your computer once the script is launched

This should work for up to 10 m+k pairs but it was only tested with 2

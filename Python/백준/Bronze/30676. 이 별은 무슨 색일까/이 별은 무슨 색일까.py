import sys

wavelength = int(input())

if 620 <= wavelength <= 780:
    print("Red")
elif 590 <= wavelength < 620:
    print("Orange")
elif 570 <= wavelength < 590:
    print("Yellow")
elif 495 <= wavelength < 570:
    print("Green")
elif 450 <= wavelength < 495:
    print("Blue")
elif 425 <= wavelength < 450:
    print("Indigo")
elif 380 <= wavelength < 425:
    print("Violet")
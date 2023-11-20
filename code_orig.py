# Write your code here :-)
import board
from adafruit_neopxl8 import NeoPxl8
from adafruit_pixelmap import PixelMap
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.group import AnimationGroup
from adafruit_led_animation.sequence import AnimationSequence
from rainbowio import colorwheel

strand_length = 5
pixel_brightness = 0.8
num_strands = 3

num_pixels = num_strands * strand_length

pixels = NeoPxl8(
    board.NEOPIXEL0,
    num_pixels,
    num_strands=num_strands,
    auto_write=False,
    brightness=pixel_brightness,
)


def strand(n):
    return PixelMap(
        pixels,
        tuple(range(n * strand_length, (n + 1) * strand_length)),
        individual_pixels=True,
    )


pixel_strip_A = strand(0)
pixel_strip_B = strand(1)
pixel_strip_C = strand(2)

animations = AnimationSequence(
    AnimationGroup(
        Rainbow(pixel_strip_A, speed=0.01, period=7),
        Rainbow(pixel_strip_B, speed=0.01, period=7),
        Rainbow(pixel_strip_C, speed=0.01, period=7),
    ),
    advance_interval=9,
    auto_clear=True,
)

while True:
    animations.animate()

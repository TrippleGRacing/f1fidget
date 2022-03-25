def on_button_pressed_a():
    global Gear
    if True:
        Gear += 1
        basic.show_number(Math.constrain(Gear, 0, 8))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Gear
    if True:
        basic.show_string("N")
        Gear = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Gear
    if True:
        Gear += -1
        basic.show_number(Math.constrain(Gear, 1, 8))
input.on_button_pressed(Button.B, on_button_pressed_b)

Gear = 0
basic.show_string("Formula 1 Fidget")
basic.pause(2000)
basic.show_leds("""
    # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
""")

def on_forever():
    pass
basic.forever(on_forever)

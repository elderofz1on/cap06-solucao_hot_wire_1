def on_button_pressed_a():
    global falhas
    falhas = 0
    basic.show_number(falhas)
    basic.show_leds("""
        # # # . #
                # . # . #
                # . # # #
                # . . . .
                # . . . .
    """)
    basic.pause(200)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("Falhas: ")
    basic.show_number(falhas)
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    global falhas
    falhas += 1
    basic.show_icon(IconNames.SKULL)
    basic.pause(500)
    basic.clear_screen()
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

falhas = 0
falhas = 0
basic.show_leds("""
    # # # . #
        # . # . #
        # . # # #
        # . . . .
        # . . . .
""")
basic.pause(200)
basic.clear_screen()
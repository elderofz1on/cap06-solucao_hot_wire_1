input.onButtonPressed(Button.A, function () {
    falhas = 0
    basic.showNumber(falhas)
    basic.showLeds(`
        # # # . #
        # . # . #
        # . # # #
        # . . . .
        # . . . .
        `)
    basic.pause(200)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    basic.showString("Falhas: ")
    basic.showNumber(falhas)
    basic.pause(500)
    basic.clearScreen()
})
input.onPinPressed(TouchPin.P1, function () {
    falhas += 1
    basic.showIcon(IconNames.Skull)
    basic.pause(500)
    basic.clearScreen()
})
let falhas = 0
falhas = 0
basic.showLeds(`
    # # # . #
    # . # . #
    # . # # #
    # . . . .
    # . . . .
    `)
basic.pause(200)
basic.clearScreen()

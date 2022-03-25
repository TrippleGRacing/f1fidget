input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (true) {
        Gear += 1
        basic.showNumber(Math.constrain(Gear, 0, 8))
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    if (true) {
        basic.showString("N")
        Gear = 0
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (true) {
        Gear += -1
        basic.showNumber(Math.constrain(Gear, 1, 8))
    }
    
})
let Gear = 0
basic.showString("Formula 1 Fidget")
basic.pause(2000)
basic.showLeds(`
    # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
`)
basic.showLeds(`
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
`)
basic.showLeds(`
    # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
`)
basic.showLeds(`
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
`)
basic.showLeds(`
    # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
`)
basic.forever(function on_forever() {
    
})

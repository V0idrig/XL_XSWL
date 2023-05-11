def right():
    pass
def left():
    pass
def stop():
    sensors.dd_mmotor(AnalogPin.P13, 0, AnalogPin.P14, 0)
    sensors.dd_mmotor(AnalogPin.P15, 0, AnalogPin.P16, 0)
def go():
    sensors.dd_mmotor(AnalogPin.P13, 0, AnalogPin.P14, 0)
    sensors.dd_mmotor(AnalogPin.P15, 0, AnalogPin.P16, 0)
stop()

def on_forever():
    pass
basic.forever(on_forever)

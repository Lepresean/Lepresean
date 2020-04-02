from gpiozero import Button
print("imported Button")

btn = Button(4)

def hello():
    print("hello")

btn.when_pressed = hello

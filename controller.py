import time
import mouse



def repeatClick(x,y,numberOfClick,period,type='single', button='left'):
    def click(type, button):
        if type == 'double':
            mouse.click(button)
            mouse.click(button)
        elif type == 'single':
            mouse.click(button)
    mouse.move(x, y, duration=0.2)
    #if x,y is not changing
    time.sleep(0.2)
    for i in range(numberOfClick):
        click(type, button)

        time.sleep(period)


'''
#Get cursor position

a=mouse.is_pressed('left')
print(a)
while not a:
    a = mouse.is_pressed('left')
    if a:
        break
    mouse.on_right_click(lambda: print("Right Button clicked."))
'''
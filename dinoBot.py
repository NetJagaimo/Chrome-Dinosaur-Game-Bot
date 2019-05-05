from PIL import ImageGrab, Image
import pyautogui
import time

def startGame(cordinates):
    print("Start! press ctrl + c to terminate the program")
    pyautogui.click(cordinates['replayBtn']) 
    pyautogui.keyDown('down')

def pressSpace(airtime):
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
    time.sleep(airtime)
    pyautogui.keyDown('down')

def imageGrab(box):
    image = ImageGrab.grab(box)
    grayImage = image.convert('L')
    return len(grayImage.getcolors())

def main(cordinates):
    offset = 0
    t = time.time()
    airtime = 0.135
    while True:
        if time.time() - t >= 5:
            if offset >= 12:
                if offset < 140:
                    offset += 8
                else:
                    offset = 140
                if airtime-0.0084 > 0:
                    airtime -= 0.0084
                else:
                    airtime = 0
                t = time.time()
            else:
                offset += 2
                t = time.time()

        obstacle1_box = (cordinates['dino'][0] + 80, 155 + cordinates['topLeft'][1], cordinates['dino'][0] + 145 + offset, 156 + cordinates['topLeft'][1])
        ob1 = imageGrab(obstacle1_box)
        if ob1 > 1:
            pressSpace(airtime)

if __name__ == "__main__":
    print("Please adjust the runner-canvas width to 600")
    inStr = input("Please enter the top left cordinate(Separate by blank): ")
    inStr = inStr.split()
    topLeft = (int(inStr[0]), int(inStr[1]))
    cordinates = {
        'replayBtn': (302 + topLeft[0], 116 + topLeft[1]),
        'dino': (85 + topLeft[0], 121 + topLeft[1]),
        'topLeft': topLeft
    }

    input("Press enter to start...")
    startGame(cordinates)
    main(cordinates) 
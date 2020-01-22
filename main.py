import keyboard

currentIndex = 1
lightParty = True


def main():
    global currentIndex
    global lightParty

    keyboard.add_hotkey('page up', cycleUp, suppress=True)
    keyboard.add_hotkey('page down', cycleDown, suppress=True)
    keyboard.add_hotkey('home', toggleParty, suppress=True)

    keyboard.wait('')


def cycleUp():
    global currentIndex
    global lightParty

    currentIndex -= 1

    if lightParty is True:
        if currentIndex < 1:
            currentIndex = 4
        elif currentIndex > 4:
            currentIndex = 4
    elif lightParty is False and currentIndex < 1:
        currentIndex = 8

    key = 'F' + str(currentIndex)
    print(key)

    keyboard.press_and_release(key)


def cycleDown():
    global currentIndex
    global lightParty

    currentIndex += 1
    if lightParty is True:
        if currentIndex > 4:
            currentIndex = 1
    if lightParty is False:
        if currentIndex < 1:
            currentIndex = 8
        elif currentIndex > 8:
            currentIndex = 1

    key = 'F' + str(currentIndex)
    print(key)

    keyboard.press_and_release(key)


def toggleParty():
    global lightParty
    lightParty = not lightParty
    print("Light Party: " + str(lightParty))


main()

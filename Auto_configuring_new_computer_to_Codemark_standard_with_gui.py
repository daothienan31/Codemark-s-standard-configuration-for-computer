# File name: Auto_configuring_new_computer_to_Codemark_standard_with_gui
# Purpose: Automatically setup configuration to Codemark Standard. (Eliminating repeating manual actions)
# Author: An Thien Dao (Andy)
# Co-Author:
# Beginning date: July 4th, 2022
# Modified date: July 5th, 2022

import pyautogui, sys
import cv2 as cv
import numpy as np
import PIL
from PIL import Image
from PIL import ImageGrab
import pytesseract
import os.path
import time
import shutil

saved_screen_size = (1920, 1080)  # Size of saved pictures to use for button detection/location
current_device_screen_size = pyautogui.size()  # Record current screen size for adjustment to saved_screen_size


# Function name: resize_saved_picture_to_current_device_size
# Purpose: For pyautogui.locateCenterOnScreen() to work, image required to be same size. So this function calculate
# screen ratio and adjust the saved image
# Author: An Thien Dao (Andy)
# Modifier: An Thien Dao (Andy)
# Beginning date: July 5th, 2022
# Modified date: July 5th, 2022
# REQUIRE TO BE TESTED
# Source code: https://www.reddit.com/r/learnpython/comments/htt6yy/pyautogui_and_image_detection_on_different/
def resize_saved_picture_to_current_device_size(image):
    image = Image.open(image)
    screens_ratio = (current_device_screen_size[0] / saved_screen_size[0], current_device_screen_size[1] /
                     saved_screen_size[1])  # Calculate screen
    resize_saved_picture = image.resize(image.size[0] * screens_ratio[0], image.size[1] * screens_ratio[1])  # Produce
    # new image ratio
    if os.path.exists('resized_button.png'):  # remove the existing resized_button.png
        os.remove('resized_button.png')
    resize_saved_picture.save('resized_button.png')  # save the new picture


# Function name: resize_saved_picture_to_current_device_size
# Purpose: Relocating mouse's current position to the target button to click. If the screen has different ratio. Call
# resize_saved_picture_to_current_device_size function
# Author: An Thien Dao (Andy)
# Modifier: An Thien Dao (Andy)
# Beginning date: July 4th, 2022
# Modified date: July 5th, 2022
def click_button(clickable_icon):
    if saved_screen_size != current_device_screen_size:  # Need to be tested as
        # resize_saved_picture_to_current_device_size() is needed to be tested
        resize_saved_picture_to_current_device_size(clickable_icon)
        button = pyautogui.locateCenterOnScreen('resized_button.png')
    else:
        button = pyautogui.locateCenterOnScreen(clickable_icon)

    if button is not None:
        pyautogui.moveTo(button)
        pyautogui.click()


# Function name: locate_icon
# Purpose: Relocating mouse's current position to the target icon. If the screen has different ratio. Call
# resize_saved_picture_to_current_device_size function
# Author: An Thien Dao (Andy)
# Modifier: An Thien Dao (Andy)
# Beginning date: July 4th, 2022
# Modified date: July 5th, 2022
def relocate_to_icon(icon):
    if saved_screen_size != current_device_screen_size:  # Need to be tested as
        # resize_saved_picture_to_current_device_size() is needed to be tested
        resize_saved_picture_to_current_device_size(icon)
        icon_location = pyautogui.locateCenterOnScreen('resized_button.png')
    else:
        icon_location = pyautogui.locateCenterOnScreen(icon)
    if icon_location is not None:
        pyautogui.moveTo(icon_location)


# Function name: keep_checking_mouse_position
# Purpose: Tool to check the mouse's location on screen
# Author: An Thien Dao (Andy)
# Modifier: An Thien Dao (Andy)
# Beginning date: July 6th, 2022
# Modified date: July 6th, 2022
def keep_checking_mouse_position():
    while True:
        print(pyautogui.position())
        time.sleep(1)


# Function name: turn_off_news_and_interest_in_task_bar
# Purpose: Turn off news and interest in task bar
# Author: An Thien Dao (Andy)
# Modifier: An Thien Dao (Andy)
# Beginning date: July 6th, 2022
# Modified date: July 6th, 2022
def turn_off_news_and_interest_in_task_bar():
    relocate_to_icon('TaskbarShowHiddenIcon.png')
    pyautogui.move(-50, 0)
    pyautogui.rightClick()
    pyautogui.sleep(1)
    relocate_to_icon('Newsandinterests.png')
    pyautogui.sleep(1)
    click_button('NewsandinterestsTurnOff.png')


# Function name: modify_view_in_folder
# Purpose: Modify 'View' in folder
# Author: An Thien Dao (Andy)
# Modifier: An Thien Dao (Andy)
# Beginning date: July 6th, 2022
# Modified date: July 6th, 2022
def modify_view_in_folder():
    with pyautogui.hold('win'):
        pyautogui.press('e')
    time.sleep(1)
    click_button('ViewinFolder.png')
    time.sleep(1)
    click_button('FileNameExtensionsInFolder.png')
    time.sleep(1)
    click_button('ViewinFolder.png')
    click_button('OptionsInViewInFolder.png')
    time.sleep(1)
    click_button('OpenFileExplorerTo.png')
    time.sleep(1)
    click_button('OpenFileExplorerToThisPC.png')
    for x in range(2):
        click_button('CheckBoxInFolderOptions.png')
    click_button('ClearInFolderOptions.png')
    click_button('OKInFolderOptions.png')


# Function name: copy_codemark_image_into_public_folder
# Purpose: Copy Codemark's background, profile & lockscreen image into
# Author: An Thien Dao (Andy)
# Modifier: An Thien Dao (Andy)
# Beginning date: July 7th, 2022
# Modified date: July 7th, 2022
def copy_codemark_image_into_public_folder():
    with pyautogui.hold('win'):
        pyautogui.press('e')
    time.sleep(1)
    click_button('SearchBarInMyComputer.png')
    pyautogui.write('CODEMARK')
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(1)
    click_button('FileNamecodemark_SecurityProfilePicture.png')
    pyautogui.keyDown('shiftleft')
    pyautogui.keyDown('shiftright')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.keyUp('shiftleft')
    pyautogui.keyUp('shiftright')
    with pyautogui.hold('ctrl'):
        pyautogui.press('c')
    click_button('DriverIcon.png')
    pyautogui.write(r"C:\Users\Public\Pictures")
    time.sleep(1)
    pyautogui.press('enter')
    with pyautogui.hold('ctrl'):
        pyautogui.press('v')


# Function name: complete_email
# Purpose: send an email after completion
# Author: An Thien Dao (Andy)
# Modifier: An Thien Dao (Andy)
# Beginning date: July 11th, 2022
# Modified date: July 11th, 2022
def complete_email():
    relocate_to_icon('MicrosoftEdgeIcon.png')
    record_icon_location = pyautogui.position()
    pyautogui.rightClick()
    time.sleep(1)
    click_button('TaskAfterRightClickMicrosoftEdge.png')
    click_button('MicrosoftEdgeNewInPrivateWindow.png')
    time.sleep(1)
    pyautogui.moveTo(record_icon_location)
    pyautogui.doubleClick()
    pyautogui.write('outlook.live.com')
    pyautogui.press('enter')
    time.sleep(3)
    click_button('OutlookBrowserSignIn.png')
    time.sleep(3)
    pyautogui.write(email)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.write('password')
    pyautogui.press(password)
    time.sleep(3)
    click_button('No_StaySignedIn.png')
    time.sleep(10)
    click_button('NewMessage_OutlookEmail.png')
    time.sleep(10)
    pyautogui.write('adao@codemark.ca')
    click_button('AddASubjectField.png')
    pyautogui.write('DONE!')
    click_button('SendButton.png')


# Function name: power_and_sleep_setting()
# Purpose: Setting power and sleep
# Author: An Thien Dao (Andy)
# Modifier: An Thien Dao (Andy)
# Beginning date: July 11th, 2022
# Modified date: July 11th, 2022
def power_and_sleep_setting():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('Power & sleep setting')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    relocate_to_icon('WhenPluggedInTurnOffAfter.png')
    pyautogui.move(0, 25)
    pyautogui.click()
    time.sleep(1)
    click_button('30Minutes.png')
    time.sleep(1)
    relocate_to_icon('WhenPluggedInPCGoesToSleepAfter.png')
    pyautogui.move(0, 25)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('n')
    pyautogui.press('enter')


# Function name: notification_setting()
# Purpose: Only 8 features in the notification setting and in order
# Author: An Thien Dao (Andy)
# Modifier: An Thien Dao (Andy)
# Beginning date: July 12th, 2022
# Modified date: July 14th, 2022
def notification_setting():
    add_in_options = ['AllSettings_NotificationSetting.png', 'Network_NotificationSetting.png',
                      'ScreenSnip_NotificationSetting.png', 'Location_NotificationSetting.png',
                      'Connect_NotificationSetting.png', 'Project_NotificationSetting.png',
                      'VPN_NotificationSetting.png', 'FocusAssist_NotificationSetting.png']
    options = 0
    click_button('NotificationButton.png')
    pyautogui.move(0, -250)
    time.sleep(1)
    pyautogui.rightClick()
    time.sleep(1)
    relocate_to_icon('Edit_NotificationSetting.png')
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    for x in range(3):
        relocate_to_icon('Unpin_NotificationSetting.png')
        time.sleep(1)
        for y in range(4):
            click_button('Unpin_NotificationSetting.png')
            time.sleep(1)
    while options < 8:
        click_button('Add_NotificationSetting.png')
        time.sleep(1)
        relocate_to_icon(add_in_options[options])
        pyautogui.doubleClick()
        time.sleep(1)
        options += 1
    click_button('Done_NotificationSetting.png')


# Function name: color()
# Purpose: print out the RGB value of the pixel that the mouse currently on
# Author: https://stackoverflow.com/questions/64722136/how-to-use-pyautogui-to-detect-rgb-values
# Modifier: https://stackoverflow.com/questions/64722136/how-to-use-pyautogui-to-detect-rgb-values
# Beginning date: July 15th, 2022
# Modified date: July 15th, 2022
def color():
    while 1:
        x, y = pyautogui.position()
        r, g, b = pyautogui.pixel(x, y)
        print(r, g, b)
        time.sleep(1)


# Function name: start_menu_adjustment()
# Purpose: To check and adjust the display in start menu
# Author: An Thien Dao (Andy)
# Modifier: An Thien Dao (Andy)
# Beginning date: July 15th 2022
# Modified date: July 15th 2022
def start_menu_adjustment():
    stop_looping = 0
    pyautogui.press('win')
    pyautogui.write('notepad')
    pyautogui.press('enter')
    pyautogui.press('win')
    time.sleep(1)
    relocate_to_icon('AllApps_Start.png')
    pyautogui.move(50, 0)
    # TODO: Test
    while stop_looping == 0:
        x, y = pyautogui.position()
        r, g, b = pyautogui.pixel(x, y)
        if r == g == b < 75:
            stop_looping = 1
        else:
            pyautogui.rightClick()
            time.sleep(1)
            click_button('UnpinFromStart_Start.png')
            time.sleep(1)
    # TODO: Pin correct attributes from all apps in correct order


# Function name: taskbar_setting_adjustment()
# Purpose: Change taskbar setting to requirement
# Author: An Thien Dao (Andy)
# Modifier: An Thien Dao (Andy)
# Beginning date: July 18th, 2022
# Modified date: July 18th, 2022
def taskbar_setting_adjustment():
    pyautogui.press('win')
    pyautogui.write('notepad')
    pyautogui.press('enter')
    relocate_to_icon('TaskbarShowHiddenIcon.png')
    pyautogui.move(-50, 0)
    pyautogui.rightClick()
    click_button('TaskbarSetting_Taskbar.png')
    click_button('AlwaysHideLabels_Taskbar.png')
    time.sleep(1)
    click_button('WhenTaskBarIsFull.png')
    start_taskbar_setting()

    # TODO: Start


# Function name: start_taskbar_setting()
# Purpose: Only keep 'Show recently opened items in Jump Lits  on Start or the task bar and in File Explorer Quick
# Access' on
# Author: An Thien Dao (Andy)
# Modifier: An Thien Dao (Andy)
# Beginning date: July 18th, 2022
# Modified date: July 18th, 2022
def start_taskbar_setting():
    # TODO: Test
    stop_looping = 0
    while stop_looping == 0:
        current_location = pyautogui.position()
        relocate_to_icon('Off_start.png')
        if current_location != pyautogui.position():
            pyautogui.click()
        else:
            stop_looping = 1
    for x in range(6):
        click_button('On_start.png')


def main():
    print('Hello')
    # notification_setting()
    # copy_codemark_image_into_public_folder()
    # modify_view_in_folder()
    # turn_off_news_and_interest_in_task_bar()
    # keep_checking_mouse_position()
    # click_button('WindowsIcon.png')
    # power_and_sleep_setting()
    # notification_setting()
    # start_menu_adjustment()
    taskbar_setting_adjustment()
    # complete_email()
    # color()


main()

# https://stackoverflow.com/questions/49101270/move-to-searched-text-on-active-screen-with-pyautogui

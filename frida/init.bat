rem adb forward tcp:27043 tcp:27043
rem adb forward tcp:27042 tcp:27042
adb -s emulator-5554 forward tcp:27043 tcp:27043
adb -s emulator-5554 forward tcp:27042 tcp:27042
pause
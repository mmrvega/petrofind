from pywinauto import Application
from pywinauto.findwindows import ElementAmbiguousError
import pyperclip
from time import sleep
# Path to your calculator application executable
calc_exe_path = "./Petro Calculator.exe"

# Launch the calculator application
app = Application(backend="uia").start(calc_exe_path)
app = Application(backend="uia").connect(path=calc_exe_path, top_level_only=False)
calc_window = app.window(title_re="Petro Calculator")
# Access the window (assuming it's the first window)
window = app.windows()[0]
text_id = 156
window.click_input(coords=(380, 224))

window.click_input(coords=(106, 362))
#for control in window.descendants():
#    print(control.window_text(), control.class_name(),  control._control_types, control.control_id())
#    print("++++++++++++++++\n")
#for i in range(1, 189):  # Replace "ButtonName" with the actual name of the button
text_control = None
text_id = 150
for control in window.descendants():
    if control.control_id() == text_id:
        text_control = control
if text_control is not None:
    print(text_id)
    text_control.click_input()
sleep(1)
    # text_id += 1
#000000000000000000000000 725,395
# Close the calculator application
calc_window.close()

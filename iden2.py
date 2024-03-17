from pywinauto import Application
# Path to your calculator application executable
calc_exe_path = "./Petro Calculator.exe"
# Connect to the calculator application
app = Application(backend="uia").start(calc_exe_path)
app = Application(backend="uia").connect(path=calc_exe_path, top_level_only=False)
calc_window = app.window(title_re="Petro Calculator")
# Access the window (assuming it's the first window)
window = app.windows()[0]

for control in window.descendants():
    print(control.window_text(), control.class_name(),  control._control_types, control.control_id())
    print("++++++++++++++++\n")
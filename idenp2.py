from pywinauto import Application
from pywinauto.findwindows import ElementNotFoundError
from time import sleep
import pyperclip
from os import system
# Path to your calculator application executable
calc_exe_path = "./Petro Calculator.exe"
# Connect to the calculator application
app = Application(backend="uia").start(calc_exe_path)
app = Application(backend="uia").connect(path=calc_exe_path, top_level_only=False)
calc_window = app.window(title_re="Petro Calculator")
# Access the window (assuming it's the first window)
window = app.windows()[0]

denr_id = 147  # Replace "ButtonName" with the actual name of the button
denr_cont = None
calb_id = 148
calb_cont = None
temp_id = 149
temp_cont = None
obs_id = 150
obs_cont = None
# search screen data for ides
window.click_input(coords=(380, 224))
window.click_input(coords=(106, 362))
for control in window.descendants():
    if control.control_id() == denr_id:
        denr_cont = control
    if control.control_id() == calb_id:
        calb_cont = control
    if control.control_id() == temp_id:
        temp_cont = control
    if control.control_id() == obs_id:
        obs_cont = control
# start process
if denr_cont and calb_cont is not None:
    density = 1074
    tempr = -18.00
    with open("a53.txt", "a") as file1:
        while 1074 <= density <= 1074.75 : #stop 616.5 / stop 718
            if density <= 778:
                tempr_high = 95
            elif density <= 824:
                tempr_high = 125
            elif density <= 1035:
                tempr_high = 150
            elif density <= 1075:
                tempr_high = 17
            obs_cont.set_text(density)
            while -18 <= tempr <= tempr_high: #95
            
        #   den_cont.set_text(density)
                try:
                    temp_cont.set_text(tempr)
                    calb_cont.click()
                    error_code = 0
                    temp_cont.set_text(tempr)
                except:
                    print("error exception")
                    window.click_input(coords=(810, 430))
                    error_code = 1
                    tempr += 0.25
    #calculation button 
    #writeing vlaue to file
               # vcfr_cont.click_input(double=True)
                #vcfr_cont.type_keys("^c")
                #vcf = pyperclip.paste()
                denr =denr_cont.get_value()
                print(denr)
                if not denr or error_code == 1:
                    print("error of vcf speed",denr)
                    #sleep(0.2)
                    
                else:
                    vcfwrite = f"{tempr}, {density}, {denr}\n"
                #for contro in window.descendants():
                #    vwrite = f"{vcfr_cont.get_value()}\n"
                #file1.write()
                    file1.write(vcfwrite)
                    tempr += 0.25
                    
            system("cls")
            density += 0.5
            tempr = -18.0
    sleep(5)
    file1.close()
    print("end :>")
else:
    print(f"Button with name not found.")
    
# Print control identifiers of the window (including all controls within it)
#for control in window.children():
#    print(control.window_text(), control.class_name(),  control._control_types, control.control_id())
#    print("++++++++++++++++\n")
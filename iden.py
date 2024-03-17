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

text_id = 7  # Replace "ButtonName" with the actual name of the button
text_control = None
den_id = 19
den_cont = None
Adoc_id = 18
adoc_cont = None
temp_id = 13
fivedec_id = 9
fivedec_cont = None
temp_cont = None
cal_id = 12
cal_cont = None
vcfr_id = 11
vcfr_cont = None
# search screen data for ides
for control in window.descendants():
    if control.control_id() == text_id:
        text_control = control
    if control.control_id() == den_id:
        den_cont = control
    if control.control_id() == Adoc_id:
        adoc_cont = control
    if control.control_id() == temp_id:
        temp_cont = control
    if control.control_id() == cal_id:
        cal_cont = control
    if control.control_id() == vcfr_id:
        vcfr_cont = control
    if control.control_id() == fivedec_id:
        fivedec_cont = control
# start process
if text_control and den_cont is not None:
    # buttons start
    adoc_cont.click_input() 
    fivedec_cont.click_input()
    #texts start 
    #text_to_input = ""
    #text_control.set_text(text_to_input)
    density = 718
    tempr = -18.00
    counter = int(0)
    with open("a54.txt", "a") as file1:
        while 718 <= density <= 1075 : #stop 616.5 / stop 718
            den_cont.set_text(density)
            while -18 <= tempr <= 95: #95
            
        #   den_cont.set_text(density)
                temp_cont.set_text(tempr)
    #calculation button
                cal_cont.click() 
    #writeing vlaue to file
               # vcfr_cont.click_input(double=True)
                #vcfr_cont.type_keys("^c")
                #vcf = pyperclip.paste()
                vcf =vcfr_cont.get_value()
                if not vcf:
                    print("error of vcf speed",vcf)
                    sleep(0.2)
                    
                else:
                    vcfwrite = f"{tempr}, {density}, {vcf}\n"
                #for contro in window.descendants():
                #    vwrite = f"{vcfr_cont.get_value()}\n"
                #file1.write()
                    file1.write(vcfwrite)
                    itr = (counter/322728)*100
                    print ("remaning:", itr, "%")
                    tempr += 0.25
                    counter += 1
            
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
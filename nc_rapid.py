import re
import os
import tkinter as tk
from tkinter import filedialog

# Script varibles
FD_AllFiles                 = 0 #Set this depending if you want the script to run on all files in current directory or show a file dialog
Threshold_Height            = 4 #Set the threshold for when a rapid move should happen
New_Feedrate                = 3001 #Set rapid move feedrate

# Setup varibles
Above_Height_Threshold      = 1 #Sets initial condition (do not change)
Above_Height_Threshold_prev = 1 #Sets initial condition (do not change) 
NewLine_Flag                = 1 #Sets initial condition (do not change)
LineNum                     = 1 #Sets initial condition (do not change)
Current_Height              = 0 #Sets initial condition (do not change)

if FD_AllFiles == 0:
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilenames()
else:
    file_path = os.listdir()



for SelectedFiles in file_path:
    print(SelectedFiles)
    new_file_path = SelectedFiles.split(".")
    new_file_path = new_file_path[0] + "_HighFeed.nc"

    f_output = open(new_file_path, "w")

    with open(SelectedFiles) as f:
        for line in f:
    # Check to see if the line is a comment or empty and discard it 
            if ";" in line or line in ['\n', '\r\n']:
                continue
    #
            #print("Input Line = ",line.replace("\n", " "))
            Above_Height_Threshold_prev = Above_Height_Threshold
            data_line = line.split()
            Output_Line =""
            NewLine_Flag = 1
    # This section checks the current height of the machine and sets a flag for when its greater then the threshold                
            if "z" in line or "Z" in line:
                data_line = line.split()
                for i in data_line:
                    if "z" in i or "Z" in i:
                        #Current_Height = re.findall(r"[-+]?\d*\.\d+|\d+", i)
                        Current_Height = i.replace("z","")
                        Current_Height = i.replace("Z","")
                        #print(i)
                        Current_Height = float(''.join(Current_Height))
                        if Current_Height > Threshold_Height:
                            Above_Height_Threshold = 1
                        else:
                            Above_Height_Threshold = 0
                        #print(LineNum, "  Current Height ", Current_Height ," - Above Height Threshold ", Above_Height_Threshold," - Old Height Threshold ", Above_Height_Threshold_prev)
    # Amend feedrate if appicable to the new value if the threshold is set. 
            for i in data_line:
                if "f" in i or "F" in i and Above_Height_Threshold >= 1 and Above_Height_Threshold_prev >= 1:
                    if NewLine_Flag >= 1:
                        Output_Line = Output_Line + "F" + str(New_Feedrate)
                        NewLine_Flag = 0
                    else:
                        Output_Line = Output_Line + " F" + str(New_Feedrate)
                        NewLine_Flag = 0
                else:
                    if NewLine_Flag >= 1:
                        Output_Line = Output_Line + i
                        NewLine_Flag = 0
                    else:
                        Output_Line = Output_Line + " " + i 
                        NewLine_Flag = 0

            #print("PrintOutput line ",Output_Line, "\n")
            #print(LineNum, "  Current Height ", Current_Height ," - Above Height Threshold ", Above_Height_Threshold," - Old Height Threshold ", Above_Height_Threshold_prev)
            f_output.writelines(Output_Line +"\n")
            LineNum += 1
    f_output.close()


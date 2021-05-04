

<img align="right" width=175 src="Media/R_Logo.png" />

# Root CNC

Root_Rapdise is a tool that aims to add rapid movements back into the Gcode Fusion360 CAM that is limited to persional uses.

The tool will add a user defined feederate to movements above a given threshold.

This tool is a work around to the current notification for rapid movements in Fusion360

    ;When using Fusion 360 for Personal Use, the feedrate of
    ;rapid moves is reduced to match the feedrate of cutting
    ;moves, which can increase machining time. Unrestricted rapid
    ;moves are available with a Fusion 360 Subscription.

## License

This project is licensed under the Creative Commons 4.0 license with 
Attribution-NonCommerial-ShareAlike see `LICENSE.txt` for details


## How To install.
### Requirements
* Ensure Python is installed and added to path

### install 
* Download the files  
* Copy the `nc_rapid.py` to `C:\Windows\`
* Lets test it! Goto the directory where you have your generated Gcode (Please note it'll 'Rapidise' all files in current directory and below - ensure only Gcode is in the current directory with no dub directories) 
* Hold `SHIFT KEY` and click `RIGHT CLICK`
* From dropdown select `Open command window here` or `Open PowerShell windows here`
* Write `nc_rapid.py` and press `ENTER KEY`
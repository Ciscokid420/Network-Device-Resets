# $language = "python"
# $interface = "1.0"

# ResetSwitch.py

# Works with Cisco. Tested on:
#   2960X
#   3560CX

# Decription:
# 	This script when ran with SecureCRT will reset a switch from ROMMON mode.
#   The script will wait for outputs from the switch, so it can be ran
#	continuously while you change from switch to switch.

# Starts loop
while True :

    # Script will look for this to stop flash from initializing
    initPrompt = "flash_init"

    # Script will look for this to issue commands
    swPrompt = "switch:"

    # Script will look for this to enter "y" when prompted
    ynPrompt = " (y/n)?"
    
    #Script will look for conig .text deleted and boot
    #bootswitch = "File'flash:config.text' deleted"
    # Using GetScriptTab() will make this script 'tab safe'
    objTab = crt.GetScriptTab()
    objTab.Screen.Synchronous = True
    objTab.Screen.IgnoreEscape = True

    # Wait for initPrompt then send break command to enter ROMMON
    objTab.Screen.WaitForString(initPrompt)
    objTab.Screen.SendSpecial("TN_BREAK")
    objTab.Screen.SendSpecial("TN_BREAK") # sending this twice to make sure it takes

    # Wait for swPrompt then initalize flash
    objTab.Screen.WaitForString(swPrompt)
    objTab.Screen.Send("flash_init" + "\n" + "\n") #sending \n twice advances the screen

    # Wait for swPrompt then send enter command
    objTab.Screen.WaitForString(swPrompt)
    objTab.Screen.Send("del flash:vlan.dat" + "\n")

    # Wait for ynPrompt then send enter command
    objTab.Screen.WaitForString(ynPrompt)
    objTab.Screen.Send("y" + "\n")

    # Wait for swPrompt then send enter command
    objTab.Screen.WaitForString(swPrompt)
    objTab.Screen.Send("del " + "flash:" + "config.text" + "\n")

    # Wait for ynPrompt then send enter command
    objTab.Screen.WaitForString(ynPrompt)
    objTab.Screen.Send("y" + "\n")

    objTab.Screen.WaitForString(swPrompt)
    objTab.Screen.SendSpecial("TN_BREAK")
    objTab.Screen.Send("boot" + "\n")

while True :

    # Script will look for this to stop flash from initializing
    initPrompt = "Type control-C to prevent autobooting."

    # Script will look for this to issue commands
    swPrompt = "rommon"

    # Script will look for this to enter "y" when prompted
    ynPrompt = "y/n"

    loginPrompt = "Press RETURN to get started!"
    
    #Script will look for conig .text deleted and boot
    #bootswitch = "File'flash:config.text' deleted"
    # Using GetScriptTab() will make this script 'tab safe'
    objTab = crt.GetScriptTab()
    objTab.Screen.Synchronous = True
    objTab.Screen.IgnoreEscape = True

    # Wait for initPrompt then send break command to enter ROMMON
    objTab.Screen.WaitForString(initPrompt)
    crt.Screen.Send(chr(3))
    crt.Screen.Send(chr(3)) # sending this twice to make sure it takes

    # Wait for swPrompt then initalize flash
    objTab.Screen.WaitForString(swPrompt)
    objTab.Screen.Send("confreg" + "\n") #sending \n twice advances the screen

    # Wait for swPrompt then send enter command
    objTab.Screen.WaitForString(ynPrompt)
    objTab.Screen.Send("y" + "\n")

    objTab.Screen.WaitForString(ynPrompt)
    objTab.Screen.Send("n" + "\n")
    
    objTab.Screen.WaitForString(ynPrompt)
    objTab.Screen.Send("n" + "\n")

    objTab.Screen.WaitForString(ynPrompt)
    objTab.Screen.Send("n" + "\n")

    objTab.Screen.WaitForString(ynPrompt)
    objTab.Screen.Send("n" + "\n")

    objTab.Screen.WaitForString(ynPrompt)
    objTab.Screen.Send("y" + "\n")

    objTab.Screen.WaitForString(ynPrompt)
    objTab.Screen.Send("y" + "\n")

    objTab.Screen.WaitForString(ynPrompt)
    objTab.Screen.Send("n" + "\n")

    objTab.Screen.WaitForString(ynPrompt)
    objTab.Screen.Send("n" + "\n")
    
    
    objTab.Screen.WaitForString(ynPrompt)
    objTab.Screen.Send("y" + "\n")

    objTab.Screen.WaitForString(swPrompt)
    objTab.Screen.Send("boot" + "\n")

    objTab.Screen.WaitForString(loginPrompt)
    crt.Sleep(300)
    objTab.Screen.Send("\r")
    objTab.Screen.Send("enable" + "\n")
    objTab.Screen.Send("erase  startup-config" + "\n" +"\n")
    objTab.Screen.Send("write erase" + "\n")
    objTab.Screen.Send("\r" + "exit" + "\n" + "exit" + "\n")

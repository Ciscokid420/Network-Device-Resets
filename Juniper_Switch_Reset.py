# $language = "python"
# $interface = "1.0"



admPW = 0
#Starts the infinite Loop for the script
while True:

#Sets the string variables for the first part of the script
    krnlPrompt = "/kernel"
    ldPrompt = "loader>"
    binPrompt = "/bin/sh"
    error = "continue, shell, abort, retry, or reboot ?"
    rtPrompt = "root>"
    conf = "#"
    pwPrompt = " password:"
    rbPrompt = "Reboot the system?"
    roottPrompt = "root@"
    prompts = ["root#","root>","root@"]
#loads in requirements for SecureCRT and makes the script "tab safe" whatever that means
    objTab = crt.GetScriptTab()
    objTab.Screen.Synchronous = True
    objTab.Screen.IgnoreEscape = True
#waits for the krnl prompt and sends 2 "spacebar" characters to stop it from booting into normal mode
    objTab.Screen.WaitForString(krnlPrompt)
    objTab.Screen.Send(" ")
    objTab.Screen.Send(" ")
#Looks for the loader prompt and sends the boot into safemode command
    objTab.Screen.WaitForString(ldPrompt)
    objTab.Screen.Send("boot -s" + "\n")
#Looks for the /bin prompt and sends the recovery command
    objTab.Screen.WaitForString(binPrompt)
    objTab.Screen.Send("recovery" + "\n")
#Starts a loop that looks for any broken files in the system error, it tries to continue for 2 minutes here. It will stop if no errors are found. 
    while True:
        screen_output = objTab.Screen.ReadString(error, 120)
        if screen_output:
            objTab.Screen.Send("con" + "\n")
        else:
            break
    #format_complete = 0
    #if format_complete == 0:
        #format_message = "FORMAT UNDER WAY"
        #crt.Dialog.MessageBox(format_message)
           
 #Waits for the root prompt to pop up and sends the configure command       
    objTab.Screen.WaitForStrings(prompts)
    #objTab.Screen.WaitForStrings(rootPrompt)
    objTab.Screen.Send("configure" + "\n")
#looks for the root with # prompt and sends the reset password command
    objTab.Screen.WaitForStrings(prompts)
    objTab.Screen.Send("set system root-authentication plain-text-password" + "\n")
#Sets the password to juniper1
    objTab.Screen.WaitForString(pwPrompt)
    objTab.Screen.Send("juniper1" + "\n")
#sets the passwordto juniper1 again for the confirm password prompt
    objTab.Screen.WaitForString(pwPrompt)
    objTab.Screen.Send("juniper1" + "\n")
#sends the commit command to the switch to save the changes
    objTab.Screen.WaitForString(conf)
    objTab.Screen.Send("commit" + "\n")
#sends 2 exit commands to the switch 
    objTab.Screen.WaitForStrings(prompts)
    objTab.Screen.Send("exit" + "\n")
    objTab.Screen.Send("exit" + "\n")    
#looks for the y/n prompt and reboots 
    objTab.Screen.WaitForString(rbPrompt)
    objTab.Screen.Send("y" + "\n")
#Sets the admPW to 1 to stop the above loop so that you can enter into regular boot mode
    admPW += 1
#starts another loop while admPW is 1
    while admPW == 1:
#sets the variables in the loop to text strings
        lgnPrompt = "login:"
        pwPrompt = "Password:"
        rootPrompt = "root@"
        rebootPrompt = "Rebooting..."
        resetPrompt = "FLASH:"
#looks for the login prompt and logs into switch
        objTab.Screen.WaitForString(lgnPrompt)
        objTab.Screen.Send("root" + "\n")
        objTab.Screen.WaitForString(pwPrompt)
        objTab.Screen.Send("juniper1" + "\n")
#looks for the root prompt and puts the switch into cli mode        
        objTab.Screen.WaitForStrings(prompts)
        objTab.Screen.Send("cli" + "\n")
#looks for the second root prompt and sends the zeroize command and confirms the reformat
        objTab.Screen.WaitForStrings(prompts)
        objTab.Screen.Send("request system zeroize" + "\n")
        objTab.Screen.Send("y" + "\n")
#Sets the admPW to 0 so that the above loop will stop and the first loop will begin.         
        
        #this IF statement is to create a popup box for the people who are not watching
        #the screen. There will be a popup that says uplug switch to indicate that the reset is finished.
        format_complete = objTab.Screen.ReadString(rebootPrompt) 
        if format_complete: 
            message = "Reformat Complete Please Uplug the Switch"
            crt.Dialog.MessageBox(message)
            admPW-=1
        
        

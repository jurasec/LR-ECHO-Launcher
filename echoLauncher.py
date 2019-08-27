# -*- coding: latin-1 -*-

### LogRhythm Echo usecases launcher
### Julio Cesar Rodriguez Dominguez <jurasec@gmail.com>


# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
import requests


def webRequestUseCases():
    urlApi = "https://localhost:33333/api/usecases"
    response = requests.get(urlApi, verify=False)
    results = response.json()["objects"]
    return results

def runUsecase(id, title):
    urlApiCase = "https://localhost:33333/api/execute/{0}".format(id)
    requests.get(urlApiCase, verify=False)
    
    print("Case [{1}] with id [{0}] executed. Press any key to continue...".format(id, title))
    input()

# Create the menu
menu = ConsoleMenu("LogRhythm Echo Launcher", "Choose an option")

# Create usecases items

options = webRequestUseCases()
# A FunctionItem runs a Python function when selected
for option in options:
    function_item = FunctionItem(option["title"], runUsecase, [option["id"], option["title"]])
    menu.append_item(function_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()

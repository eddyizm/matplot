from appJar import gui

def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)

def toolbar(btn):
    print(btn)
    if btn == "EXIT": app.stop()
    elif btn == "LOGOUT": logout()
    elif btn == "FILL": app.setTabBg("Tabs", app.getTabbedFrameSelectedTab("Tabs"), app.colourBox())
    elif btn == "PIE-CHART": app.showSubWindow("Statistics")
    elif btn == "FULL-SCREEN":
        if app.exitFullscreen():
            app.setToolbarIcon("FULL-SCREEN", "FULL-SCREEN")
        else:
            app.setSize("fullscreen")
            app.setToolbarIcon("FULL-SCREEN", "FULL-SCREEN-EXIT")
    elif btn == "CALENDAR": app.showSubWindow("DatePicker")
    elif btn == "ADDRESS-BOOK": app.showSubWindow("AddressBook")
    elif btn == "MAP": app.showSubWindow("Maps")
    elif btn == "ACCESS": app.showAccess()



app = gui('Login Window', '400x200')
app.addLabel('title', 'Data Visualization')
app.setBg('grey')
app.setLabelBg('title', 'red')

app.setFont(18)
app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")
app.setFocus("Username")

# toolbar
# tools = ["ABOUT", "REFRESH", "OPEN", "CLOSE", "SAVE",
#         "NEW", "SETTINGS", "PRINT", "SEARCH", "UNDO",
#         "REDO", "PREFERENCES", "HOME", "HELP", "CALENDAR",
#         "WEB", "OFF"]

# app.addToolbar(tools, tbFunc, findIcon=True)
app.addToolbar(["EXIT", "LOGOUT", "FILL", "ACCESS", "PIE-CHART", "CALENDAR", "ADDRESS-BOOK", "MAP", "FULL-SCREEN"], toolbar, findIcon=True)

#app.addToolbarButton('ABOUT', hello(), findIcon=True)

app.addButtons(["Submit", "Cancel"], press)        
app.go()

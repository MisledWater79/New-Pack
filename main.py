from tkinter import *
from tkinter import filedialog
import os
import uuid

manifest = {
    "format_version": 2,
    "header": {
        "name": "",
        "description": "",
        "uuid": str(uuid.uuid4()),
        "version": [1, 0, 0],
        "min_engine_version": [1, 13, 0]
    },
    "modules": [
        {
            "type": "data",
            "uuid": str(uuid.uuid4()),
            "version": [1, 0, 0]
        },
        {
            "type": "script",
            "language": "javascript",
            "uuid": str(uuid.uuid4()),
            "entry": "",
            "version": "1.0.0-beta"
        }
    ],
    "dependencies": [],
    "capabilities": [
        "script_eval"
    ]
}


class Application(Frame):
    def __init__(self, master):
        # Idk tbh
        Frame.__init__(self, master)
        self.root = master

        # Modules Variables
        self.a = BooleanVar()
        self.s = BooleanVar()
        self.s.set(True)
        self.u = BooleanVar()
        self.u.set(True)
        self.g = BooleanVar()
        self.n = BooleanVar()

        # Version Variable
        self.version = IntVar()
        self.version.set(2)

        # Input Variables
        self.packInput = Entry()
        self.folderInput = Entry()
        self.descriptionInput = Entry()
        self.scriptEntryInput = Entry()
        self.folderPathInput = Entry()

        # Pack Variable
        self.packName = "New Pack"
        self.folderName = "New Pack"
        self.description = "1.0.0"
        self.scriptEntry = "index.js"

        # File Path Variable
        self.folderPath = ""

        # Make UI
        self.ui()

    def ui(self):
        # Root configs
        self.root.title("New Pack")
        self.root.geometry("290x286")

        # Text for text inputs
        Label(root, text="Pack name:").grid(column=0, row=0, sticky='n')
        Label(root, text="Folder name:").grid(column=0, row=1, sticky='n')
        Label(root, text="Description:").grid(column=0, row=2, sticky='n')
        Label(root, text="Script Entry:").grid(column=0, row=3, sticky='n')
        Label(root, text="Packs Folder:").grid(column=0, row=4, sticky='n')

        # Text Inputs
        self.packInput = Entry(root, width=15)
        self.packInput.grid(column=1, row=0, sticky='w')
        self.packInput.insert(0, "New Pack")
        self.folderInput = Entry(root, width=15)
        self.folderInput.grid(column=1, row=1, sticky='w')
        self.folderInput.insert(0, "New Pack")
        self.descriptionInput = Entry(root, width=15)
        self.descriptionInput.grid(column=1, row=2, sticky='w')
        self.descriptionInput.insert(0, "1.0.0")
        self.scriptEntryInput = Entry(root, width=15)
        self.scriptEntryInput.grid(column=1, row=3, sticky='w')
        self.scriptEntryInput.insert(0, "index.js")
        self.folderPathInput = Entry(root, width=15)
        self.folderPathInput.grid(column=1, row=4, sticky='w')

        # Modules
        Label(root, text="--Modules--").grid(column=0, row=5, sticky='n')
        Checkbutton(root, text="Server Admin", variable=self.a).grid(column=0, row=6, sticky='w')
        Checkbutton(root, text="Server", variable=self.s, indicatoron=True).grid(column=0, row=7, sticky='w')
        Checkbutton(root, text="Server UI", variable=self.u, state="active").grid(column=0, row=8, sticky='w')
        Checkbutton(root, text="Server Gametest", variable=self.g).grid(column=0, row=9, sticky='w')
        Checkbutton(root, text="Server Net", variable=self.n).grid(column=0, row=10, sticky='w')

        # Version
        Label(root, text="--Version--").grid(column=1, row=6, sticky='n')
        Radiobutton(root, text="Stable", variable=self.version, value=1).grid(column=1, row=7, sticky='w')
        Radiobutton(root, text="Beta", variable=self.version, value=2).grid(column=1, row=8, sticky='w')
        Radiobutton(root, text="Preview", variable=self.version, value=3).grid(column=1, row=9, sticky='w')

        # Make Button
        Button(root, text="Make Pack", width=10, command=self.make).grid(column=2, row=12, sticky='e')

        # Browse Button
        Button(root, text="Browse", command=self.getpath).grid(column=2, row=4, sticky='n')

    def getpath(self):
        # Opens files explorer to get a folder
        self.folderPath = filedialog.askdirectory(initialdir=r"", title="Open")
        self.folderPathInput.insert(0, self.folderPath)

    def make(self):
        if self.folderPath == "":
            return
        # Set the inputs to the corresponding variables
        self.packName = self.packInput.get()
        self.folderName = self.folderInput.get()
        self.description = self.descriptionInput.get()
        self.scriptEntry = self.scriptEntryInput.get()

        # Set the parts in the manifest to what we want it to be
        manifest["header"]["name"] = self.packName
        manifest["header"]["description"] = self.description
        manifest["modules"][1]["entry"] = self.scriptEntry
        # Server-Admin
        if self.a.get():
            manifest["dependencies"].append({
                "module_name": "@minecraft/server-admin",
                "version": "1.0.0-beta"
            })
        # Server-Net
        if self.n.get():
            manifest["dependencies"].append({
                "module_name": "@minecraft/server-net",
                "version": "1.0.0-beta"
            })
        # Server-Gametest
        if self.g.get():
            manifest["dependencies"].append({
                "module_name": "@minecraft/server-gametest",
                "version": "1.0.0-beta"
            })
        # Server-UI
        if self.u.get() and self.version.get() == 2:
            manifest["dependencies"].append({
                "module_name": "@minecraft/server-ui",
                "version": "1.0.0-beta"
            })
        elif self.u.get():
            manifest["dependencies"].append({
                "module_name": "@minecraft/server-ui",
                "version": [0, 1, 0]
            })
        # Server
        if self.s.get() and self.version.get() == 2:
            manifest["dependencies"].append({
                "module_name": "@minecraft/server",
                "version": "1.0.0-beta"
            })
        elif self.s.get() and self.version.get() == 3:
            manifest["dependencies"].append({
                "module_name": "@minecraft/server",
                "version": "1.1.0-beta"
            })
        elif self.s.get() and self.version.get() == 1:
            manifest["dependencies"].append({
                "module_name": "@minecraft/server",
                "version": "1.0.0"
            })
        elif self.s.get():
            manifest["dependencies"].append({
                "module_name": "@minecraft/server",
                "version": [0, 1, 0]
            })

        # Check for duplicates
        finalpath = self.folderPath + "/" + self.folderName

        i = 2
        while os.path.exists(finalpath):
            finalpath = self.folderPath + "/" + self.folderName + " (" + str(i) + ")"
            i += 1

        # Make directories and files
        os.mkdir(finalpath)
        os.mkdir(finalpath + "/scripts")
        f = open(finalpath + "/manifest.json", 'w')
        f.write(str(manifest).replace("'", '"'))
        f.close()
        f = open(finalpath + "/scripts/" + self.scriptEntry, 'w')
        f.write("import { world } from '@minecraft/server';\n\nconsole.warn(\"Hello World\");")
        f.close()

        # Debug
        print(self.packName, self.folderName, self.description, self.scriptEntry,
              self.a.get(), self.s.get(), self.u.get(), self.g.get(), self.n.get(), self.version.get())
        print(self.folderPath)
        print(manifest)


# Make root and app then loop
root = Tk()
app = Application(root)
root.mainloop()

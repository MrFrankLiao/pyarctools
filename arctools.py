from tkinter import *
from tools.log.analysis import analysis
from tkinter.filedialog import askdirectory
import itertools
import threading
import time

done = False


def set_done(bool):
    global done
    done = bool


def get_done():
    return done


def animate():
    global Lb1
    while(get_done() == False):
        for c in itertools.cycle(['|', '/', '-', '\\']):
            Lb1.set('running, plz wait. ' + c)
            time.sleep(0.1)
            if get_done():
                Lb1.set("Done!!!!")
                break


def selectPath():
    path_ = askdirectory()
    path.set(path_)


def analysis_interface():
    t.start()
    analysis(start=start_time_text, end=end_time_text, path=path.get())
    set_done(True)

root = Tk()
root.title("ARCGIS TOOLS")
t = threading.Thread(target=animate)

path = StringVar()
delete_enable = BooleanVar()
Lb1 = StringVar()
start_time_text = StringVar()
end_time_text = StringVar()
Label(root, text="ANALYSIS LOG:").grid(row=0, column=0)

Label(root, text="START TIME(YYYY-MM-DD):").grid(row=1, column=0)
Entry(root, textvariable=start_time_text).grid(row=1, column=1, sticky=E)

Label(root, text="END TIME(YYYY-MM-DD):").grid(row=2, column=0)
Entry(root, textvariable=end_time_text).grid(row=2, column=1, sticky=E)

Label(root, text="TARGET PATH:").grid(row=3, column=0)
Entry(root, textvariable=path).grid(row=3, column=1)
Button(root, text="SELECT PATH", command=selectPath).grid(row=3, column=2)
Button(root, text="START TO ANALYSIS", command=analysis_interface).grid(row=3, column=3)

Label(root, textvariable=Lb1, text="").grid(row=4, column=1)

root.mainloop()


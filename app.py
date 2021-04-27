import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
import sys
import shutil
import subprocess
import networkx as nx
import graphviz
import pydot
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from subprocess import Popen, PIPE


def Constructor(status):
    status.config(text="Running functions...")
    if os.path.isfile('test.exe') == False:
        comp = subprocess.Popen(["g++", "-o", "test.exe", "slicer.cpp"],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        comp.wait()
    # if os.path.isfile('test2.exe') == False:
        # comp=subprocess.Popen(["g++","-o","test2.exe","DGL.cpp"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        # comp.wait()
    # if os.path.isfile('test3.exe') == False:
        # comp=subprocess.Popen(["g++","-o","test3.exe","SG.cpp"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        comp.wait()
    status.config(text="Ready...")


def Destructor(window):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        os.remove("main.cpp")
        if os.path.isfile("main.exe"):
            os.remove("main.exe")
        if os.path.isfile("test.exe"):
            os.remove("test.exe")
        # if os.path.isfile("test2.exe"):
         #   os.remove("test2.exe")
        # if os.path.isfile("test3.exe"):
         #   os.remove("test3.exe")
        window.destroy()
    exit()


def GraphMaker(graph):
    windoww = Tk()
    G = nx.DiGraph()
    with open('CD.txt') as data:
        CDnodes = []
        CDedges = []
        CDlines = []
        for line in data.readlines():
            line = line[:-1]
            line = line.split('|')
            #line=list(map(lambda txt: txt.lstrip(),line))
            CDlines.append(line)
        data.close()
        for line in CDlines:
            CDnodes.append(line[0])
            for i in range(1, len(line)):
                CDedges.append((line[i], line[0]))
        G.add_nodes_from(CDnodes)
        G.add_edges_from(CDedges, color='red', length=0.1)
    with open('AR.txt') as data:
        ARedges = []
        ARlines = []
        for line in data.readlines():
            line = line[:-1]
            line = line.split('|')
            ARlines.append(line)
        data.close()
        for line in ARlines:
            for i in range(1, len(line)):
                ARedges.append((line[i], line[0]))
        G.add_edges_from(ARedges, color='blue', length=0.2)
    with open('T.txt') as data:
        Tedges = []
        Tlines = []
        for line in data.readlines():
            line = line[:-1]
            line = line.split('|')
            Tlines.append(line)
        data.close()
        for line in Tlines:
            for i in range(1, len(line)):
                Tedges.append((line[i], line[0]))
        G.add_edges_from(Tedges, color='green', length=0.4)
    with open('PI.txt') as data:
        PIedges = []
        PIlines = []
        for line in data.readlines():
            line = line[:-1]
            line = line.split('|')
            PIlines.append(line)
        data.close()
        for line in PIlines:
            for i in range(1, len(line)):
                PIedges.append((line[i], line[0]))
        print(PIedges)
        G.add_edges_from(PIedges, color='cyan', length=0.5)
    with open('PO.txt') as data:
        POedges = []
        POlines = []
        for line in data.readlines():
            line = line[:-1]
            line = line.split('|')
            POlines.append(line)
        data.close()
        for line in POlines:
            for i in range(1, len(line)):
                POedges.append((line[i], line[0]))
        print(POedges)
        G.add_edges_from(POedges, color='magenta', length=0.6)
    with open('CE.txt') as data:
        CEedges = []
        CElines = []
        for line in data.readlines():
            line = line[:-1]
            line = line.split('|')
            CElines.append(line)
        data.close()
        for line in CElines:
            for i in range(1, len(line)):
                CEedges.append((line[i], line[0]))
        print(CEedges)
        G.add_edges_from(CEedges, color='violet', length=0.7)
    with open('RL.txt') as data:
        RLedges = []
        RLlines = []
        for line in data.readlines():
            line = line[:-1]
            line = line.split('|')
            RLlines.append(line)
        data.close()
        for line in RLlines:
            for i in range(1, len(line)):
                RLedges.append((line[i], line[0]))
        print(RLedges)
        G.add_edges_from(RLedges, color='purple', length=0.8)
    # labels={}
    # i=1
    # for node in G.nodes():
    #     labels[node]=node
    #     i=i+1
    # print(G.nodes())
    edgecolor = nx.get_edge_attributes(G, 'color').values()
    print(set(edgecolor))
    CDpatch = mpatches.Patch(color='red', label="Control/Data Dependent Edges")
    ARpatch = mpatches.Patch(color='blue', label="Affect Return Edges")
    Tpatch = mpatches.Patch(color='green', label="Transitive Edges")
    PIpatch = mpatches.Patch(color='cyan', label="Parameter In Edges")
    POpatch = mpatches.Patch(color='magenta', label="Parameter Out Edges")
    CEpatch = mpatches.Patch(color='violet', label="Calling Edges")
    RLpatch = mpatches.Patch(color='purple', label="Return Link Edges")
    fig = plt.figure(figsize=(20, 20))
    #pos = nx.nx_pydot.graphviz_layout(G,prog='neato')
    nx.draw_networkx(G, with_labels=True, edge_color=edgecolor,
                     font_size=8, alpha=0.7, node_color="skyblue")
    fig.legend(handles=[CDpatch, ARpatch, Tpatch,
               PIpatch, POpatch, CEpatch, RLpatch])
    dataPlot = FigureCanvasTkAgg(fig, master=windoww)
    dataPlot.draw()
    dataPlot.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    os.remove("CD.txt")
    os.remove("AR.txt")
    os.remove("T.txt")
    os.remove("PI.txt")
    os.remove("PO.txt")
    os.remove("CE.txt")
    os.remove("RL.txt")


def TargetFileRunner(status, codepreview, graph, nongraph, variablenames, output, InputEntry,lnbr):
    comp = subprocess.run(["javac", "source.java"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, input="")
    #line = codepreview.get(codepreview.curselection())
    #linenumber = line.split(' ', 1)[0]
    if len(variablenames.get()) != 0:
        Constructor(status)
        status.config(text="Running...")
        stdin = InputEntry.get('1.0', 'end-1c')
        print(stdin)
        linee=lnbr.get()
        input1 = str(linee)+'\n'+variablenames.get()+'\n'
        with open('inputt1.txt','w') as xyz:
            xyz.write(input1)
            xyz.close()
        with open('inputt2.txt','w') as xyz:
            xyz.write(stdin)
            xyz.close()
        input1 = bytes(input1, 'utf-8')                
        p = Popen(['test.exe'], stdout=PIPE, stdin=PIPE)
        p.stdin.write(input1)
        p.stdin.close()
        #path = 'C:/Users/Admin/Desktop/DAIICT/8th sem BTP/final/Application/Application/filee.txt'
        #sys.stdout = open(path, 'w')
        result = p.stdout.readlines()
        print(result)
        GraphMaker(graph)
        output.config(state='normal')
        output.delete('1.0', tk.END)
        output.insert(tk.END, result)
        output.config(state='disabled')
        status.config(text="Ready...")
        if os.path.isfile("outputnn.java"):
            os.remove("outputnn.java")
        if os.path.isfile("outputnn.class"):
            os.remove("outputnn.class")
        if os.path.isfile("input.txt"):
            os.remove("input.txt")
        if os.path.isfile("resultt.txt"):
            os.remove("resultt.txt")
        if os.path.isfile("inputt1.txt"):
            os.remove("inputt1.txt")
        if os.path.isfile("inputt2.txt"):
            os.remove("inputt2.txt")
        if os.path.isfile("source.class"):
            os.remove("source.class")
    else:
        messagebox.showwarning(
            "Enter the Variable Name", "Please Select a valid variable name from the line")

# def InputView(flag,flag1,InputEntry):
 #   flag1.set(flag)
    # print(flag1.get())
 #   if flag%2==0:
  #      InputEntry.config(state='normal')
   # else:
   #     InputEntry.delete('1.0',tk.END)
  #      InputEntry.config(state='disabled')


# Selects a file and copies to the current working directory irrespective of the OS
def FileSelector(root):
    root.withdraw()
    filelocation = filedialog.askopenfilename(
        title="Select a Java file", filetypes=[("Java file", '*.java')])
    cwd = os.getcwd()
    if filelocation is None:
        exit()
    filename = filelocation.split('/')[-1]   
    targetfile = cwd+'\\'+filename
    with open('fil','w') as xyz:
        xyz.write(filename)
        xyz.close()
    shutil.copyfile(filelocation, targetfile)
    Main(targetfile)


def Close(root):
    root.destroy()
    exit()


def New(window):
    FileSelector(window)


def Main(targetfile):
    window = tk.Tk()
    window.geometry("%dx%d+0+0" % (window.winfo_screenwidth() -
                    50, window.winfo_screenheight()-100))
    window.title("Java Slicer")
    # style=ttk.Style()
    # style.theme_use('clam')
    # print(style.theme_names())

    Menubar = tk.Menu(window)
    # file=tk.Menu(Menubar,tearoff=False)
    Menubar.add_command(label="New", command=lambda: New(window))
    Menubar.add_command(label="Quit(Alt+F4)",
                        command=lambda: Destructor(window))
    # Menubar.add_cascade(label="File",menu=file)
    # edit=tk.Menu(Menubar,tearoff=False)
    Menubar.add_command(label="Copy Slice")
    window.config(menu=Menubar)

    status = tk.Label(window, text="Ready...", bd=1,
                      relief=tk.SUNKEN, anchor=tk.E)
    status.pack(side=tk.BOTTOM, fill=tk.X)
    codeframe = tk.Frame(window)
    codeframe.pack(side=tk.LEFT)
    tk.Label(codeframe, text="CODE PREVIEW ", font=(
        "Times New Roman", 12), justify=tk.LEFT, anchor="n").pack()
    codebox = tk.Frame(codeframe)
    codebox.pack(side=tk.LEFT)
    visualization = tk.Frame(window)
    visualization.pack(side=tk.RIGHT)

    tab = ttk.Notebook(visualization)
    graph = tk.Frame(tab, bg='#34424B')
    nongraph = Tk()
    # tab.add(graph,text="Graph")
    #tab.add(nongraph, text="Slice")
    output = tk.Text(nongraph, width=100, height=90, font=(
        "Arial", 14), fg='#FFFFFF', bg='#36454F', state='disabled')
    gscrollv = tk.Scrollbar(nongraph, orient="vertical", command=output.yview)
    gscrollv.pack(side=tk.RIGHT, fill=tk.Y)
    output.config(yscrollcommand=gscrollv.set)
    gscrollh = tk.Scrollbar(
        nongraph, orient="horizontal", command=output.xview)
    gscrollh.pack(side=tk.BOTTOM, fill=tk.X)
    output.config(xscrollcommand=gscrollh.set)
    output.pack()
    tab.pack()

    codepreview = tk.Listbox(codebox, font=(
        "Arial", 14), width=85, height=20, fg='#FFFFFF', bg='#36454F')
    with open(targetfile, "r") as code:
        lines = code.readlines()
        i = 1
        for line in lines:
            codepreview.insert(tk.END, str(i)+" "+str(line))
            i = i+1
        code.close()
    FPscrollv = tk.Scrollbar(codebox, orient="vertical",
                             command=codepreview.yview)
    FPscrollv.pack(side=tk.RIGHT, fill=tk.Y)
    codepreview.config(yscrollcommand=FPscrollv.set)
    FPscrollh = tk.Scrollbar(
        codebox, orient="horizontal", command=codepreview.xview)
    codepreview.pack()
    FPscrollh.pack(side=tk.BOTTOM, fill=tk.X)
    codepreview.config(xscrollcommand=FPscrollh.set)

    SelectAlgo = tk.Frame(codeframe, bg='#36454F')
    InputFrame = tk.Frame(SelectAlgo, bg='#DCDCDC')
    # RadioFrame=tk.Frame(SelectAlgo)
    InputLabel = tk.Label(InputFrame, text="Input(stdin): ", bg='#DCDCDC')
    InputLabel.pack(side="left")
    InputEntryFrame = tk.Frame(InputFrame)
    InputEntry = tk.Text(InputEntryFrame, width=15, height=3)
    IEscrollv = tk.Scrollbar(
        InputEntryFrame, orient="vertical", command=InputEntry.yview)
    IEscrollv.pack(side=tk.RIGHT, fill=tk.Y)
    InputEntry.config(yscrollcommand=IEscrollv.set)

    SelectAlgo.pack(padx=60, pady=60)
    VariableFrame = tk.Frame(SelectAlgo)
    variablenameLabel = tk.Label(
        VariableFrame, text="Variable: ", bg='#DCDCDC')
    variablenames = tk.Entry(VariableFrame)
    variablenameLabel.pack(side="left")
    variablenames.pack(side="left")
    VariableFrame.pack(padx=20, pady=20)
    InputFrame.pack(padx=20, pady=20)
    Inp_lin = tk.Frame(SelectAlgo, bg='#DCDCDC')
    InputLabel = tk.Label(Inp_lin, text="Line Number: ", bg='#DCDCDC')
    lnbr = tk.Entry(Inp_lin)
    InputLabel.pack(side="left")
    lnbr.pack(side="left")
    Inp_lin.pack(padx=20, pady=20)
    # radio1.invoke()
    InputLabel.pack(side="left")
    InputEntryFrame.pack()
    InputEntry.pack(side="left")
    InputFrame.pack()
    runbutton = tk.Button(SelectAlgo, text="Run", command=lambda: TargetFileRunner(
        status, codepreview, graph, nongraph, variablenames, output, InputEntry,lnbr))
    runbutton.pack()

    window.protocol('WM_DELETE_WINDOW', lambda: Destructor(window))
    window.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x250")
    root.configure(bg="#ffffcc")
    tk.Label(root, text="JAVA SLICER",
             font=("Arial 14 bold"), relief=RIDGE).pack(padx=20, pady=20)
    tk.Label(root, text="Required: ", font=("Arial 14 bold"),
             relief=GROOVE).pack(padx=20, pady=20)
    # Ccompiler=subprocess.run(["gcc","-v"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    Cppcompiler = subprocess.run(
        ["g++", "-v"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    SelectFileButton = tk.Button(
        root, text="Select File...", relief=RAISED, command=lambda: FileSelector(root))
    # if Ccompiler.stderr!=b'':
    #     tk.Label(root,text="• GCC C Compiler",bg='green',font=("Arial 8 bold")).pack(padx=2,pady=2)
    # else:
    #     tk.Label(root,text="• GCC C Compiler",bg='red',font=("Arial 8 bold")).pack(padx=2,pady=2)
    #     SelectFileButton["state"]="disabled"
    if Cppcompiler.stderr != b'':
        tk.Label(root, text="• JAVA Compiler: Found", bg='green', relief=RIDGE,
                 font=("Arial 10 bold")).pack(padx=12, pady=12)
    else:
        tk.Label(root, text="• JAVA Compiler: Not Found", relief=RIDGE,
                 bg='red', font=("Arial 10 bold")).pack(padx=16, pady=16)
        SelectFileButton["state"] = "disabled"
    SelectFileButton.pack(padx=2, pady=2)
    root.title("JAVA Slicer")
    root.protocol('WM_DELETE_WINDOW', lambda: Close(root))
    root.mainloop()

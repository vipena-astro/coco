#Necessary libraries
import tkinter as tk
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from skimage.io import imread as imread

#Creation of the interactive window
window=tk.Tk()

#Handlers for different events in the interactive window
def handle_loadfile(event,master=window):
    #Files are loaded via the btn_loadfile Button
    global display_name #For reusing masters, so that Tkinter doesn't keep adding space downwards
    global display_content
    if display_name!='':
        master=display_content
    filename=entry.get() #Read the file name from the user input
    image=imread(filename) #Open the image
    fig,ax=plt.subplots()
    display=FigureCanvasTkAgg(fig,master=master)
    display.get_tk_widget().pack() #Add a pyplot axis to the master
    ax.imshow(image) #Load the image into the pyplot axis
    ax.set_axis_off()
    display_name=filename #Update masters
    display_content=display.get_tk_widget()
    lbl_messagebox['text']=filename+' loaded :)' #Send message to user
    
def handle_analyse(event,master=window):
    #Images are analysed via the btn_analyse Button
    global analysis_content #For reusing masters, so that Tkinter doesn't keep adding space downwards
    global analysis_image
    global analysis
    if display_name!='':
        master=analysis_content
    filename=entry.get()
    image=imread(filename) #Read the image and extract its channels
    r=image[:,:,0].flatten()
    g=image[:,:,1].flatten()
    b=image[:,:,2].flatten()
    c=np.array([r,g,b]).T
    print('image read')
    lbl_messagebox['text']='image read'
    fig,ax=plt.subplots()
    display=FigureCanvasTkAgg(fig,master=master)
    display.get_tk_widget().grid(row=0,column=1) #Add a pyplot axis to the master
    print('scattering')
    lbl_messagebox['text']='scattering'
    ax.scatter(eval(axes[0]),eval(axes[1]),c=c/255,s=.25) #Scatter-plot the pixels into the axis, according to the channels specified in global var. axes
    ax.set_xlabel(axes[0])
    ax.set_ylabel(axes[1])
    ax.set_xlim(0,255)
    ax.set_ylim(0,255)
    print('updating masters\n(Hold on, this may take a while)') #Inform the user (for some reason pyplot takes a while *here* if the image is large)
    lbl_messagebox['text']='updating masters (hold on, this may take a while)'
    analysis_content=display.get_tk_widget()
    analysis_image=fig

def handle_save(event):
    #Saving is handled by the btn_save Button
    filename=entry.get()
    analysis_image.savefig(filename.split('.')[0]+'_analysis_'+axes+'.jpg')
    print('saved!')
    lbl_messagebox['text']='saved!'

def handle_checkers(event,which='rg'):
    #Choosing the channels to use as main axes in the analysis is handled by these checkboxes
    global axes
    if which=='rg':
        btn_rg['relief']=tk.SUNKEN
        btn_rb['relief']=tk.RAISED
        btn_gb['relief']=tk.RAISED
    elif which=='rb':
        btn_rg['relief']=tk.RAISED
        btn_rb['relief']=tk.SUNKEN
        btn_gb['relief']=tk.RAISED
    else:
        btn_rg['relief']=tk.RAISED
        btn_rb['relief']=tk.RAISED
        btn_gb['relief']=tk.SUNKEN
    axes=which



#I will use a grid for the window layout
window.rowconfigure([0,1],minsize=15)
window.columnconfigure([0,1,2,3,4,5],minsize=30)

#Creation of the elements
canvas=tk.Label(text='Image',fg='black',bg='white',width=80,height=30) #Main canvas for the image in the x-y-colour space
analysis=tk.Label(text='Analysis',fg='black',bg='white',width=80,height=30) #Secondary canvas for the image in the channel-channel-colour space
entry=tk.Entry() #Entry for the user to specify the name of the file to load
btn_loadfile=tk.Button(text='Load',bg='white',fg='black',width=30,height=5) #Button to load the file specified in the entry
btn_analyse=tk.Button(text='Analyse',bg='white',fg='black',width=30,height=5) #Button to analyse the loaded image
btn_save=tk.Button(text='Save',bg='white',fg='black',width=30,height=5) #Button to save the analysis plot
btn_rg=tk.Button(text='rg',relief=tk.RAISED) #Button checked at double click when r-g are the analysis channels
btn_rb=tk.Button(text='rb',relief=tk.RAISED) #Button checked at double click when r-b are the analysis channels
btn_gb=tk.Button(text='gb',relief=tk.RAISED) #Button checked at double click when g-b are the analysis channels
lbl_messagebox=tk.Label()

#Organisation of the elements into the grid
canvas.grid(row=0,column=0)
analysis.grid(row=0,column=1)
entry.grid(row=1,column=0)
btn_loadfile.grid(row=1,column=1)
btn_analyse.grid(row=3,column=1)
lbl_messagebox.grid(row=5,column=0)
btn_save.grid(row=5,column=1)
btn_rg.grid(row=2,column=0)
btn_rb.grid(row=3,column=0)
btn_gb.grid(row=4,column=0)

#Flux control variables (see the definitions of the handlers above)
display_name=''
display_content=None
analysis_content=None
analysis_image=None
axes=''

#Binding of buttons so that they are constantly being queried on whether they are clicked or not
btn_loadfile.bind('<Button-1>',lambda ev: handle_loadfile(ev,master=canvas))
btn_analyse.bind('<Button-1>',lambda ev: handle_analyse(ev,master=analysis))
btn_save.bind('<Button-1>',handle_save)
btn_rg.bind('<Button-1>',lambda ev: handle_checkers(ev,which='rg'))
btn_rb.bind('<Button-1>',lambda ev: handle_checkers(ev,which='rb'))
btn_gb.bind('<Button-1>',lambda ev: handle_checkers(ev,which='gb'))

#Launching the mainloop
window.mainloop()

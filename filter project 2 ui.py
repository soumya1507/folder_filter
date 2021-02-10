import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk
import os,shutil
from PIL import Image
from tkinter import filedialog,messagebox
ext=[
{"audio_files":(".mp3",".m4a",".wav",".flac",".aif",".mpa")}
,{"python_files":(".py")}
,{"doc_files":(".doc",".pdf",".txt",".docx",".csv",".ppt",".pptx")}
,{"video_files":(".mp4",".mkv",".MKV",".flv",".mpeg")}
,{"java_files":(".java")}
,{"c_files":(".c",".cpp")}
,{"image_files":(".png",".jpg",".heic",".jpeg",".ico")}
,{"html_files":(".html")}
,{"compressed_file":(".zip",".arj",".rar")}
,{"htm_files":(".html")}]
win=tk.Tk()
win.geometry('1000x600')
win.wm_iconbitmap("icons.ico")
win.title("Folder Filter")

input_frame=tk.LabelFrame(win,text="")
input_frame.grid(row=0,columnspan=2,padx=150,pady=100)


font_size=tkfont.Font(family="Lucida Grande",size=20)
entry_frame=ttk.LabelFrame(input_frame,text="")
entry_frame.grid(row=4,columnspan=2,padx=5,pady=30)

entry_label=tk.Label(entry_frame,text="Enter full Folder Path...",font=font_size)
entry_label.grid(row=0,columnspan=2,padx=0,pady=5)
url=tk.StringVar()
url_entry=tk.Entry(entry_frame,width=50,textvariable=url)
url_entry.grid(row=1,column=0,padx=5,pady=10)

enter_btn=tk.Button(input_frame,text="Enter",background="green",width=20).grid(row=5,column=0,padx=100,pady=20)
clear_btn=tk.Button(input_frame,text="Clear",background="red",width=20).grid(row=5,column=1,padx=100,pady=20)


entry_frame=ttk.LabelFrame(input_frame,text="")
entry_frame.grid(row=4,columnspan=2,padx=5,pady=30)

entry_label=tk.Label(entry_frame,text="Enter full Folder Path...",font=font_size)
entry_label.grid(row=0,columnspan=2,padx=0,pady=5)
url=tk.StringVar()
url_entry=tk.Entry(entry_frame,width=50,textvariable=url)
url_entry.grid(row=1,column=0,padx=5,pady=10)
url_entry.focus()

def clear_btn():
    url_entry.delete(0,tk.END)
def enter_btn(event=None):
    folderpath=url.get()
    if folderpath=="":
        tk.messagebox.showwarning("warning","Enter folder path..")
    else:
        
        def file_finder(folder_path,extension_type,foldername):
            files=[]
            for file in os.listdir(folder_path):
                for extension in extension_type:
                    if file.endswith(extension):
                        if os.path.exists(folder_name):
                            pass
                        else:
                            os.mkdir(foldername)
                        files.append(file)
            return files
        if os.path.exists(folderpath):
            os.chdir(folderpath)
            for root,directory,filename in os.walk(folderpath):
                for i in filename:
                    if os.path.exists(os.path.join(root,i)):
                        pass
                    else:
                        shutil.move(os.path.join(root,i),folderpath)
            for root,directory,filename in os.walk(folderpath):
                for i in directory:
                    shutil.rmtree(i)

            for ext_dict in ext:
                os.chdir(folderpath)
                folder_name=list(ext_dict.keys())[0]
                temp=tuple(ext_dict.values())
                if type(temp[0])==tuple:
                    ext_list=temp[0]
                else:
                    ext_list=temp
        
        
                for f in file_finder(folderpath,ext_list,folder_name):
                    path=os.path.join(folderpath,folder_name)
                    os.chdir(path)
                    if os.path.exists(f):
                        pass
                    else:
                        source=folderpath+"\\"+f
                        shutil.move(source,path)
        
            for file in os.listdir(folderpath):
                if "."in file:
                    os.chdir(folderpath)
                    folder_name="extra"
                    if os.path.exists(folder_name):
                        pass
                    else:
                        os.mkdir(folder_name)
                        os.chdir(os.path.join(folderpath,"extra"))
                    shutil.move(os.path.join(folderpath,file),os.path.join(folderpath,"extra"))
                
            os.chdir(folderpath)
            messagebox.showinfo("successfull","Your files filtered successfully..")
            
        else:
            messagebox.showerror("Error","Invalid path")

        url_entry.delete(0,tk.END)
enter_btn_=tk.Button(input_frame,text="Enter",background="green",width=20,command=enter_btn).grid(row=5,column=0,padx=100,pady=20)
clear_btn=tk.Button(input_frame,text="Clear",background="red",width=20,command=clear_btn).grid(row=5,column=1,padx=100,pady=20)
win.bind('<Return>',enter_btn)
win.mainloop()

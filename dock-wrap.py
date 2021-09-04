from tkinter import *
import docker

img_list = []

app = Tk()
app.title('Docker Wrapper')

client = docker.from_env()
img = client.images.list()
cont = client.containers.list()

for i in cont:
    print(i.attrs)

def raise_frame(frame):
    frame.tkraise()

def image_list(lst):
    for i in img:
        val = (i.attrs['RepoDigests'])
        for j in val:
            lst.append(j.split('@')[0])

#    for size in img:
#        s = size.attrs['Size']
#        print(s)

    for image in lst:
        img_listbox.insert(END, image)


def container_list():
    pass

# frames


f1 = Frame(app)
img_listbox = Listbox(f1, width=130, height=10)
img_listbox.grid(row=0, column=0, sticky='news')
scrollbar = Scrollbar(f1)
scrollbar.grid(row=0, column=1, sticky='ns')

img_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=img_listbox.yview)


f2 = Frame(app)
cont_list = Listbox(f2, width=130, height=10)
cont_list.grid(row=0, column=0, sticky='news')
for i in ["c-one", "c-two", "c-three", "c-four"]:
    cont_list.insert(END, i)


f3 = Frame(app)
f4 = Frame(app)
f5 = Frame(app)
f6 = Frame(app)

for frame in (f1,f2,f3,f4,f5,f6):
    frame.grid(row=0,column=0, sticky='news')


right_frame = Frame(app)
img_btn = Button(right_frame, text="Images", width=30, command=lambda:raise_frame(f1)).grid(row=0)
cont_btn = Button(right_frame, text="Containers", width=30, command=lambda:raise_frame(f2)).grid(row=1)
net_btn = Button(right_frame, text="Networks", width=30, command=lambda:raise_frame(f3)).grid(row=2)
vol_btn = Button(right_frame, text="Volumes", width=30, command=lambda:raise_frame(f4)).grid(row=3)
doc_btn = Button(right_frame, text="Docker Files", width=30, command=lambda:raise_frame(f5)).grid(row=4)
doc_mac_btn = Button(right_frame, text="Docker-machine", width=30, command=lambda:raise_frame(f6)).grid(row=5)
right_frame.grid(row=0, column=1, sticky='news')

raise_frame(f1)
image_list(img_list)
app.mainloop()

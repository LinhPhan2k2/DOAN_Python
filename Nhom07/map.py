import folium
import webbrowser
import ipywidgets as widgets
from IPython.display import display
import gts
import tkinter 
from tkintermapview import TkinterMapView
from tkinter import *
from turtle import color

root_tk = tkinter.Tk()
root_tk.geometry("800x800")
root_tk.title("Nhom07_GTS")

lbl = Label(root_tk, text="Danh lam thắng cảnh", font=("Times New Roman Bold" ,30,),bg="yellow")
map_widget = TkinterMapView(root_tk,width=600, heigh = 400, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, y = 40)
map_widget.set_position(10.778970,106.698929)

marker_1 = map_widget.set_marker(10.778970,106.698929, text="Nhà thờ Đức Bà", text_color="black")
marker_2 = map_widget.set_marker(10.777030,106.703310, text="Nhà hát Thành Phố", text_color="black")
marker_3 = map_widget.set_marker(10.777130,106.695440, text="Dinh Độc Lập", text_color="black")
marker_4 = map_widget.set_marker(10.774110,106.700620, text="Chợ Bến Thành", text_color="black")
marker_5 = map_widget.set_marker(10.779731922055774,106.69209159639547, text="Bảo tàng chứng tích chiến tranh", text_color="black")
marker_6 = map_widget.set_marker(10.78825801187255,106.70474832523111, text="Bảo tàng lịch sử Việt Nam", text_color="black")
marker_7 = map_widget.set_marker(10.773940323533742, 106.70685775221801, text="Bến Bạch Đằng", text_color="black")

map_widget.pack(fill="both", expand=True)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom = 22)

myframe = LabelFrame(root_tk)
myframe.pack(pady=10)
my_lbl1  = Label(myframe, text="Mời nhập điểm bắt đầu: ", font=("Times New Romand",20))  #label nhập
my_lbl1.grid(row=0, column=0, pady=20, padx=10)

my_entry = Entry(myframe, font=("Times New Romand", 20)) #textbox nhập
my_entry.grid(row=0, column=1, padx=10)

my_button = Button(myframe, text="Tìm kiếm", font=("Times New Romand", 20)) #button
my_button.grid(row = 0, column = 2, padx = 30)
root_tk.mainloop()

# gts.main()
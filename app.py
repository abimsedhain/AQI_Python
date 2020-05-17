import tkinter as tk
import requests
import webbrowser

API_KEY = "API_KEY_HERE"

# HEIGHT & WIDTH FOR FRAME
HEIGHT = 400
WIDTH = 600

# HEIGHT & WIDTH FOR MENU ITEMS
mHEIGHT = 150
mWIDTH = 420

root = tk.Tk()

# Get screen width and height
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

# Calculate position x, y
x = (ws / 2) - (mWIDTH / 2)
y = (hs / 2) - (mHEIGHT / 2)


class Window(tk.Frame):
    def __init__(self, master):

        tk.Frame.__init__(self, master)
        self.master = master

        def center_window(w, h):
            # calculate position x, y
            x = (ws / 2) - (w / 2)
            y = (hs / 2) - (h / 2)
            self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        canvas = tk.Canvas(self.master, height=HEIGHT, width=WIDTH, bg='#61C9A8')
        canvas.pack()

        self.place(relx=0.5, rely=0.09, relwidth=0.2, relheight=0.1, anchor='n')
        self.master.title("AIR QUALITY INDEX")

        frame = tk.Frame(self.master, bg='green')
        frame.place(relx=0.5, rely=0.09, relwidth=0.2, relheight=0.1, anchor='n')

        button = tk.Button(frame, text="Get AQI", bg='#BDD358', highlightthickness=0, font=40, command=self.get_aqi)
        button.place(relheight=1, relwidth=1)
        
        lower_frame = tk.Frame(self.master, bg='black', bd=3)
        lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

        v = tk.StringVar()
        label = tk.Label(lower_frame, font=('Arial', 18), anchor='nw', justify='left', bd=15, textvariable=v)
        label.place(relwidth=1, relheight=1)

        my_menu = tk.Menu(self.master)
        self.master.config(menu=my_menu)

        # File menu
        file_menu = tk.Menu(my_menu, tearoff=False, font=12)
        my_menu.add_cascade(label="Air Quality Chart", menu=file_menu)

        # File Menu items
        file_menu.add_command(label="AQI Chart", command=self.aqi_chart)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exitProgram)

        # About Menu
        about_menu = tk.Menu(my_menu, tearoff=False, font=12)
        my_menu.add_cascade(label="Help", menu=about_menu)

        # About Menu Items
        about_menu.add_command(label="GET API KEY", command=self.api_key)
        about_menu.add_separator()
        about_menu.add_command(label="Support", command=self.support_me)
        about_menu.add_separator()
        about_menu.add_command(label="Feedback", command=self.feed_back)
        about_menu.add_separator()
        about_menu.add_command(label="About", command=self.about_app)

        self.master.geometry("600x400")
        self.master.resizable(False, False)
        center_window(WIDTH, HEIGHT)


    def exitProgram(self):
        exit()


    def aqi_chart(self):
        top = tk.Toplevel()
        top.title('Air Quality Index Chart')
        lbl = tk.Label(top, text="\n 0-50      | Good \n"
                                 "51-100   | Moderate \n"
                                 "101-150 | Unhealthy for Sensitive Groups \n"
                                 "151-200 | Unhealthy \n"
                                 "201-300 |  Very Unhealthy \n"
                                 "300+     | Hazardous", justify='left', font=14).pack()

        top.geometry('%dx%d+%d+%d' % (mWIDTH, mHEIGHT, x, y))
        top.resizable(False, False)

    # API KEY Hyperlink
    def api_key(self):
        webbrowser.open('https://www.iqair.com/', new=1)

    def support_me(self):
        top = tk.Toplevel()
        top.title('About App')
        lbl = tk.Label(top, text="\n \nYou can support me through GitHub.",
                       justify='left', font=12).pack()
        lbl1 = tk.Label(top, text="\n https://github.com/abimsedhain",
                        justify='left', font=12).pack()

        top.geometry('%dx%d+%d+%d' % (mWIDTH, mHEIGHT, x, y))
        top.resizable(False, False)

    def feed_back(self):
        top = tk.Toplevel()
        top.title('About App')
        lbl = tk.Label(top, text="\n \nIf you have any feedback then tweet me. \n",
                       justify='left', font=12).pack()
        lbl1 = tk.Label(top, text=" @ApexAbim \n \n",
                        justify='center', font=12).pack()

        top.geometry('%dx%d+%d+%d' % (self.master.mWIDTH, self.master.mHEIGHT, self.master.x, self.master.y))
        top.resizable(False, False)

    def about_app(self):
        top = tk.Toplevel()
        top.title('About App')
        lbl = tk.Label(top, text=" Air Quality Index App. \n", justify='center', font=12).pack()
        lbl2 = tk.Label(top,
                        text="This app displays the Air Quality Index and \n temperture according to the nearest station. ",
                        justify='left', font=12).pack()

        lbl1 = tk.Label(top, text="\n Version 1.0.0",
                        justify='left', font=12).pack()

        top.geometry('%dx%d+%d+%d' % (mWIDTH, mHEIGHT, x, y))
        top.resizable(False, False)

    def get_aqi(self):

        ap_key = API_KEY
        url = 'https://api.airvisual.com/v2/nearest_city?key=' + ap_key
        response = requests.get(url)
        aqi = response.json()

        city = aqi['data']['city']
        country = aqi['data']['country']
        aqindex = aqi['data']['current']['pollution']['aqius']
        temp = aqi['data']['current']['weather']['tp']
        
        #label['text'] = 'City: %s,%s \nAir Quality Index: %s \nTemp.(°C): %s' % (city, country, aqindex, temp)
        self.v.set('HELLO')


app = Window(root)
root.mainloop()

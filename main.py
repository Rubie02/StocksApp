from kivy.lang import  Builder
from kivymd.app import MDApp
import matplotlib
from matplotlib.widgets import Widget
matplotlib._png = None
from kivy.core.window import  Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList

import json
import requests
import Predict as Pre
import Cost
import branch
import Stocks_graph as Sg
import top_stocks as ts

#pip install kivy-garden
#garden install matplotlib
#python -m pip install --upgrade cmake matplotlib mpi4py numpy scipy yt
#python -m pip install --upgrade matplotlib==3.2.2
#multithread

username = ""
password = ""
company = []
nameshares = ""

class FormLogin(Screen):
    def login(self):
        global username, password, company
        url_database = "https://databasehtml-79e92-default-rtdb.firebaseio.com/.json"
        auth = 'vQVQE85jHdcn5DcHFLlb5pJDeDtxdNUBhFadEA68'
        signupUser = self.ids.login_user.text
        signupPassword = self.ids.login_password.text
        request = requests.get(url_database+'?auth='+auth)
        data = request.json()
        if data == None:
            self.dialog = MDDialog(
                    title = "Thông Báo",
                    text = "[color=#604ad7]Chưa có tài khoản này[/color]",
                    pos_hint = {'center_x':.5, 'center_y':.5}
                    )
            self.dialog.open()
            self.ids.login_user.text = ""
            self.ids.login_password.text = ""
        else:
            if signupUser in data.keys():
                if signupPassword == data[signupUser]['password']:
                    username = self.ids.login_user.text
                    password = self.ids.login_password.text
                    try:
                        company = data[signupUser]["company"]
                    except:
                        company = []
                    self.manager.current = "main"
                    self.manager.transition.direction = "up"  
                    self.ids.login_user.text = ""
                    self.ids.login_password.text = ""
                else:
                    self.dialog = MDDialog(
                        title = "Thông Báo",
                        text = "[color=#604ad7]Sai mật khẩu[/color]",
                        pos_hint = {'center_x':.5, 'center_y':.5}
                        )
                    self.dialog.open()
                    self.ids.login_password.text = ""
            else:
                self.dialog = MDDialog(
                    title = "Thông Báo",
                    text = "[color=#604ad7]Chưa có tài khoản này[/color]",
                    pos_hint = {'center_x':.5, 'center_y':.5}
                    )
                self.dialog.open()
                self.ids.login_user.text = ""
                self.ids.login_password.text = ""

class FormSignup(Screen):
    def signup(self):
        url_database = "https://databasehtml-79e92-default-rtdb.firebaseio.com/.json"
        auth = 'vQVQE85jHdcn5DcHFLlb5pJDeDtxdNUBhFadEA68'
        signupUser = self.ids.signup_user.text
        signupPassword = self.ids.signup_password.text
        signupConfirmPassword = self.ids.signup_confirmpassword.text
        request = requests.get(url_database+'?auth='+auth)
        data = request.json()
        if data == None:
            if signupPassword != signupConfirmPassword:
                    self.dialog = MDDialog(
                        title = "Thông Báo",
                        text = "[color=#604ad7]Mật khẩu không giống nhau[/color]",
                        pos_hint = {'center_x':.5, 'center_y':.5}
                        )
                    self.dialog.open()
            else:
                signup_info = str({f'\"{signupUser}\":{{"password":\"{signupPassword}\"}}'})
                signup_info = signup_info.replace("\'", "")
                to_database = json.loads(signup_info)
                requests.patch(url = url_database, json = to_database)
                self.manager.current = "login"
                self.manager.transition.direction = "right"  
                self.dialog = MDDialog(
                    title = "Thông Báo",
                    text = "[color=#604ad7]Đăng ký tài khoản thành công![/color]",
                    pos_hint = {'center_x':.5, 'center_y':.5}
                    )
                self.dialog.open()    
                self.ids.signup_user.text = ""
                self.ids.signup_password.text = ""
                self.ids.signup_confirmpassword.text = ""
        else:
            if signupUser in data.keys():
                self.dialog = MDDialog(
                    title = "Thông Báo",
                    text = "[color=#604ad7]Đã có tài khoản này[/color]",
                    pos_hint = {'center_x':.5, 'center_y':.5}
                    )
                self.dialog.open()
            else:
                if signupPassword != signupConfirmPassword:
                    self.dialog = MDDialog(
                        title = "Thông Báo",
                        text = "[color=#604ad7]Mật khẩu không giống nhau[/color]",
                        pos_hint = {'center_x':.5, 'center_y':.5}
                        )
                    self.dialog.open()
                else:
                    signup_info = str({f'\"{signupUser}\":{{"password":\"{signupPassword}\"}}'})
                    signup_info = signup_info.replace("\'", "")
                    to_database = json.loads(signup_info)
                    requests.patch(url = url_database, json = to_database)
                    self.manager.current = "login"
                    self.manager.transition.direction = "right"  
                    self.dialog = MDDialog(
                        title = "Thông Báo",
                        text = "[color=#604ad7]Đăng ký tài khoản thành công![/color]",
                        pos_hint = {'center_x':.5, 'center_y':.5}
                        )
                    self.dialog.open()    
                    self.ids.signup_user.text = ""
                    self.ids.signup_password.text = ""
                    self.ids.signup_confirmpassword.text = ""

class FormShares(Screen):
    def Load(self):
        self.ids.txtshares.text = nameshares
        box_info = self.ids.boxMoreInformation
        plt_info = Sg.candle_graph(nameshares)
        fig_info = FigureCanvasKivyAgg(plt_info.gcf())
        box_info.clear_widgets()
        box_info.add_widget(fig_info)

class FormMain(Screen, Widget):
    def on_row_press(self, table, row):
        global nameshares
        start_index, end_index = row.table.recycle_data[row.index]["range"]
        nameshares = row.table.recycle_data[start_index]["text"][-3:]
        self.manager.current = "shares"
        self.manager.transition.direction = "up"

    def Welcome(self):
        self.ids.lbwelcome.text = "Username: " + username

    def ShowCost(self):
        text = str(self.ids.txtgroud.text).upper()
        check = Cost.Check(text)
        if check==False:
            self.dialog = MDDialog(
                        title = "Thông Báo",
                        text = "[color=#604ad7]Không có nhóm cổ phiếu này[/color]",
                        pos_hint = {'center_x':.5, 'center_y':.5}
                        )
            self.dialog.open()
        else:
            boxcost = self.ids.boxcost
            dt = Cost.Cost(text)
            dt.bind(on_row_press=self.on_row_press)
            boxcost.clear_widgets()
            boxcost.add_widget(dt)
        #self.ids.txtgroud.text = ""

    def ShowBranchCost(self):
        text = str(self.ids.txtbranchground.text)
        check = branch.check(text)
        if check==False:
            self.dialog = MDDialog(
                        title = "Thông Báo",
                        text = "[color=#604ad7]Không có ngành này[/color]",
                        pos_hint = {'center_x':.5, 'center_y':.5}
                        )
            self.dialog.open()
        else:
            boxcost = self.ids.boxbranch
            dt = branch.branchCost(text)
            dt.bind(on_row_press=self.on_row_press)
            boxcost.clear_widgets()
            boxcost.add_widget(dt)
        #self.ids.txtbranchground.text = ""
    
    def ShowFollow(self):
        url_database = "https://databasehtml-79e92-default-rtdb.firebaseio.com/.json"
        text = str(self.ids.txtfollow.text).upper()
        check = Pre.Check(text)
        if check==False:
            self.dialog = MDDialog(
                        title = "Thông Báo",
                        text = "[color=#604ad7]Không có mã cổ phiếu này[/color]",
                        pos_hint = {'center_x':.5, 'center_y':.5}
                        )
            self.dialog.open()
        else:
            if text in company:
                self.dialog = MDDialog(
                        title = "Thông Báo",
                        text = "[color=#604ad7]Đã theo dõi mã cổ phiếu này[/color]",
                        pos_hint = {'center_x':.5, 'center_y':.5}
                        )
                self.dialog.open()
            else:
                company.append(text)
            jsoncompany = json.dumps(company)
            acc_info = str({f'\"{username}\":{{"password":\"{password}\", "company":{jsoncompany}}}'})
            acc_info = acc_info.replace("\'", "")
            to_database = json.loads(acc_info)
            requests.patch(url = url_database, json = to_database)
            self.dialog = MDDialog(
                        title = "Thông Báo",
                        text = "[color=#604ad7]Đã thêm mã cổ phiếu[/color]",
                        pos_hint = {'center_x':.5, 'center_y':.5}
                        )
            self.dialog.open()
            boxcost = self.ids.boxFollow
            dt = Cost.CostFollow(company)
            dt.bind(on_row_press=self.on_row_press)
            boxcost.clear_widgets()
            boxcost.add_widget(dt)
        self.ids.txtfollow.text = ""

    def ShowListFollow(self):
        if not company:
            self.dialog = MDDialog(
                        title = "Thông Báo",
                        text = "[color=#604ad7]Chưa có danh sách cổ phiểu theo dõi[/color]",
                        pos_hint = {'center_x':.5, 'center_y':.5}
                        )
            self.dialog.open()
        else:
            boxcost = self.ids.boxFollow
            dt = Cost.CostFollow(company)
            dt.bind(on_row_press=self.on_row_press)
            boxcost.clear_widgets()
            boxcost.add_widget(dt)
    
    def ShowTopStocks(self):
        text = str(self.ids.txttopground.text)
        if len(text)==0:
            self.dialog = MDDialog(
                        title = "Thông Báo",
                        text = "[color=#604ad7]Nhập nhóm hoặc ngành cổ phiếu[/color]",
                        pos_hint = {'center_x':.5, 'center_y':.5}
                        )
            self.dialog.open()
        else:
            if ts.check_group_stock(text):
                dt, counted = ts.list_top_stocks(text)
                self.dialog = MDDialog(
                        title = "Thông Báo",
                        text = f"[color=#604ad7]Cổ phiểu top : {counted}[/color]",
                        pos_hint = {'center_x':.5, 'center_y':.5}
                        )
                self.dialog.open()
                boxcost = self.ids.boxTopStock
                dt.bind(on_row_press=self.on_row_press)
                boxcost.clear_widgets()
                boxcost.add_widget(dt)
            else:
                self.dialog = MDDialog(
                        title = "Thông Báo",
                        text = "[color=#604ad7]Không có nhóm/ngành cổ phiếu[/color]",
                        pos_hint = {'center_x':.5, 'center_y':.5}
                        )
                self.dialog.open()

    def RefreshFollow(self):
        global company
        company = []
        self.ids.txtgroud.text = ""
        self.ids.txtfollow.text = ""
        self.ids.txtPredict.text = ""

    def ShowPredict(self):
        text = str(self.ids.txtPredict.text).upper()
        check = Pre.Check(text)
        if check==False:
            self.dialog = MDDialog(
                        title = "Thông Báo",
                        text = "[color=#604ad7]Không có mã cổ phiếu này[/color]",
                        pos_hint = {'center_x':.5, 'center_y':.5}
                        )
            self.dialog.open()  
        else:
            predicted_val, plt = Pre.Predict(text)
            self.dialog = MDDialog(
                        title = "Dự đoán",
                        text = f"[color=#604ad7]Giá trị cổ phiếu {text} ngày mai là {predicted_val}[/color]",
                        pos_hint = {'center_x':.5, 'center_y':.5}
                        )
            self.dialog.open()
            pre = str(predicted_val)
            txt = self.ids.tommorrow
            txt.text = pre
            box_predict = self.ids.box
            fig = FigureCanvasKivyAgg(plt.gcf())
            box_predict.clear_widgets()
            box_predict.add_widget(fig)
        #self.ids.txtPredict.text = ""

class ContentNavigationDrawer(BoxLayout):
    pass

class DrawerList(ThemableBehavior, MDList):
    pass

class WindowManager(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        Window.size = (350,600)

MainApp().run()
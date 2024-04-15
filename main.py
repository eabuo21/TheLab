from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class TheLabApp(App):
    pass
class WidgetExample(GridLayout):
    count = 0
    my_text= StringProperty (str(count))
    def on_button_click(self):
        print("you clicked")
        self.count += 1
        self.my_text= str(self.count)

    def on_toggle_button_state(self,togglebutton):
        print("button toggled" +togglebutton.state)
        if togglebutton.state == "normal":
            togglebutton.text="off"
        else:
            togglebutton.text="ON"
class MainWidget(Widget):
    pass

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs  ):
        super().__init__(**kwargs)
        for i in range (0, 100):
           #     spacing=(.2, .2, .2, .2)
            self.orientation="rl-tb"
            b= Button(text=str(i +1), size_hint=(None, None), size=((dp(100)), (dp(100))) )
            self.add_widget(b)
class BoxLayoutExample(BoxLayout):
    pass
class AnchorLayoutExample(AnchorLayout):
    pass
class GridLayoutExample(GridLayout):
    pass

"""    def __init__ (self, **kwargs):
       super().__init__(**kwargs)
       b1 = Button(text="A")
       b2 = Button(text="B")
       b3= Button(text="C")
       self.add_widget(b1)
       self.add_widget(b2)
       self.add_widget(b3)

"""










TheLabApp().run()
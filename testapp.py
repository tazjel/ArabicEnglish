import kivy
kivy.require('1.7.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class HomeScreen(GridLayout):

	def __init__(self, **kwargs):

			super(HomeScreen, self).__init__(**kwargs)
			self.searchbar = TextInput(multiline=False)
			self.add_widget(self.searchbar)
			Label(text='Bedouin Translator')


class TransApp(App):

    def build(self):

        return HomeScreen()



if __name__ == '__main__':
    TransApp().run()

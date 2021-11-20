from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:

    orientation: "vertical"
    padding: "6dp"
    spacing: "6dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "logo-ege.png"

    MDLabel:
        text: "Подготовка к ЕГЭ"
        font_style: "Button"
        adaptive_height: True

    ScrollView:

        MDList:

            OneLineListItem:
                text: "О программе"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Задание 1"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"
            
            OneLineListItem:
                text: "Задание 2"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 3"

            OneLineListItem:
                text: "Выход"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = exit()        


MDScreen:

    MDNavigationLayout:
        x: toolbar.height

        MDToolbar:
            id: toolbar
            pos_hint: {"top": 1}
            elevation: 10
            title: "Подготовка к ЕГЭ"
            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]] 

        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"

                GridLayout:
                    cols: 2

                    MDToolbar:
                        id: toolbar
                        pos_hint: {"top": 1}
                        elevation: 20
                        title: "О программе"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                MDLabel:
                    text: "Экран 1"    
                

            MDScreen:
                name: "scr 2"

                BoxLayout:
                    orientation: "vertical"
                        
                    MDToolbar:
                        id: toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: "Задание 1"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    
                    MDBottomNavigation:
                        panel_color: get_color_from_hex("#2196f4")
                        selected_color_background: get_color_from_hex("#2196f4")
                        text_color_active: get_color_from_hex("#fafafa")
                    
                        MDBottomNavigationItem:
                            name: 'screen 1'
                            text: 'Что проверяет?'
                            icon: 'brain'
                    
                            ScrollView:
                                
                                BoxLayout:
                                    orientation: "vertical"
                                    size_hint_y: None
                                    height: self.minimum_height
                                    padding: 20
                                    spacing: 10
                                    
                                    MDLabel:
                                        text: 'Использование и анализ информационных моделей (таблицы, диаграммы, графики).'
                                        bold: True
                                        font_styles: "H5" 
                                        size_hint_y: None
                                        height: self.texture_size[1]
                                        halign: 'center'
                                                                         
                                    MDLabel:
                                        text: 'Что проверяет данное задание?'
                                        bold: True
                                        font_styles: "Subtitle1"
                                        size_hint_y: None
                                        height: self.texture_size[1]
                                        halign: 'left'
                                    
                                    MDLabel:
                                        text: 'Умение представлять и считывать данные в разных типах информационных моделей (схемы, карты, таблицы, графики и формулы).'
                                        size_hint_y: None
                                        height: self.texture_size[1]
                                        halign: 'justify'

                                    MDLabel:
                                        text: 'Умение интерпретировать результаты, получаемые в ходе моделирования реальных процессов.'
                                        size_hint_y: None
                                        height: self.texture_size[1]
                                        halign: 'justify'
                                           
                        MDBottomNavigationItem:
                            name: 'screen 2'
                            text: 'Что нужно знать?'
                            font_styles: "H5"
                            icon: 'book-open-page-variant'
                
                            MDLabel:
                                text: 'Что нужно знать?'
                                halign: 'center'
                        
                        MDBottomNavigationItem:
                            name: 'screen 3'
                            text: 'Практика'
                            icon: 'border-color'

                            MDLabel:
                                text: 'Практика'
                                halign: 'center'
            
            
            MDScreen:
                name: "scr 3"

                BoxLayout:
                    orientation: "vertical"
                        
                    MDToolbar:
                        id: toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: "Задание 2"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    
                    MDBottomNavigation:
                        panel_color: get_color_from_hex("#2196f4")
                        selected_color_background: get_color_from_hex("#2196f4")
                        text_color_active: get_color_from_hex("#fafafa")
                        text_color: 
                    
                        MDBottomNavigationItem:
                            name: 'screen 1'
                            text: 'Что проверяет?'
                            icon: 'brain'
                    
                            BoxLayout:
                                orientation: "vertical"
                                
                                MDLabel:
                                    text: 'Что проверяет'
                                    halign: 'center'
                                    
                        MDBottomNavigationItem:
                            name: 'screen 2'
                            text: 'Теория'
                            icon: 'book-open-page-variant'
                
                            MDLabel:
                                text: 'Теория'
                                halign: 'center'
                        
                        MDBottomNavigationItem:
                            name: 'screen 3'
                            text: 'Практика'
                            icon: 'border-color'
                
                            MDLabel:
                                text: 'Практика'
                                halign: 'center'
            
        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer







'''


class ContentNavigationDrawer(MDBoxLayout, GridLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()



class MyApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)


if __name__ in ('__main__', '__android__'):
    MyApp().run()
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget, TwoLineIconListItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.icon_definitions import md_icons
from kivymd.uix.segmentedcontrol import MDSegmentedControl, MDSegmentedControlItem

# Устанавливаем размер окна для тестирования
Window.size = (390, 844)

class BottomNavigation(MDBoxLayout):
    def __init__(self, current_screen="main", **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.adaptive_height = True
        self.spacing = "10dp"
        self.padding = "10dp"
        self.md_bg_color = "white"
        self.size_hint_x = 1  # Растягиваем на всю ширину

        screens = {
            "main": {"icon": "home", "name": "Главная"},
            "message": {"icon": "email", "name": "Сообщения"},
            "schedule": {"icon": "calendar", "name": "Расписание"},
            "notifications": {"icon": "bell", "name": "Уведомления"},
            "profile": {"icon": "account", "name": "Профиль"}
        }

        # Добавляем равномерное распределение кнопок
        for screen, data in screens.items():
            box = MDBoxLayout(
                adaptive_width=True,
                size_hint_x=1/len(screens)  # Равномерное распределение
            )
            
            btn = MDIconButton(
                icon=data["icon"],
                theme_icon_color="Custom",
                icon_color="darkorange" if screen == current_screen else "grey",
                pos_hint={"center_x": .5, "center_y": .5},
                on_release=lambda x, s=screen: self.switch_screen(s)
            )
            btn._screen_name = screen  # Добавляем атрибут для идентификации экрана
            
            if screen == "notifications":
                btn.badge_icon = "1"
            
            box.add_widget(btn)
            self.add_widget(box)

    def switch_screen(self, screen_name):
        app = MDApp.get_running_app()
        app.switch_screen(screen_name)

KV = '''
MDScreen:
    MDNavigationLayout:
        ScreenManager:
            id: screen_manager
            
            # Главный экран
            MDScreen:
                name: 'main'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: "InStudy"
                        elevation: 0
                        pos_hint: {"top": 1}
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: "dodgerblue"
                        specific_text_color: "white"
                    
                    ScrollView:
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: "16dp"
                            spacing: "16dp"
                            adaptive_height: True
                            
                            MDLabel:
                                text: "Быстрые действия"
                                bold: True
                                font_style: "H6"
                                adaptive_height: True
                                
                            MDGridLayout:
                                cols: 2
                                spacing: "16dp"
                                adaptive_height: True
                                
                                # Карточка расписания
                                MDCard:
                                    size_hint: None, None
                                    size: "160dp", "120dp"
                                    md_bg_color: "darkorange"
                                    padding: "8dp"
                                    on_release: app.switch_screen('schedule')
                                    
                                    MDBoxLayout:
                                        orientation: 'vertical'
                                        spacing: "4dp"
                                        
                                        MDIconButton:
                                            icon: "calendar"
                                            theme_icon_color: "Custom"
                                            icon_color: "white"
                                            pos_hint: {"center_x": .5}
                                            icon_size: "36sp"
                                            
                                        MDLabel:
                                            text: "Расписание"
                                            halign: "center"
                                            theme_text_color: "Custom"
                                            text_color: "white"
                                            bold: True
                                            
                                        MDLabel:
                                            text: "Сегодня 4 занятия"
                                            halign: "center"
                                            theme_text_color: "Custom"
                                            text_color: "white"
                                            font_style: "Caption"
                                
                                # Карточка дисциплин
                                MDCard:
                                    size_hint: None, None
                                    size: "160dp", "120dp"
                                    md_bg_color: "darkorange"
                                    padding: "8dp"
                                    on_release: app.switch_screen('courses')
                                    
                                    MDBoxLayout:
                                        orientation: 'vertical'
                                        spacing: "4dp"
                                        
                                        MDIconButton:
                                            icon: "book"
                                            theme_icon_color: "Custom"
                                            icon_color: "white"
                                            pos_hint: {"center_x": .5}
                                            icon_size: "36sp"
                                            
                                        MDLabel:
                                            text: "Дисциплины"
                                            halign: "center"
                                            theme_text_color: "Custom"
                                            text_color: "white"
                                            bold: True
                                            
                                        MDLabel:
                                            text: "14 активных курсов"
                                            halign: "center"
                                            theme_text_color: "Custom"
                                            text_color: "white"
                                            font_style: "Caption"
                            
                            MDLabel:
                                text: "Последняя активность"
                                bold: True
                                font_style: "H6"
                                adaptive_height: True
                            
                            MDList:
                                id: activity_list
                                adaptive_height: True
                                
                            MDLabel:
                                text: "Полезные статьи"
                                bold: True
                                font_style: "H6"
                                adaptive_height: True
                            
                            MDList:
                                id: articles_list
                                adaptive_height: True

            # Экран написать преподавателю
            MDScreen:
                name: 'message'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: "Связь с преподавателем"
                        elevation: 0
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: "dodgerblue"
                        specific_text_color: "white"
                        
                    ScrollView:
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: "16dp"
                            spacing: "16dp"
                            adaptive_height: True
                            
                            Widget:
                                size_hint_y: None
                                height: "80dp"
                            
                            MDLabel:
                                text: "Появились вопросы?"
                                halign: "center"
                                font_style: "H5"
                                bold: True
                            
                            MDLabel:
                                text: "Напишите преподавателю!"
                                halign: "center"
                                theme_text_color: "Secondary"
                            
                            MDTextField:
                                hint_text: "Напишите ФИО преподавателя"
                                mode: "rectangle"
                                
                            MDFlatButton:
                                text: "Перейти в чат"
                                md_bg_color: "darkorange"
                                text_color: "white"
                                size_hint_x: 1
                                height: "48dp"

            # Экран расписания
            MDScreen:
                name: 'schedule'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: "Расписание"
                        elevation: 0
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: "dodgerblue"
                        specific_text_color: "white"
                        
                    ScrollView:
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: "16dp"
                            spacing: "16dp"
                            adaptive_height: True
                            
                            MDLabel:
                                text: "Сегодня"
                                bold: True
                                font_style: "H6"
                                adaptive_height: True
                            
                            MDLabel:
                                text: "22 июня 2025, понедельник"
                                theme_text_color: "Secondary"
                                adaptive_height: True
                            
                            MDList:
                                id: schedule_list
                                adaptive_height: True

            # Экран уведомлений
            MDScreen:
                name: 'notifications'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: "Уведомления"
                        elevation: 0
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: "dodgerblue"
                        specific_text_color: "white"
                        
                    ScrollView:
                        MDList:
                            id: notifications_list
                            padding: "16dp"
                            spacing: "8dp"

            # Экран профиля
            MDScreen:
                name: 'profile'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: "Профиль"
                        elevation: 0
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: "dodgerblue"
                        specific_text_color: "white"
                    
                    ScrollView:
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: "16dp"
                            spacing: "16dp"
                            adaptive_height: True
                            
                            MDBoxLayout:
                                orientation: 'vertical'
                                spacing: "16dp"
                                adaptive_height: True
                                padding: "0dp", "16dp", "0dp", "16dp"
                            
                                MDIconButton:
                                    icon: "account-circle"
                                    theme_icon_color: "Custom"
                                    icon_color: "dodgerblue"
                                    icon_size: "86sp"
                                    pos_hint: {"center_x": .5}
                                    size_hint_y: None
                                    height: "86dp"
                                
                                MDLabel:
                                    text: "Иван Петров"
                                    halign: "center"
                                    font_style: "H5"
                                    bold: True
                                    size_hint_y: None
                                    height: "36dp"
                                
                                MDLabel:
                                    text: "Студент 2 курса"
                                    halign: "center"
                                    theme_text_color: "Secondary"
                                    size_hint_y: None
                                    height: "24dp"
                                
                                MDLabel:
                                    text: "Группа: ИС-21-1"
                                    halign: "center"
                                    theme_text_color: "Secondary"
                                    size_hint_y: None
                                    height: "24dp"
                            
                            MDGridLayout:
                                cols: 3
                                spacing: "16dp"
                                adaptive_height: True
                                
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    adaptive_height: True
                                    
                                    MDLabel:
                                        text: "4.7"
                                        halign: "center"
                                        font_style: "H4"
                                        bold: True
                                    
                                    MDLabel:
                                        text: "Средний балл"
                                        halign: "center"
                                        theme_text_color: "Secondary"
                                
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    adaptive_height: True
                                    
                                    MDLabel:
                                        text: "18"
                                        halign: "center"
                                        font_style: "H4"
                                        bold: True
                                    
                                    MDLabel:
                                        text: "Дисциплин"
                                        halign: "center"
                                        theme_text_color: "Secondary"
                                
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    adaptive_height: True
                                    
                                    MDLabel:
                                        text: "85%"
                                        halign: "center"
                                        font_style: "H4"
                                        bold: True
                                    
                                    MDLabel:
                                        text: "Посещаемость"
                                        halign: "center"
                                        theme_text_color: "Secondary"
                            
                            MDLabel:
                                text: "Быстрые действия"
                                bold: True
                                font_style: "H6"
                                adaptive_height: True
                            
                            MDGridLayout:
                                cols: 2
                                spacing: "16dp"
                                adaptive_height: True
                                
                                MDFlatButton:
                                    text: "Мои оценки"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    md_bg_color: "darkorange"
                                    size_hint_x: 1
                                
                                MDFlatButton:
                                    text: "Расписание"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    md_bg_color: "darkorange"
                                    size_hint_x: 1
                            
                            MDLabel:
                                text: "Настройки"
                                bold: True
                                font_style: "H6"
                                adaptive_height: True
                            
                            MDList:
                                adaptive_height: True
                                
                                OneLineIconListItem:
                                    text: "Настройки уведомлений"
                                    IconLeftWidget:
                                        icon: "bell"
                                
                                OneLineIconListItem:
                                    text: "Безопасность"
                                    IconLeftWidget:
                                        icon: "shield-check"
                                
                                OneLineIconListItem:
                                    text: "Общие настройки"
                                    IconLeftWidget:
                                        icon: "cog"
                                
                                OneLineIconListItem:
                                    text: "Выйти из аккаунта"
                                    theme_text_color: "Custom"
                                    text_color: "red"
                                    IconLeftWidget:
                                        icon: "logout"
                                        theme_text_color: "Custom"
                                        text_color: "red"

            # Экран дисциплин
            MDScreen:
                name: 'courses'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: "Дисциплины"
                        elevation: 0
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: "dodgerblue"
                        specific_text_color: "white"
                    
                    ScrollView:
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: "16dp"
                            spacing: "16dp"
                            adaptive_height: True
                            
                            MDLabel:
                                text: "Активные курсы"
                                bold: True
                                font_style: "H6"
                                adaptive_height: True
                            
                            MDList:
                                id: courses_list
                                adaptive_height: True

            # Экран библиотеки
            MDScreen:
                name: 'library'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: "Электронная библиотека"
                        elevation: 0
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: "dodgerblue"
                        specific_text_color: "white"
                    
                    ScrollView:
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: "16dp"
                            spacing: "16dp"
                            adaptive_height: True
                            
                            MDTextField:
                                hint_text: "Поиск по названию, автору или предмету..."
                                mode: "rectangle"
                                
                            MDSegmentedControl:
                                MDSegmentedControlItem:
                                    text: "Все"
                            
                            MDList:
                                id: library_list
                                adaptive_height: True

            # Экран зачетной книжки
            MDScreen:
                name: 'gradebook'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: "Зачётная книжка"
                        elevation: 0
                        left_action_items: [["arrow-left", lambda x: app.switch_screen('main')]]
                        md_bg_color: "dodgerblue"
                        specific_text_color: "white"
                    
                    ScrollView:
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: "16dp"
                            spacing: "16dp"
                            adaptive_height: True
                            
                            MDBoxLayout:
                                orientation: 'horizontal'
                                adaptive_height: True
                                spacing: "16dp"
                                
                                MDLabel:
                                    text: "4.47"
                                    font_style: "H4"
                                    bold: True
                                    theme_text_color: "Primary"
                                    adaptive_height: True
                                
                                MDLabel:
                                    text: "Средний балл"
                                    theme_text_color: "Secondary"
                                    adaptive_height: True
                            
                            MDBoxLayout:
                                orientation: 'horizontal'
                                adaptive_height: True
                                spacing: "16dp"
                                
                                MDLabel:
                                    text: "18"
                                    font_style: "H4"
                                    bold: True
                                    theme_text_color: "Primary"
                                    adaptive_height: True
                                
                                MDLabel:
                                    text: "Кредитов"
                                    theme_text_color: "Secondary"
                                    adaptive_height: True
                            
                            MDLabel:
                                text: "Оценки по дисциплинам"
                                bold: True
                                font_style: "H6"
                                adaptive_height: True
                            
                            MDList:
                                id: grades_list
                                adaptive_height: True

            # Экран навигатора по InStudy
            MDScreen:
                name: 'navigator'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: "Навигатор по InStudy"
                        elevation: 0
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: "dodgerblue"
                        specific_text_color: "white"
                    
                    ScrollView:
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: "16dp"
                            spacing: "16dp"
                            adaptive_height: True
                            
                            MDLabel:
                                text: "Справочник по работе с платформой"
                                bold: True
                                font_style: "H6"
                                adaptive_height: True
                            
                            MDList:
                                OneLineIconListItem:
                                    text: "Модули"
                                    IconLeftWidget:
                                        icon: "view-grid"
                                
                                OneLineIconListItem:
                                    text: "Главная страница"
                                    IconLeftWidget:
                                        icon: "home"
                                
                                OneLineIconListItem:
                                    text: "Виджеты рабочего стола"
                                    IconLeftWidget:
                                        icon: "widgets"
                                
                                OneLineIconListItem:
                                    text: "Сообщения"
                                    IconLeftWidget:
                                        icon: "email"
                                
                                OneLineIconListItem:
                                    text: "Расписание"
                                    IconLeftWidget:
                                        icon: "calendar"
                                
                                OneLineIconListItem:
                                    text: "Учебно-методические пособия"
                                    IconLeftWidget:
                                        icon: "book-open-variant"

            # Экран событий
            MDScreen:
                name: 'events'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: "События"
                        elevation: 0
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: "dodgerblue"
                        specific_text_color: "white"
                    
                    ScrollView:
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: "16dp"
                            spacing: "16dp"
                            adaptive_height: True
                            
                            MDLabel:
                                text: "Актуальные события"
                                bold: True
                                font_style: "H6"
                                adaptive_height: True
                            
                            # Карточка события
                            MDCard:
                                orientation: "vertical"
                                padding: "8dp"
                                size_hint: None, None
                                size: "320dp", "200dp"
                                pos_hint: {"center_x": .5}
                                
                                MDIcon:
                                    icon: "video-vintage"
                                    theme_text_color: "Custom"
                                    text_color: "white"
                                    pos_hint: {"center_x": .5}
                                    font_size: "48sp"
                                
                                MDLabel:
                                    text: "Вебинар 'Карьерные тренды 2022'"
                                    bold: True
                                    adaptive_height: True
                                
                                MDLabel:
                                    text: "15:52 (мск)"
                                    theme_text_color: "Secondary"
                                    adaptive_height: True

            # Экран документов и бланков
            MDScreen:
                name: 'documents'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: "Документы и бланки"
                        elevation: 0
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: "dodgerblue"
                        specific_text_color: "white"
                    
                    ScrollView:
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: "16dp"
                            spacing: "16dp"
                            adaptive_height: True
                            
                            MDList:
                                OneLineIconListItem:
                                    text: "График учебного процесса"
                                    IconLeftWidget:
                                        icon: "calendar-clock"
                                
                                OneLineIconListItem:
                                    text: "Заявления СПО"
                                    IconLeftWidget:
                                        icon: "file-document"
                                
                                OneLineIconListItem:
                                    text: "Приказ об увеличении стоимости обучения"
                                    IconLeftWidget:
                                        icon: "file-document"
                                
                                OneLineIconListItem:
                                    text: "Заявление на предоставление"
                                    IconLeftWidget:
                                        icon: "file-document"

            # Экран заказа справки
            MDScreen:
                name: 'certificate'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: "Заказать справку"
                        elevation: 0
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: "dodgerblue"
                        specific_text_color: "white"
                    
                    ScrollView:
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: "16dp"
                            spacing: "16dp"
                            adaptive_height: True
                            
                            MDLabel:
                                text: "Выберите тип справки"
                                bold: True
                                font_style: "H6"
                                adaptive_height: True
                            
                            MDList:
                                OneLineIconListItem:
                                    text: "Справка об обучении"
                                    IconLeftWidget:
                                        icon: "certificate"
                                
                                OneLineIconListItem:
                                    text: "Справка о стипендии"
                                    IconLeftWidget:
                                        icon: "cash"
                                
                                OneLineIconListItem:
                                    text: "Справка для военкомата"
                                    IconLeftWidget:
                                        icon: "shield"

            # Экран настроек
            MDScreen:
                name: 'settings'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: "Настройки"
                        elevation: 0
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: "dodgerblue"
                        specific_text_color: "white"
                    
                    ScrollView:
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: "16dp"
                            spacing: "16dp"
                            adaptive_height: True
                            
                            MDList:
                                OneLineIconListItem:
                                    text: "Уведомления"
                                    IconLeftWidget:
                                        icon: "bell"
                                
                                OneLineIconListItem:
                                    text: "Тема оформления"
                                    IconLeftWidget:
                                        icon: "palette"
                                
                                OneLineIconListItem:
                                    text: "Язык"
                                    IconLeftWidget:
                                        icon: "translate"
                                
                                OneLineIconListItem:
                                    text: "Конфиденциальность"
                                    IconLeftWidget:
                                        icon: "shield-lock"

            # Экран портфолио
            MDScreen:
                name: 'portfolio'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: "Портфолио"
                        elevation: 0
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: "dodgerblue"
                        specific_text_color: "white"
                    
                    ScrollView:
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: "16dp"
                            spacing: "16dp"
                            adaptive_height: True
                            
                            MDLabel:
                                text: "Мои достижения"
                                bold: True
                                font_style: "H6"
                                adaptive_height: True
                            
                            MDGridLayout:
                                cols: 2
                                spacing: "16dp"
                                adaptive_height: True
                                
                                MDCard:
                                    orientation: "vertical"
                                    padding: "8dp"
                                    size_hint: None, None
                                    size: "160dp", "160dp"
                                    
                                    MDIconButton:
                                        icon: "trophy"
                                        pos_hint: {"center_x": .5}
                                        theme_icon_color: "Custom"
                                        icon_color: "gold"
                                        icon_size: "48sp"
                                    
                                    MDLabel:
                                        text: "Научные работы"
                                        halign: "center"
                                        bold: True
                                    
                                    MDLabel:
                                        text: "3 публикации"
                                        halign: "center"
                                        theme_text_color: "Secondary"
                                
                                MDCard:
                                    orientation: "vertical"
                                    padding: "8dp"
                                    size_hint: None, None
                                    size: "160dp", "160dp"
                                    
                                    MDIconButton:
                                        icon: "medal"
                                        pos_hint: {"center_x": .5}
                                        theme_icon_color: "Custom"
                                        icon_color: "gold"
                                        icon_size: "48sp"
                                    
                                    MDLabel:
                                        text: "Награды"
                                        halign: "center"
                                        bold: True
                                    
                                    MDLabel:
                                        text: "5 наград"
                                        halign: "center"
                                        theme_text_color: "Secondary"

            # Экран электронного дневника
            MDScreen:
                name: 'diary'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: "Электронный дневник"
                        elevation: 0
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: "dodgerblue"
                        specific_text_color: "white"
                    
                    ScrollView:
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: "16dp"
                            spacing: "16dp"
                            adaptive_height: True
                            
                            MDSegmentedControl:
                                MDSegmentedControlItem:
                                    text: "I"
                                MDSegmentedControlItem:
                                    text: "II"
                                MDSegmentedControlItem:
                                    text: "III"
                                MDSegmentedControlItem:
                                    text: "IV"
                            
                            MDBoxLayout:
                                orientation: 'vertical'
                                spacing: "16dp"
                                adaptive_height: True
                                
                                MDTextField:
                                    hint_text: "Студент"
                                    mode: "rectangle"
                                    multiline: False
                                    size_hint_y: None
                                    height: "48dp"
                                
                                MDTextField:
                                    hint_text: "Группа"
                                    mode: "rectangle"
                                    multiline: False
                                    size_hint_y: None
                                    height: "48dp"
                            
                            MDCard:
                                orientation: "vertical"
                                padding: "16dp"
                                spacing: "8dp"
                                size_hint_y: None
                                height: "120dp"
                                
                                MDLabel:
                                    text: "Комментарий"
                                    theme_text_color: "Secondary"
                                    size_hint_y: None
                                    height: "24dp"
                                
                                MDLabel:
                                    text: "Руб. Атт."
                                    theme_text_color: "Secondary"
                                    size_hint_y: None
                                    height: "24dp"
                                
                                MDLabel:
                                    text: "Ит. оценка"
                                    theme_text_color: "Secondary"
                                    size_hint_y: None
                                    height: "24dp"
                            
                            MDBoxLayout:
                                adaptive_height: True
                                spacing: "16dp"
                                
                                MDFlatButton:
                                    text: "Детализация"
                                    md_bg_color: "darkorange"
                                    text_color: "white"
                                    size_hint_x: 0.5
                                
                                MDFlatButton:
                                    text: "Расписание"
                                    md_bg_color: "darkorange"
                                    text_color: "white"
                                    size_hint_x: 0.5

            # Экран доски объявлений
            MDScreen:
                name: 'announcements'
                
                MDBoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: "Доска объявлений"
                        elevation: 0
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: "dodgerblue"
                        specific_text_color: "white"
                    
                    ScrollView:
                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: "16dp"
                            spacing: "16dp"
                            adaptive_height: True
                            
                            MDLabel:
                                text: "Важные объявления"
                                bold: True
                                font_style: "H6"
                                adaptive_height: True
                            
                            MDList:
                                OneLineIconListItem:
                                    text: "Изменение в расписании"
                                    IconLeftWidget:
                                        icon: "calendar-alert"
                                
                                OneLineIconListItem:
                                    text: "Новый учебный материал"
                                    IconLeftWidget:
                                        icon: "book-plus"
                                
                                OneLineIconListItem:
                                    text: "Важная информация"
                                    IconLeftWidget:
                                        icon: "information"

        # Боковое меню
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)
            width: "320dp"
            
            MDBoxLayout:
                orientation: 'vertical'
                padding: "16dp"
                spacing: "12dp"
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "Главная страница"
                            on_release: 
                                app.switch_screen('main')
                                nav_drawer.set_state("close")
                            font_style: "Subtitle1"
                            _txt_bot_pad: "16dp"
                            _txt_top_pad: "16dp"
                            IconLeftWidget:
                                icon: "view-dashboard"
                                theme_text_color: "Custom"
                                text_color: "dodgerblue"
                                icon_size: "24sp"
                        
                        OneLineIconListItem:
                            text: "Написать преподавателю"
                            on_release: 
                                app.switch_screen('message')
                                nav_drawer.set_state("close")
                            font_style: "Subtitle1"
                            _txt_bot_pad: "16dp"
                            _txt_top_pad: "16dp"
                            IconLeftWidget:
                                icon: "email"
                                theme_text_color: "Custom"
                                text_color: "dodgerblue"
                                icon_size: "24sp"
                        
                        OneLineIconListItem:
                            text: "Доска объявлений"
                            on_release: 
                                app.switch_screen('announcements')
                                nav_drawer.set_state("close")
                            font_style: "Subtitle1"
                            _txt_bot_pad: "16dp"
                            _txt_top_pad: "16dp"
                            IconLeftWidget:
                                icon: "bulletin-board"
                                theme_text_color: "Custom"
                                text_color: "dodgerblue"
                                icon_size: "24sp"
                        
                        OneLineIconListItem:
                            text: "Расписание"
                            on_release: 
                                app.switch_screen('schedule')
                                nav_drawer.set_state("close")
                            font_style: "Subtitle1"
                            _txt_bot_pad: "16dp"
                            _txt_top_pad: "16dp"
                            IconLeftWidget:
                                icon: "calendar"
                                theme_text_color: "Custom"
                                text_color: "dodgerblue"
                                icon_size: "24sp"
                        
                        OneLineIconListItem:
                            text: "Дисциплины"
                            on_release: 
                                app.switch_screen('courses')
                                nav_drawer.set_state("close")
                            font_style: "Subtitle1"
                            _txt_bot_pad: "16dp"
                            _txt_top_pad: "16dp"
                            IconLeftWidget:
                                icon: "school"
                                theme_text_color: "Custom"
                                text_color: "dodgerblue"
                                icon_size: "24sp"
                        
                        OneLineIconListItem:
                            text: "Электронная библиотека"
                            on_release: 
                                app.switch_screen('library')
                                nav_drawer.set_state("close")
                            font_style: "Subtitle1"
                            _txt_bot_pad: "16dp"
                            _txt_top_pad: "16dp"
                            IconLeftWidget:
                                icon: "book-variant"
                                theme_text_color: "Custom"
                                text_color: "dodgerblue"
                                icon_size: "24sp"
                        
                        OneLineIconListItem:
                            text: "Документы и бланки"
                            on_release: 
                                app.switch_screen('documents')
                                nav_drawer.set_state("close")
                            font_style: "Subtitle1"
                            _txt_bot_pad: "16dp"
                            _txt_top_pad: "16dp"
                            IconLeftWidget:
                                icon: "file-document"
                                theme_text_color: "Custom"
                                text_color: "dodgerblue"
                                icon_size: "24sp"
                        
                        OneLineIconListItem:
                            text: "Заказать справку"
                            on_release: 
                                app.switch_screen('certificate')
                                nav_drawer.set_state("close")
                            font_style: "Subtitle1"
                            _txt_bot_pad: "16dp"
                            _txt_top_pad: "16dp"
                            IconLeftWidget:
                                icon: "file-certificate"
                                theme_text_color: "Custom"
                                text_color: "dodgerblue"
                                icon_size: "24sp"
                        
                        OneLineIconListItem:
                            text: "События"
                            on_release: 
                                app.switch_screen('events')
                                nav_drawer.set_state("close")
                            font_style: "Subtitle1"
                            _txt_bot_pad: "16dp"
                            _txt_top_pad: "16dp"
                            IconLeftWidget:
                                icon: "video"
                                theme_text_color: "Custom"
                                text_color: "dodgerblue"
                                icon_size: "24sp"
                        
                        OneLineIconListItem:
                            text: "Электронный дневник"
                            on_release: 
                                app.switch_screen('diary')
                                nav_drawer.set_state("close")
                            font_style: "Subtitle1"
                            _txt_bot_pad: "16dp"
                            _txt_top_pad: "16dp"
                            IconLeftWidget:
                                icon: "notebook"
                                theme_text_color: "Custom"
                                text_color: "dodgerblue"
                                icon_size: "24sp"
                        
                        OneLineIconListItem:
                            text: "Навигатор по InStudy"
                            on_release: 
                                app.switch_screen('navigator')
                                nav_drawer.set_state("close")
                            font_style: "Subtitle1"
                            _txt_bot_pad: "16dp"
                            _txt_top_pad: "16dp"
                            IconLeftWidget:
                                icon: "compass"
                                theme_text_color: "Custom"
                                text_color: "dodgerblue"
                                icon_size: "24sp"
                        
                        OneLineIconListItem:
                            text: "Настройки"
                            on_release: 
                                app.switch_screen('settings')
                                nav_drawer.set_state("close")
                            font_style: "Subtitle1"
                            _txt_bot_pad: "16dp"
                            _txt_top_pad: "16dp"
                            IconLeftWidget:
                                icon: "cog"
                                theme_text_color: "Custom"
                                text_color: "dodgerblue"
                                icon_size: "24sp"
                        
                        OneLineIconListItem:
                            text: "Портфолио"
                            on_release: 
                                app.switch_screen('portfolio')
                                nav_drawer.set_state("close")
                            font_style: "Subtitle1"
                            _txt_bot_pad: "16dp"
                            _txt_top_pad: "16dp"
                            IconLeftWidget:
                                icon: "trophy"
                                theme_text_color: "Custom"
                                text_color: "dodgerblue"
                                icon_size: "24sp"
                        
                        OneLineIconListItem:
                            text: "Зачётная книжка"
                            on_release: 
                                app.switch_screen('gradebook')
                                nav_drawer.set_state("close")
                            font_style: "Subtitle1"
                            _txt_bot_pad: "16dp"
                            _txt_top_pad: "16dp"
                            IconLeftWidget:
                                icon: "book-open"
                                theme_text_color: "Custom"
                                text_color: "dodgerblue"
                                icon_size: "24sp"
                        
                        OneLineIconListItem:
                            text: "Выход"
                            on_release: 
                                app.stop()
                                nav_drawer.set_state("close")
                            font_style: "Subtitle1"
                            _txt_bot_pad: "16dp"
                            _txt_top_pad: "16dp"
                            theme_text_color: "Custom"
                            text_color: "red"
                            IconLeftWidget:
                                icon: "exit-to-app"
                                theme_text_color: "Custom"
                                text_color: "red"
                                icon_size: "24sp"
'''

class InStudyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"
        self.root = Builder.load_string(KV)
        
        # Добавляем нижнее меню на все основные экраны
        screens_with_bottom_nav = [
            'main', 'message', 'schedule', 'notifications', 'profile',
            'courses', 'library', 'gradebook', 'navigator', 'events',
            'documents', 'certificate', 'settings', 'portfolio', 'diary'
        ]
        
        for screen in screens_with_bottom_nav:
            screen_widget = self.root.ids.screen_manager.get_screen(screen)
            bottom_nav = BottomNavigation(current_screen=screen)
            screen_widget.children[0].add_widget(bottom_nav)
        
        return self.root
    
    def on_start(self):
        self.add_activities()
        self.add_articles()
        self.add_schedule()
        self.add_courses()
        self.add_library_items()
        self.add_grades()
        self.add_notifications()
    
    def switch_screen(self, screen_name):
        # Получаем текущий и новый экран
        current_screen = self.root.ids.screen_manager.get_screen(self.root.ids.screen_manager.current)
        new_screen = self.root.ids.screen_manager.get_screen(screen_name)
        
        # Обновляем цвета иконок в нижнем меню на обоих экранах
        for screen in [current_screen, new_screen]:
            if hasattr(screen.children[0], 'children'):
                for child in screen.children[0].children:
                    if isinstance(child, BottomNavigation):
                        for box in child.children:
                            if isinstance(box, MDBoxLayout) and box.children:
                                btn = box.children[0]
                                if isinstance(btn, MDIconButton):
                                    btn.icon_color = "darkorange" if screen_name == btn._screen_name else "grey"
        
        # Переключаем экран
        self.root.ids.screen_manager.current = screen_name
    
    def add_activities(self):
        activities = [
            {"icon": "bell", "text": "Напоминание", "secondary_text": "Экзамен через 3 дня"},
            {"icon": "check-circle", "text": "Задание сдано", "secondary_text": "История России"}
        ]
        
        activity_list = self.root.ids.activity_list
        for activity in activities:
            item = TwoLineIconListItem(
                text=activity["text"],
                secondary_text=activity["secondary_text"]
            )
            icon = IconLeftWidget(
                icon=activity["icon"]
            )
            item.add_widget(icon)
            activity_list.add_widget(item)
    
    def add_articles(self):
        articles = [
            {"text": "Эффективные методы изучения", "secondary_text": "5 мин чтения"},
            {"text": "Подготовка к экзаменам: стратегия успеха", "secondary_text": "7 мин чтения"}
        ]
        
        articles_list = self.root.ids.articles_list
        for article in articles:
            item = TwoLineIconListItem(
                text=article["text"],
                secondary_text=article["secondary_text"]
            )
            icon = IconLeftWidget(
                icon="file-document"
            )
            item.add_widget(icon)
            articles_list.add_widget(item)
    
    def add_schedule(self):
        schedule = [
            {
                "subject": "Математический анализ",
                "type": "Лекция",
                "time": "9:00-10:30",
                "room": "Ауд. 205",
                "teacher": "Иванов И.И."
            },
            {
                "subject": "Физика",
                "type": "Практика",
                "time": "10:45-12:15",
                "room": "Ауд. 314",
                "teacher": "Петрова А.В."
            },
            {
                "subject": "История России",
                "type": "Лекция",
                "time": "13:00-14:30",
                "room": "Ауд. 102",
                "teacher": "Сидоров П.П."
            },
            {
                "subject": "Английский язык",
                "type": "Практика",
                "time": "14:45-16:15",
                "room": "Ауд. 408",
                "teacher": "Смирнова О.К."
            }
        ]
        
        schedule_list = self.root.ids.schedule_list
        for lesson in schedule:
            item = TwoLineIconListItem(
                text=f"{lesson['time']} - {lesson['subject']}",
                secondary_text=f"{lesson['room']}, {lesson['teacher']}"
            )
            icon = IconLeftWidget(
                icon="clock"
            )
            item.add_widget(icon)
            schedule_list.add_widget(item)
    
    def add_courses(self):
        courses = [
            {
                "subject": "Математический анализ",
                "progress": "75%",
                "hours": "90/120 часов",
                "status": "Активно"
            },
            {
                "subject": "Физика",
                "progress": "60%",
                "hours": "60/100 часов",
                "status": "Активно"
            },
            {
                "subject": "История России",
                "progress": "100%",
                "hours": "80/80 часов",
                "status": "Завершено"
            },
            {
                "subject": "Английский язык",
                "progress": "45%",
                "hours": "45/100 часов",
                "status": "Активно"
            }
        ]
        
        courses_list = self.root.ids.courses_list
        for course in courses:
            item = TwoLineIconListItem(
                text=course["subject"],
                secondary_text=f"{course['hours']} • {course['progress']}"
            )
            icon = IconLeftWidget(
                icon="book"
            )
            item.add_widget(icon)
            courses_list.add_widget(item)

    def add_library_items(self):
        items = [
            {
                "title": "Математический анализ, Том 1",
                "author": "Фихтенгольц Г.М.",
                "type": "Книга",
                "size": "12.5 МБ",
                "downloads": "1254"
            },
            {
                "title": "Лекция: Основы квантовой физики",
                "author": "Петрова А.В.",
                "type": "Видео",
                "size": "245 МБ",
                "downloads": "342"
            },
            {
                "title": "История России XIX века",
                "author": "Соловьёв С.М.",
                "type": "Аудио",
                "size": "89 МБ",
                "downloads": "567"
            }
        ]
        
        library_list = self.root.ids.library_list
        for item in items:
            list_item = TwoLineIconListItem(
                text=item["title"],
                secondary_text=f"{item['author']} • {item['size']}"
            )
            icon = IconLeftWidget(
                icon="book" if item["type"] == "Книга" else "video" if item["type"] == "Видео" else "headphones"
            )
            list_item.add_widget(icon)
            library_list.add_widget(list_item)

    def add_grades(self):
        grades = [
            {
                "subject": "Математический анализ",
                "grade": "4.5",
                "credits": "6",
                "exams": [
                    {"type": "Экзамен", "grade": "5/5", "date": "15 янв. 2025 г."},
                    {"type": "Тест", "grade": "4/5", "date": "10 февр. 2025 г."}
                ]
            },
            {
                "subject": "Физика",
                "grade": "4.5",
                "credits": "5",
                "exams": [
                    {"type": "Экзамен", "grade": "4/5", "date": "20 янв. 2025 г."},
                    {"type": "Задание", "grade": "5/5", "date": "15 февр. 2025 г."}
                ]
            },
            {
                "subject": "История России",
                "grade": "5.0",
                "credits": "4",
                "exams": [
                    {"type": "Экзамен", "grade": "5/5", "date": "25 янв. 2025 г."}
                ]
            }
        ]
        
        grades_list = self.root.ids.grades_list
        for grade in grades:
            item = TwoLineIconListItem(
                text=f"{grade['subject']} ★",
                secondary_text=f"Средний балл: {grade['grade']}  Кредитов: {grade['credits']}"
            )
            icon = IconLeftWidget(
                icon="star"
            )
            item.add_widget(icon)
            grades_list.add_widget(item)

    def add_notifications(self):
        notifications = [
            {
                "title": "Новое задание",
                "description": "Добавлено новое задание по Математическому анализу",
                "time": "1 час назад",
                "icon": "book"
            },
            {
                "title": "Изменение в расписании",
                "description": "Лекция по Физике перенесена на 14:30",
                "time": "2 часа назад",
                "icon": "calendar-clock"
            },
            {
                "title": "Результаты теста",
                "description": "Доступны результаты теста по Истории России",
                "time": "3 часа назад",
                "icon": "clipboard-check"
            }
        ]
        
        notifications_list = self.root.ids.notifications_list
        for notification in notifications:
            item = TwoLineIconListItem(
                text=notification["title"],
                secondary_text=f"{notification['description']} • {notification['time']}"
            )
            icon = IconLeftWidget(
                icon=notification["icon"]
            )
            item.add_widget(icon)
            notifications_list.add_widget(item)

if __name__ == '__main__':
    InStudyApp().run() 
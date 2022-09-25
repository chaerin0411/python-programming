# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 20:35:51 2021

@author: chaerin
"""
# os.path.basename 사용
import os
# 기본적인 위젯 Frame, Text, Menu 등 사용
from tkinter import *
# 파일 열기, 다른 이름으로 저장, 메시지 박스 등 대화상자 사용
from tkinter import filedialog, messagebox

class TextEditor():
    '''텍스트 편집기'''
    def __init__(self, root):
        self.root = root
        self.root.title('Tkinter 기본 편집기')
        
        frame = Frame(root)
        frame.pack(fill="both", expand=1)
        
        # 기본 편집을 지원하는 위젯 Text 생성
        self.editor = Text(frame, wrap='word')
        self.editor.pack(side="left", fill="both", expand=1)
        self.editor.focus()
        # 메뉴 생성
        self.make_menu()
    
    def make_menu(self):
        # 메뉴의 최상위인 메뉴바 생성
        self.menubar = Menu(root)
        
        # 메뉴 아이템 File
        fmenu = Menu(self.menubar, tearoff = 0) # tearoff = 0 윈도에 분리되지 않도록
        fmenu.add_command(label="New")
        fmenu.add_command(label="Open...")
        fmenu.add_command(label="Save")
        fmenu.add_command(label="Save As...")
        fmenu.add_separator()
        fmenu.add_command(label="Exit")
        # 메뉴바에 File을 추가
        self.menubar.add_cascade(label="File", menu=fmenu)
        
        # 메뉴 보이기
        root.config(menu=self.menubar)

root = Tk()
root.geometry('800x600')
editor = TextEditor(root)
root.mainloop()
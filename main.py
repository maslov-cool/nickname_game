import io
import sys
import random

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>516</width>
    <height>421</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
    <horstretch>0</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="windowTitle">
   <string>Псевдоним. Возвращение</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="sizePolicy">
    <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
     <horstretch>0</horstretch>
     <verstretch>0</verstretch>
    </sizepolicy>
   </property>
   <widget class="QWidget" name="gridLayoutWidget_3">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>511</width>
      <height>391</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout_3">
     <item row="0" column="0">
      <layout class="QGridLayout" name="gridLayout">
       <item row="0" column="0">
        <widget class="QLabel" name="label">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="text">
          <string>Задать количество камней</string>
         </property>
        </widget>
       </item>
       <item row="0" column="1">
        <widget class="QSpinBox" name="stones">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="minimumSize">
          <size>
           <width>0</width>
           <height>50</height>
          </size>
         </property>
        </widget>
       </item>
       <item row="0" column="2">
        <widget class="QPushButton" name="startButton">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="text">
          <string>Задать</string>
         </property>
        </widget>
       </item>
       <item row="1" column="0" colspan="3">
        <widget class="QLCDNumber" name="remainLcd">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="minimumSize">
          <size>
           <width>0</width>
           <height>50</height>
          </size>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item row="1" column="0">
      <layout class="QGridLayout" name="gridLayout_2">
       <item row="0" column="0">
        <widget class="QLabel" name="label_2">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="minimumSize">
          <size>
           <width>0</width>
           <height>50</height>
          </size>
         </property>
         <property name="text">
          <string>Сколько камней взять?</string>
         </property>
        </widget>
       </item>
       <item row="0" column="1">
        <widget class="QLineEdit" name="takeInput">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
        </widget>
       </item>
       <item row="2" column="0" colspan="2">
        <widget class="QListWidget" name="listWidget"/>
       </item>
       <item row="1" column="0" colspan="2">
        <widget class="QPushButton" name="takeButton">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="minimumSize">
          <size>
           <width>0</width>
           <height>50</height>
          </size>
         </property>
         <property name="text">
          <string>Взять</string>
         </property>
        </widget>
       </item>
       <item row="3" column="0" colspan="2">
        <widget class="QLabel" name="resultLabel">
         <property name="sizePolicy">
          <sizepolicy hsizetype="Expanding" vsizetype="Expanding">
           <horstretch>0</horstretch>
           <verstretch>0</verstretch>
          </sizepolicy>
         </property>
         <property name="minimumSize">
          <size>
           <width>0</width>
           <height>50</height>
          </size>
         </property>
         <property name="text">
          <string/>
         </property>
         <property name="alignment">
          <set>Qt::AlignCenter</set>
         </property>
        </widget>
       </item>
      </layout>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>516</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>

"""


class Pseudonym(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.startButton.clicked.connect(self.f1)
        self.takeButton.clicked.connect(self.f2)

    def f1(self):
        self.takeButton.setEnabled(True)
        self.resultLabel.setText('')
        self.listWidget.clear()
        self.stones_quality = self.stones.value()
        self.remainLcd.display(self.stones_quality)

    def f2(self):
        n = int(self.takeInput.text())
        if 1 <= n <= 3 and n <= self.stones_quality:
            self.stones_quality -= n
            self.listWidget.addItem('Игрок взял - ' + self.takeInput.text())

            if not self.stones_quality:
                self.resultLabel.setText('Победа пользователя!')
                self.remainLcd.display(0)
                self.takeButton.setEnabled(False)
            else:
                self.remainLcd.display(self.stones_quality)

            if self.stones_quality:
                n1 = random.randint(1, min(3, self.stones_quality))
                self.stones_quality -= n1
                self.listWidget.addItem('Компьютер взял - ' + str(n1))

                if not self.stones_quality:
                    self.resultLabel.setText('Победа компьютера!')
                    self.remainLcd.display(0)
                    self.takeButton.setEnabled(False)
                else:
                    self.remainLcd.display(self.stones_quality)
        else:
            self.resultLabel.setText('Невозможно взять столько')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pseudonym()
    ex.show()
    sys.exit(app.exec())


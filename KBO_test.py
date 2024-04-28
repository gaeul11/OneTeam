import traceback
import sys
import os

import layout
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget, QListView
from PyQt5.QtCore import pyqtSlot

# UI 파일 로드
root = os.path.dirname(os.path.abspath(__file__))
ui_path = os.path.join(root, 'kbo.ui')
class KboApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_path, self)  # UI 로드
        self.setWindowTitle("kbo")  # 창 제목 설정

        # tab 버튼 연결
        if hasattr(self, 'kbo_tabWidget'):
            self.kbo_tabWidget.currentChanged.connect(self.on_tab_changed)

        # # dayChedule_List 이름의 QListView가 이미 생성된 경우
        # layout.addWidget(self.dayChedule_List)  # 레이아웃에 위젯 추가
    @pyqtSlot(int)  # 탭 인덱스 파라미터를 받음
    def on_tab_changed(self, index):
        print(f"Tab changed to index: {index}")  # 탭 인덱스를 출력
        # index == 0 : 순위 탭
        # index == 1 : 선수정보 탭
        # index == 2 : 일정 탭 
        try:
            if index == 0:
               self.rankTab()
        except Exception as e:
             print(e)

        if index == 1:
            print("hello  선수정보 tab")
        if index == 2:
            print("hello  일정 tab")

    #rank tab에 들어갈 내용이 담길 함수
    def rankTab(self):
        print("test rank")


# 애플리케이션 실행
if __name__ == '__main__':
    app = QApplication(sys.argv)
    kbo = KboApp()
    kbo.show()
    sys.exit(app.exec_())
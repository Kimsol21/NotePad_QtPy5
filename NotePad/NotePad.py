import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtGui import QTextCursor

# Qt Designer를 통해 만든 ui파일 불러와서 form_class라는 변수에 저장.
form_class = uic.loadUiType("X:\\PyQT_Tutorial\\NotePad\\NotePad.ui")[0]

class findWindow(QDialog):
    
    # 생성자 함수
    def __init__(self, parent):
        super(findWindow, self).__init__(parent)
        uic.loadUi("X:\\PyQT_Tutorial\\NotePad\\find.ui", self)
        self.show() #창 보여주기
        
        self.parent = parent
        self.cursor = self.parent.plainTextEdit.textCursor() # 부모클래스에 접근해 커서 받아오기
        self.plainTxtEdit = parent.plainTextEdit #부모클래스에 접근해 plainText 받아오기.
        
        # 버튼과 함수 연결해주기.
        self.pushButton_findnext.clicked.connect(self.findNext) 
        self.pushButton_cancle.clicked.connect(self.close) 
        
        self.radioButton_down.clicked.connect(self.updown_radio_button)
        self.radioButton_up.clicked.connect(self.updown_radio_button)
        self.up_down = "down"
        
     
    # 라디오 버튼 함수
    def updown_radio_button(self):
        if self.radioButton_up.isChecked():
            self.up_down = "up"
        elif self.radioButton_down.isChecked():
            self.up_down = "down"           
        
     
   
    # 키보드 이벤트 함수(기본 지원, close와 비슷)
    def keyReleaseEvent(self, event):
        if self.lineEdit.text(): # lineEdit 안에 text가 있을 때만 
            self.pushButton_findnext.setEnabled(True) # 다음찾기 버튼 활성화 시켜주기.
        else:
            self.pushButton_findnext.setEnabled(False)
            
    
    # 다음 찾기 함수    
    def findNext(self):
        pattern = self.lineEdit.text() # 찾아야 할 TEXT를 pattern에 저장.
        text = self.plainTxtEdit.toPlainText() # plainTEXT를 text에 저장.     
        reg = QtCore.QRegExp(pattern) # 정규 표현식 설정 (ex : 010-1234-1234 -> 010 \d{4} - \d{4})
        self.cursor = self.parent.plainTextEdit.textCursor() # 부모클래스에 접근해 커서 받아오기     
        
        if self.checkBox_CaseSensitive.isChecked(): # 대소문자 구분이 켜져있으면
            cs = QtCore.Qt.CaseSensitive # 대소문자 구분 설정을 cs에 저장.
        else:
            cs = QtCore.Qt.CaseInsensitive     
        
        reg.setCaseSensitivity(cs) #reg에 대소문자 구분 설정을 set해주기. 
        pos = self.cursor.position() #현재 커서위치 받아오기.
        
        if self.up_down == "down": # 정방향 검색이라면 그냥 검색 실행.
            index = reg.indexIn(text, pos) # 검색한 후 결과 index를 반환.
        else: # 역방향 검색이라면 lastIndexIn 함수 사용.
            pos -= len(pattern)+1 #아래의 setCursor함수에서 커서를 뒤로 움직이기때문에 역방향이라면 패턴의 길이+1만큼 빼줘야함.
            index = reg.lastIndexIn(text, pos)          
        
        
        if (index != -1) and (pos>-1): # 검색된 결과가 있다면
            self.setCursor(index, len(pattern)+index) #결과 길이만큼 커서set해주기.
        else:
            self.notFoundMessage(pattern)
        
    # 커서 설정 함수
    def setCursor(self, start, end):
        print(self.cursor.selectionStart(), self.cursor.selectionEnd())
        
        self.cursor.setPosition(start) # 앞에 커서를 찍고
        self.cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, end-start) # 뒤로 커서를 움직임.
        self.plainTxtEdit.setTextCursor(self.cursor) # 실제로 plainText에 반영.
    
    
    # "찾을 수 없습니다." 메시지박스 설정 및 띄우는 함수.
    def notFoundMessage(self, pattern):
        messageBox = QMessageBox() # QTPy에서 제공해주는 메시지박스.
        messageBox.setWindowTitle('메모장')
        messageBox.setIcon(QMessageBox.Information)
        messageBox.setText('''"{}"을(를) 찾을 수 없습니다.'''.format(pattern))
        messageBox.addButton('확인', QMessageBox.YesRole)
        
        ret = messageBox.exec_() # 실행

 
class WindowClass(QMainWindow, form_class):
    
    # 생성자 함수
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Designer를 통해 만든 ui와 그것을 클릭했을 때 동작시켜줄 함수 연결.
        
        #파일
        self.action_open.triggered.connect(self.openFunction) #열기 
        self.action_save.triggered.connect(self.saveFunction) #저장
        self.action_saveAs.triggered.connect(self.saveAsFunction) #다른이름으로 저장   
        self.action_close.triggered.connect(self.close) #닫기     
        
        #편집
        self.action_undo.triggered.connect(self.undoFunction) #실행취소
        self.action_cut.triggered.connect(self.cutFunction) #잘라내기
        self.action_copy.triggered.connect(self.copyFunction) #복사
        self.action_paste.triggered.connect(self.pasteFunction) #붙여넣기
        
        self.action_find.triggered.connect(self.findFunction) #찾기
           
        # class 내에서 쓰일 변수 선언 및 초기화
        self.opened = False
        self.openedFilePath = '제목 없음'       
    
    
    # 현재 데이터와 저장된 데이터를 비교해 바뀐내용이 있는지 검사하는 함수.
    def ischanged(self):
        if not self.opened: # 오픈된적이 없을 때.
            if self.plainTextEdit.toPlainText().strip(): #공백문자 제외하고 데이터가 있을 시 True.
                return True
            return False
        
        # 현재 데이터
        current_data = self.plainTextEdit.toPlainText() 
        # 파일에 저장된 데이터
        with open(self.openedFilePath, encoding = 'UTF8') as f:
            file_data = f.read() 
             
        if current_data == file_data: # 열린적이 있고 변경사항이 없으면 False반환.
            return False
        else: # 열린적이 있고 변경사항이 있으면 True반환.
            return True
            
    
    # 저장 메시지박스 설정 및 띄우는 함수.
    def generateSaveMessageBox(self):
        messageBox = QMessageBox() # QTPy에서 제공해주는 메시지박스.
        
        messageBox.setText("변경 내용을 {}에 저장하시겠습니까?".format(self.openedFilePath))
        messageBox.addButton('저장', QMessageBox.YesRole) # 0
        messageBox.addButton('저장 안 함', QMessageBox.NoRole) # 1
        messageBox.addButton('취소', QMessageBox.RejectRole) # 2
        
        ret = messageBox.exec_() # 실행
        
        if ret == 0:
            self.saveFunction()
        else:
            return ret
        
    
    
    # 끝내기 함수
    def closeEvent(self, event): 
        if self.ischanged(): # 열린적이 있고 변경사항이 있으면 or 열린적은 없는데 에디터 내용이 있으면
            ret = self.generateSaveMessageBox() #저장하시겠습니까 띄우기
            
            # 열린적은 없는데 에디터 내용이 있으면 
            if ret == 2: # 취소 버튼 눌렀으면 close이벤트 ignore시켜주기.
                event.ignore()
            
   
    # 파일 저장 함수
    def save_file(self, fname):
        data = self.plainTextEdit.toPlainText() # PlainText에 있는 내용 가져와 data에 저장. 
            
        with open(fname, 'w', encoding = 'UTF8') as f:
            f.write(data) # fname경로에 있는 파일을 UTF-8로 인코딩해서 불러온 후 data를 write해줌.       
            
        self.opened = True # 파일이 오픈되었음을 저장.
        self.openedFilePath = fname # 오픈된 파일의 경로를 저장.   
            
        print("'{}'경로에 파일을 저장했습니다.".format(fname[0]))   
        
    
    # 파일 읽어오는 함수
    def open_file(self, fname):
        with open(fname, encoding = 'UTF8') as f:
            data = f.read() # fname경로에 있는 파일을 UTF-8로 인코딩해서 불러온 후 data에 저장.
        self.plainTextEdit.setPlainText(data) # Text 인풋 영역에 set시켜줌.
            
        self.opened = True # 파일이 오픈되었음을 저장.
        self.openedFilePath = fname # 오픈된 파일의 경로를 저장.
            
        print("'{}'경로에 있는 파일을 열었습니다.".format(fname))
    
    
    #"열기" 로직 함수    
    def openFunction(self): 
        
        #열기할때 저장안된 파일이 그냥 날라가는 것을 막기위한 로직.
        if self.ischanged(): # 열린적이 있고 변경사항이 있으면 or 열린적은 없는데 에디터 내용이 있으면 
            ret = self.generateSaveMessageBox() #저장하시겠습니까 띄우기.
        
        fname = QFileDialog.getOpenFileName(self) # 파일탐색기 띄워서 선택된 파일 경로 반환. fname에 저장시켜주기. 
        if fname[0]:
            self.open_file(fname[0])
        
    
    #"저장" 로직 함수    
    def saveFunction(self): 
        if self.opened: #오픈되어있는 경우 탐색기 띄우지 않고 바로 저장.
            self.save_file(self.openedFilePath)
        else: #오픈이 안된경우 다른이름으로 저장과 같은 로직.
            self.saveAsFunction()
            
    
    #"다른이름으로 저장" 로직 함수    
    def saveAsFunction(self): 
        fname = QFileDialog.getSaveFileName(self) # 파일탐색기 띄워서 선택된 파일 경로 반환. fname에 저장시켜주기. 
        if fname[0]:
            self.save_file(fname[0])
            
            
    # 실행취소 함수            
    def undoFunction(self):
        self.plainTextEdit.undo()
    
    
    # 잘라내기 함수        
    def cutFunction(self):
        self.plainTextEdit.cut()
        
    
    # 복사하기 함수    
    def copyFunction(self):
        self.plainTextEdit.copy()
        
        
    # 붙여넣기 함수    
    def pasteFunction(self):
        self.plainTextEdit.paste() 
        
        
    # 찾기 함수
    def findFunction(self):
        findWindow(self)
                
        
app = QApplication(sys.argv) # QApplication을 실행할 수 있는 app 생성. 
mainWindow = WindowClass()
mainWindow.show()
app.exec_() # mainWindow와 ui(form_class)를 연결해 app 실행.
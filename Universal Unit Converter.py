#All imports
import converter_engine
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton, QComboBox, QLineEdit
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt

#All Entity Units List
EntityUnits = ['','Distance', 'Weight', 'Volume', 'Time', "Temperature"]
DistanceUnits = ['','Millimeter', 'Centimeter', 'Meter', 'Kilometer', 'Feet', 'Inch', 'Yard', 'Mile']
WeightUnits = ['','Kilogram', 'Gram', 'Milligram', 'Ton', 'Pound']
VolumeUnits = ['','Gallon', 'Quart', 'Pint', 'Cup', 'Ounce']
TimeUnits = ['','Seconds', 'Minutes', 'Hour', 'Day', 'Month', 'Year']
TemperatureUnits = ['','Kelvin', 'Fahrenheit', 'Celsius']
A = 0
B = 0
C = 0

#Colors for User Interface
Navy = "#102937"
LightBlue = "#D7E5F0"

for x in DistanceUnits:
    StrFL = "FL"
    StrSL = "SL"
    StrTL = "TL"
    IntFL = A = A + 1
    IntSL = B = B + 1
    IntTL = C = C + 1
    InputFL = (StrFL + str(IntFL))
    InputSL = (StrSL + str(IntSL))
    InputTL = (StrTL + str(IntTL))

#Code to launch Main Window
app = QApplication(sys.argv)
MainWindow = QWidget()
MainWindow.setWindowTitle("Unit Converter")
MainWindow.setGeometry(300,300,300,300)
MainWindow.setFixedWidth(300)
MainWindow.setFixedHeight(360)
MainWindow.setStyleSheet("background-color: Black")

#Code for Label
TOMLabel = QtWidgets.QLabel(MainWindow)
TOMLabel.setText("Unit Converter")
TOMLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
TOMLabel.setFixedWidth(310)
TOMLabel.setFixedHeight(40)
TOMLabel.move(-5,10)
TOMLabel.setWordWrap(True)
TOMLabel.setStyleSheet(f"background-color: {Navy}; border-color: Black; border-style: outset; border-width: 1px")

#Code for Box1 (Big White One)
Box1 = QtWidgets.QLabel(MainWindow)
Box1.setGeometry(285, 285, 275, 285)
Box1.move(10,60)
Box1.setStyleSheet("background-color: White; border-color: #b0b0b5; border-style: outset; border-width: 2px; border-radius: 7.5px")

#Code for Box2 (Bottom One)
Box2 = QtWidgets.QLabel(MainWindow)
Box2.setGeometry(100, 100, 262, 100)
Box2.move(15,235)
Box2.setStyleSheet(f"background-color: {Navy}; border-radius: 7.5px")

#Code for Box3 (Middle One)
Box3 = QtWidgets.QLabel(MainWindow)
Box3.setGeometry(100, 100, 262, 100)
Box3.move(15,130)
Box3.setStyleSheet(f"background-color: {Navy}; border-radius: 7.5px")

#Code for Box3 (Top One)
Box3 = QtWidgets.QLabel(MainWindow)
Box3.setGeometry(100, 100, 262, 60)
Box3.move(15,65)
Box3.setStyleSheet(f"background-color: {Navy}; border-radius: 7.5px")

#Code for Entity Drop Down List
EntityDropDownList = QComboBox(MainWindow)
EntityDropDownList.addItems(EntityUnits)
EntityDropDownList.setAccessibleName("Entity Units")
EntityDropDownList.setFont(QFont("Calibri", 15))
EntityDropDownList.setStyleSheet(f"background-color: {LightBlue}; color: black; border-radius: 5px; border-style: Outset;border-color: Black; border-width: 1.4")
EntityDropDownList.setGeometry(40,40,140,40)
EntityDropDownList.move(20,75)

#Code for Convert Button
ConvertButton = QPushButton(MainWindow)
ConvertButton.setFont(QFont("Calibri", 15))
ConvertButton.setStyleSheet("background-color: LightGreen; border-color: Black; border-style: outset; border-width: 1.4px; border-radius: 7.5px; padding: 4px")
ConvertButton.setText("Convert")
ConvertButton.setGeometry(40,40,100,40)
ConvertButton.move(170,75)

#Code for Unit1 Drop Down List
Unit1DropDownList = QComboBox(MainWindow)
Unit1DropDownList.setFont(QFont("Calibri", 15))
Unit1DropDownList.setStyleSheet(f"background-color: {LightBlue}; color: black; border-radius: 5px; border-style: Outset;border-color: Black; border-width: 1.4")
Unit1DropDownList.setGeometry(40,40,215,40)
Unit1DropDownList.move(20,140)

#Code for Unit2 Drop Down List
Unit2DropDownList = QComboBox(MainWindow)
Unit2DropDownList.setFont(QFont("Calibri", 15))
Unit2DropDownList.setStyleSheet(f"background-color: {LightBlue}; color: black; border-radius: 5px; border-style: Outset;border-color: Black; border-width: 1.4")
Unit2DropDownList.setGeometry(40,40,215,40)
Unit2DropDownList.move(20,185)

# Code for Swap button
SwapButton = QPushButton(MainWindow)
SwapButton.setIcon(QIcon("C:/Advait/Code/Python/Python Icons/swap-vertical.svg"))
SwapButton.setStyleSheet("background-color: white; border-radius: 15px;")
SwapButton.setGeometry(240, 166, 30, 30)
SwapButton.setIconSize(SwapButton.size() * 0.7)

#Code for Input Text Boxes
InputTextBox = QLineEdit(MainWindow)
InputTextBox.setFont(QFont("Calibri", 12))
InputTextBox.setStyleSheet("background-color: white; color: black; border-radius: 5px; border-style: Outset; border-color: Black; border-width: 1px")
InputTextBox.setGeometry(40, 30, 240, 30)
InputTextBox.move(25, 245)
InputTextBox.setPlaceholderText("Enter value here...")

#Code for Output Text Boxes
OutputTextBox = QLineEdit(MainWindow)
OutputTextBox.setFont(QFont("Calibri", 12))
OutputTextBox.setStyleSheet("background-color: #e8e8e8; color: black; border-radius: 5px; border-style: Outset; border-color: Black; border-width: 1px")
OutputTextBox.setGeometry(40, 30, 240, 30)
OutputTextBox.move(25, 290)
OutputTextBox.setReadOnly(True)

def DropDownListChanging(text):
    #Clear previous units so they don't stack up
    Unit1DropDownList.clear()
    Unit2DropDownList.clear()    
    #add options in both dropdowns based on the selected category
    if text == 'Distance':
        Unit1DropDownList.addItems(DistanceUnits)
        Unit2DropDownList.addItems(DistanceUnits)
    elif text == 'Weight':
        Unit1DropDownList.addItems(WeightUnits)
        Unit2DropDownList.addItems(WeightUnits)
    elif text == 'Volume':
        Unit1DropDownList.addItems(VolumeUnits)
        Unit2DropDownList.addItems(VolumeUnits)
    elif text == 'Time':
        Unit1DropDownList.addItems(TimeUnits)
        Unit2DropDownList.addItems(TimeUnits)
    elif text == 'Temperature':
        Unit1DropDownList.addItems(TemperatureUnits)
        Unit2DropDownList.addItems(TemperatureUnits)

def perform_conversion():
    try:
        #Gather values from your UI components
        input_val = float(InputTextBox.text())
        category = EntityDropDownList.currentText()
        unit_from = Unit1DropDownList.currentText()
        unit_to = Unit2DropDownList.currentText()

        #Delegate the math to your imported engine
        if category == 'Temperature':
            final_value = converter_engine.calculate_temperature(input_val, unit_from, unit_to)
        else:
            final_value = converter_engine.calculate_standard(
                input_val, category, unit_from, unit_to, converter_engine.ConversionFactors
            )

        #Update the UI with the result
        OutputTextBox.setText(f"{final_value:.4f}")
        
    except ValueError:
        OutputTextBox.setText("Error: Enter a number")
    except KeyError:
        OutputTextBox.setText("Error: Selection Mismatch")

def swap_dropdowns():
    idx1 = Unit1DropDownList.currentIndex()
    idx2 = Unit2DropDownList.currentIndex()
    
    #Swap the selected indices
    Unit1DropDownList.setCurrentIndex(idx2)
    Unit2DropDownList.setCurrentIndex(idx1)

#Signals that call the functions when the user interacts with the GUI
EntityDropDownList.currentTextChanged.connect(DropDownListChanging)
ConvertButton.clicked.connect(perform_conversion)
SwapButton.clicked.connect(swap_dropdowns)

MainWindow.show()
sys.exit(app.exec())
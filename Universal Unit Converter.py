#All imports
import converter_engine
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QComboBox, QLineEdit, QVBoxLayout, QHBoxLayout
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
TOMLabel.setFont(QFont("Calibri", 15))
TOMLabel.setText("Unit Converter")
TOMLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
TOMLabel.setFixedWidth(310)
TOMLabel.setFixedHeight(40)
TOMLabel.move(-5,10)
TOMLabel.setWordWrap(True)
TOMLabel.setStyleSheet(f"background-color: {Navy}; color: white; border-color: Black; border-radius: 5px;border-style: outset; border-width: 1px")

#Code for Entity Drop Down List
EntityDropDownList = QComboBox(MainWindow)
EntityDropDownList.addItems(EntityUnits)
EntityDropDownList.setAccessibleName("Entity Units")
EntityDropDownList.setFont(QFont("Calibri", 15))
EntityDropDownList.setStyleSheet(f"background-color: {LightBlue}; color: black; border-radius: 5px; border-style: Outset;border-color: Black; border-width: 1.4")
EntityDropDownList.setFixedSize(145, 45)
EntityDropDownList.move(20,75)

#Code for Convert Button
ConvertButton = QPushButton(MainWindow)
ConvertButton.setFont(QFont("Calibri", 15))
ConvertButton.setStyleSheet("background-color: LightGreen; border-color: Black; border-style: outset; border-width: 1.4px; border-radius: 7.5px; padding: 4px")
ConvertButton.setText("Convert")
ConvertButton.setFixedSize(100, 45)
ConvertButton.move(170,75)

#Code for Unit1 Drop Down List
Unit1DropDownList = QComboBox(MainWindow)
Unit1DropDownList.setFont(QFont("Calibri", 15))
Unit1DropDownList.setStyleSheet(f"background-color: {LightBlue}; color: black; border-radius: 5px; border-style: Outset;border-color: Black; border-width: 1.4")
Unit1DropDownList.setFixedSize(230, 45)
Unit1DropDownList.move(20,140)

#Code for Unit2 Drop Down List
Unit2DropDownList = QComboBox(MainWindow)
Unit2DropDownList.setFont(QFont("Calibri", 15))
Unit2DropDownList.setStyleSheet(f"background-color: {LightBlue}; color: black; border-radius: 5px; border-style: Outset;border-color: Black; border-width: 1.4")
Unit2DropDownList.setFixedSize(230, 45)
Unit2DropDownList.move(20,185)

# Code for Swap button
SwapButton = QPushButton(MainWindow)
SwapButton.setIcon(QIcon("C:/Advait/Code/Python/Python Icons/swap-vertical.svg"))
SwapButton.setStyleSheet("background-color: white; border-radius: 17px;")
SwapButton.setFixedSize(35, 35)
SwapButton.setIconSize(SwapButton.size() * 0.7)

#Code for Input Text Boxes
InputTextBox = QLineEdit(MainWindow)
InputTextBox.setFont(QFont("Calibri", 12))
InputTextBox.setStyleSheet("background-color: white; color: black; border-radius: 5px; border-style: Outset; border-color: Black; border-width: 1px")
InputTextBox.setFixedSize(278, 45)
InputTextBox.move(25, 245)
InputTextBox.setPlaceholderText("Enter value here...")

#Code for Output Text Boxes
OutputTextBox = QLineEdit(MainWindow)
OutputTextBox.setFont(QFont("Calibri", 12))
OutputTextBox.setStyleSheet("background-color: #e8e8e8; color: black; border-radius: 5px; border-style: Outset; border-color: Black; border-width: 1px")
OutputTextBox.setFixedSize(278, 45)
OutputTextBox.move(25, 290)
OutputTextBox.setReadOnly(True)

# ==========================================
# RESPONSIVE LAYOUT SYSTEM (FIXED TO MATCH ORIGINAL)
# ==========================================

# 1. Create the structural containers
main_layout = QVBoxLayout()
main_layout.setContentsMargins(15, 15, 15, 15)

# The big white card container
white_card = QWidget()
white_card.setStyleSheet("background-color: white; border: 2px solid #b0b0b5; border-radius: 7.5px;")
card_layout = QVBoxLayout(white_card)
card_layout.setContentsMargins(6, 6, 6, 6)
card_layout.setSpacing(5)

# TOP PANEL (Category & Convert Button)
top_container = QWidget()
top_container.setStyleSheet(f"background-color: {Navy}; border-radius: 7.5px;")
top_layout = QHBoxLayout(top_container)
top_layout.setContentsMargins(10, 10, 10, 10)

# MIDDLE PANEL (The Dropdowns + Swap Button side-by-side)
middle_container = QWidget()
middle_container.setStyleSheet(f"background-color: {Navy}; border-radius: 7.5px;")
middle_container_layout = QHBoxLayout(middle_container)
middle_container_layout.setContentsMargins(10, 10, 10, 10)

# Inside the middle panel, we need a vertical column for the two dropdowns
dropdown_column_layout = QVBoxLayout()
dropdown_column_layout.setSpacing(10)

# BOTTOM PANEL (The Input & Output text boxes)
bottom_container = QWidget()
bottom_container.setStyleSheet(f"background-color: {Navy}; border-radius: 7.5px;")
bottom_layout = QVBoxLayout(bottom_container)
bottom_layout.setContentsMargins(10, 10, 10, 10)
bottom_layout.setSpacing(10)


# 2. Arrange your components into the layouts

# Top Row Setup
top_layout.addWidget(EntityDropDownList)
top_layout.addWidget(ConvertButton)
card_layout.addWidget(top_container, 1)

# Middle Row Setup (Dropdowns stacked vertically, Swap button on the right)
dropdown_column_layout.addWidget(Unit1DropDownList)
dropdown_column_layout.addWidget(Unit2DropDownList)

middle_container_layout.addLayout(dropdown_column_layout)
middle_container_layout.addWidget(SwapButton, alignment=Qt.AlignmentFlag.AlignCenter)
card_layout.addWidget(middle_container, 2)

# Bottom Row Setup (Text fields stacked vertically)
bottom_layout.addWidget(InputTextBox)
bottom_layout.addWidget(OutputTextBox)
card_layout.addWidget(bottom_container, 2)


# 3. Mount everything to the main window
main_layout.addWidget(TOMLabel)
main_layout.addWidget(white_card)
MainWindow.setLayout(main_layout)

# Set the window size rules to look like your original screenshot
MainWindow.resize(380, 480)
MainWindow.setMinimumSize(340, 440)

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
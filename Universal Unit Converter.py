# ==========================================
# 1. IMPORTS
# ==========================================
import sys
import converter_engine
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (QApplication, QStackedWidget, QWidget, QPushButton, 
                             QLabel, QComboBox, QLineEdit, QVBoxLayout, QHBoxLayout)
from PyQt6.QtGui import QFont, QDoubleValidator, QIcon
from PyQt6.QtCore import QSize, Qt

# ==========================================
# 2. DATA & CONFIGURATIONS
# ==========================================
# All Entity Units Lists (Updated)
EntityUnits = ['', 'Distance', 'Weight', 'Volume', 'Time', 'Temperature', 'Currency']
DistanceUnits = ['', 'Millimeter', 'Centimeter', 'Meter', 'Kilometer', 'Feet', 'Inch', 'Yard', 'Mile']
WeightUnits = ['', 'Kilogram', 'Gram', 'Milligram', 'Ton', 'Pound']
VolumeUnits = ['', 'Gallon', 'Quart', 'Pint', 'Cup', 'Ounce']
TimeUnits = ['', 'Seconds', 'Minutes', 'Hour', 'Day', 'Month', 'Year']
TemperatureUnits = ['', 'Kelvin', 'Fahrenheit', 'Celsius']
CurrencyUnits = ['', 'USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'INR', 'CNY', 'MXN']

# Dictionary map for quick dropdown population (Updated)
UNIT_MAP = {
    'Distance': DistanceUnits,
    'Weight': WeightUnits,
    'Volume': VolumeUnits,
    'Time': TimeUnits,
    'Temperature': TemperatureUnits,
    'Currency': CurrencyUnits
}
# History tracker
conversion_history = []

# Theme Dictionaries
DARK_THEME = {
    "window_bg": "#121212",       # Deep black/gray window
    "card_bg": "#1e1e1e",         # Dark grey inner card
    "panel_bg": "#2c3e50",        # Dark navy panels
    "input_bg": "#ffffff",        # White input field
    "text": "#000000",            # Black text inside input
    "border": "#ffffff",          # White border for input fields
    "history_bg": "#ee6c4d",      # Dark navy background for history panel
}

LIGHT_THEME = {
    "window_bg": "#f5f6fa",       # Clean light gray window
    "card_bg": "#ffffff",         # Pure white inner card
    "panel_bg": "#ee6c4d",        # Light gray panels
    "input_bg": "#ffffff",        # White input field
    "text": "#000000",            # Black text inside input
    "border": "#000000",          # Black border for input fields
    "history_bg": "#4B5C9A"       # Light gray background for history panel
}

current_theme = DARK_THEME

# ==========================================
# 3. APP & MAIN WINDOW SETUP
# ==========================================
app = QApplication(sys.argv)

MainWindow = QWidget()
MainWindow.setWindowTitle("Unit Converter")
MainWindow.setGeometry(300, 300, 300, 300)
MainWindow.setFixedWidth(300)
MainWindow.setFixedHeight(360)
MainWindow.setStyleSheet(f"background-color: {current_theme['window_bg']};")
MainWindow.resize(380, 480)
MainWindow.setMinimumSize(340, 440)

# Main layout that holds everything
main_layout = QVBoxLayout()
main_layout.setContentsMargins(15, 15, 15, 15)

# The White Card (Container for all central UI)
white_card = QWidget()
white_card.setStyleSheet(f"background-color: {current_theme['card_bg']}; border: 2px solid #b0b0b5; border-radius: 7.5px;")
card_layout = QVBoxLayout(white_card)

# ==========================================
# 4. WIDGET CREATION
# ==========================================
# Top Title Label
TOMLabel = QtWidgets.QLabel("Unit Converter")
TOMLabel.setFont(QFont("Calibri", 15))
TOMLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
TOMLabel.setFixedWidth(310)
TOMLabel.setFixedHeight(40)
TOMLabel.setWordWrap(True)
TOMLabel.setStyleSheet(f"background-color: {current_theme['panel_bg']}; color: {current_theme['text']}; border-color: {current_theme['border']}; border-radius: 5px;border-style: outset; border-width: 1.5px")

# Shared Stylesheet for Dropdowns
dropdown_style = f"background-color: {current_theme['input_bg']}; color: {current_theme['text']}; border-radius: 5px; border-style: Outset;border-color: {current_theme['border']}; border-width: 1.5"

EntityDropDownList = QComboBox()
EntityDropDownList.addItems(EntityUnits)
EntityDropDownList.setFont(QFont("Calibri", 15))
EntityDropDownList.setStyleSheet(dropdown_style)
EntityDropDownList.setFixedSize(135, 45)

Unit1DropDownList = QComboBox()
Unit1DropDownList.setFont(QFont("Calibri", 15))
Unit1DropDownList.setStyleSheet(dropdown_style)
Unit1DropDownList.setFixedSize(220, 45)

Unit2DropDownList = QComboBox()
Unit2DropDownList.setFont(QFont("Calibri", 15))
Unit2DropDownList.setStyleSheet(dropdown_style)
Unit2DropDownList.setFixedSize(220, 45)

# Shared Stylesheet for Text Inputs
input_style = f"background-color: {current_theme['input_bg']}; color: {current_theme['text']}; border-radius: 5px; border-style: Outset; border-color: {current_theme['border']}; border-width: 1.5px"

validator = QDoubleValidator()
validator.setNotation(QDoubleValidator.Notation.StandardNotation)

InputTextBox = QLineEdit()
InputTextBox.setValidator(validator)
InputTextBox.setFont(QFont("Calibri", 12))
InputTextBox.setStyleSheet(input_style)
InputTextBox.setFixedSize(220, 45)
InputTextBox.setPlaceholderText("Enter value here...")

OutputTextBox = QLineEdit()
OutputTextBox.setFont(QFont("Calibri", 12))
OutputTextBox.setStyleSheet(input_style)
OutputTextBox.setFixedSize(220, 45)
OutputTextBox.setReadOnly(True)

# Buttons
btn_style_standard = "QPushButton {background-color: white; border-radius: 17px;}QPushButton:hover {background-color: #D0D5CE;}"
btn_style_history = f"QPushButton {{background-color: {current_theme['history_bg']}; border-radius: 17px;}}QPushButton:hover {{background-color: #D0D5CE;}}"

HistoryButton = QPushButton()
HistoryButton.setIcon(QIcon("Portfolio Projects/Univeral Unit Converter/Icons/history-svgrepo-com.svg"))
HistoryButton.setIconSize(QSize(30, 30))
HistoryButton.setStyleSheet(btn_style_history)
HistoryButton.setFixedSize(70, 45)

ConverterThemeButton = QPushButton()
ConverterThemeButton.setIcon(QIcon("Portfolio Projects/Univeral Unit Converter/Icons/sun-svgrepo-com.svg"))
ConverterThemeButton.setIconSize(QSize(25, 25))
ConverterThemeButton.setStyleSheet(btn_style_standard)
ConverterThemeButton.setFixedSize(35, 35)

SwapButton = QPushButton()
SwapButton.setIcon(QIcon("Portfolio Projects/Univeral Unit Converter/Icons/swap-vertical.svg"))
SwapButton.setIconSize(QSize(25, 25))
SwapButton.setStyleSheet(btn_style_standard)
SwapButton.setFixedSize(35, 35)

AddButton = QPushButton()
AddButton.setIcon(QIcon("Portfolio Projects/Univeral Unit Converter/Icons/plus-svgrepo-com.svg"))
AddButton.setIconSize(QSize(30, 30))
AddButton.setStyleSheet(btn_style_history)
AddButton.setFixedSize(35, 80)

# ==========================================
# 5. LAYOUT & STACK MANAGEMENT
# ==========================================
page_stack = QStackedWidget()

# --- PAGE 1: CONVERTER SCREEN ---
converter_page = QWidget()
converter_page.setStyleSheet("background-color: transparent; border: none; border-radius: 7.5px;")
converter_layout = QVBoxLayout(converter_page)
converter_layout.setContentsMargins(10, 10, 10, 10)

# Top Panel
top_container = QWidget()
top_container.setStyleSheet(f"background-color: {current_theme['panel_bg']}; border-radius: 7.5px;")
top_layout = QHBoxLayout(top_container)
top_layout.setContentsMargins(10, 10, 10, 10)
top_layout.addWidget(EntityDropDownList)
top_layout.addWidget(HistoryButton)
top_layout.addWidget(ConverterThemeButton)

# Middle Panel
middle_container = QWidget()
middle_container.setStyleSheet(f"background-color: {current_theme['panel_bg']}; border-radius: 7.5px;")
middle_container_layout = QHBoxLayout(middle_container)
middle_container_layout.setContentsMargins(10, 10, 10, 10)
dropdown_column_layout = QVBoxLayout()
dropdown_column_layout.setSpacing(10)
dropdown_column_layout.addWidget(Unit1DropDownList)
dropdown_column_layout.addWidget(Unit2DropDownList)
middle_container_layout.addLayout(dropdown_column_layout)
middle_container_layout.addWidget(SwapButton, alignment=Qt.AlignmentFlag.AlignCenter)

# Bottom Panel
bottom_container = QWidget()
bottom_container.setStyleSheet(f"background-color: {current_theme['panel_bg']}; border-radius: 7.5px;")
bottom_container_layout = QHBoxLayout(bottom_container)
bottom_container_layout.setContentsMargins(10, 10, 10, 10)
dropdown_column_layout2 = QVBoxLayout()
dropdown_column_layout2.setSpacing(10)
dropdown_column_layout2.addWidget(InputTextBox)
dropdown_column_layout2.addWidget(OutputTextBox)
bottom_container_layout.addLayout(dropdown_column_layout2)
bottom_container_layout.addWidget(AddButton, alignment=Qt.AlignmentFlag.AlignCenter)

# Assemble Page 1
converter_layout.addWidget(top_container)
converter_layout.addWidget(middle_container, 2)
converter_layout.addWidget(bottom_container, 2)

# --- PAGE 2: HISTORY SCREEN ---
history_page = QWidget()
history_page_layout = QVBoxLayout(history_page)

HistoryTitle = QLabel("Conversion History")
HistoryTitle.setStyleSheet("font-weight: bold; font-size: 16px; color: black; border: none;")

ConverterButton = QPushButton()
ConverterButton.setIcon(QIcon("Portfolio Projects/Univeral Unit Converter/Icons/calculator-svgrepo-com.svg"))
ConverterButton.setIconSize(QSize(30, 30))
ConverterButton.setStyleSheet(f"QPushButton {{background-color: {current_theme['history_bg']}; border: none; border-radius: 17px;}}QPushButton:hover {{background-color: #D0D5CE;}}")
ConverterButton.setFixedSize(70, 45)

HistoryThemeButton = QPushButton()
HistoryThemeButton.setIcon(QIcon("Portfolio Projects/Univeral Unit Converter/Icons/sun-svgrepo-com.svg"))
HistoryThemeButton.setIconSize(QSize(25, 25))
HistoryThemeButton.setStyleSheet("QPushButton {background-color: white; border: none; border-radius: 17px;}QPushButton:hover {background-color: #D0D5CE;}")
HistoryThemeButton.setFixedSize(35, 35)

history_container = QWidget()
history_container.setStyleSheet("background-color: white; border-radius: 7.5px;")
history_layout = QHBoxLayout(history_container)
history_layout.setContentsMargins(10, 10, 10, 10)
history_layout.addWidget(HistoryTitle)
history_layout.addWidget(ConverterButton)
history_layout.addWidget(HistoryThemeButton)

HistoryLogDisplay = QLabel("No history logged yet.")
HistoryLogDisplay.setStyleSheet(f"font-size: 14px; background-color: {current_theme['panel_bg']}; border: 1px solid {current_theme['border']}; padding: 15px; border-radius: 6px;")

history_page_layout.addWidget(history_container)
history_page_layout.addWidget(HistoryLogDisplay, 1)

# --- ASSEMBLE THE STACK ---
page_stack.addWidget(converter_page) # Index 0
page_stack.addWidget(history_page)   # Index 1

# Strip margins and background from the white_card wrapper completely
white_card.setStyleSheet(f"background-color: {current_theme['card_bg']}; border: 2px solid {current_theme['border']}; border-radius: 7.5px;")
card_layout.setContentsMargins(0, 0, 0, 0)
card_layout.addWidget(page_stack)

# Mount to main window
main_layout.addWidget(TOMLabel)
main_layout.addWidget(white_card)
MainWindow.setLayout(main_layout)

# ==========================================
# 6. APP FUNCTIONS (LOGIC)
# ==========================================
def DropDownListChanging(text):
    """Updates unit dropdowns based on the selected category via dictionary mapping"""
    Unit1DropDownList.clear()
    Unit2DropDownList.clear()
    
    if text in UNIT_MAP:
        Unit1DropDownList.addItems(UNIT_MAP[text])
        Unit2DropDownList.addItems(UNIT_MAP[text])

def perform_conversion():
    try:
        input_val = float(InputTextBox.text())
        category = EntityDropDownList.currentText()
        unit_from = Unit1DropDownList.currentText()
        unit_to = Unit2DropDownList.currentText()

        if category == 'Temperature':
            final_value = converter_engine.calculate_temperature(input_val, unit_from, unit_to)
        elif category == 'Currency':
            final_value = converter_engine.calculate_currency(input_val, unit_from, unit_to)
            
            # Catch network errors safely if internet is down
            if final_value == "NETWORK_ERROR":
                OutputTextBox.setText("Error: No Connection")
                return
        else:
            final_value = converter_engine.calculate_standard(
                input_val, category, unit_from, unit_to, converter_engine.ConversionFactors
            )
            
        if final_value is not None:
            OutputTextBox.setText(f"{final_value:.4f}")
        else:
            OutputTextBox.setText("")        
    except ValueError:
        OutputTextBox.setText("Error: Selection Mismatch")
    except KeyError:
        OutputTextBox.setText("Error: Selection Mismatch")

def swap_dropdowns():
    idx1 = Unit1DropDownList.currentIndex()
    idx2 = Unit2DropDownList.currentIndex()
    Unit1DropDownList.setCurrentIndex(idx2)
    Unit2DropDownList.setCurrentIndex(idx1)

def toggle_theme(theme_button, *args):
    global current_theme 
    
    if current_theme == DARK_THEME:
        current_theme = LIGHT_THEME
        theme_button.setIcon(QIcon("Portfolio Projects/Univeral Unit Converter/Icons/moon-svgrepo-com.svg"))
    else:
        current_theme = DARK_THEME
        theme_button.setIcon(QIcon("Portfolio Projects/Univeral Unit Converter/Icons/sun-svgrepo-com.svg"))
        
    MainWindow.setStyleSheet(f"background-color: {current_theme['window_bg']};")
    
    # Update styling across app elements dynamically
    white_card.setStyleSheet(f"background-color: {current_theme['card_bg']}; border: 2px solid {current_theme['border']}; border-radius: 7.5px;")
    converter_page.setStyleSheet("background-color: transparent; border: none; border-radius: 7.5px;")
    history_page.setStyleSheet("background-color: transparent; border: none; border-radius: 7.5px;")
    
    top_container.setStyleSheet(f"background-color: {current_theme['panel_bg']}; border: none; border-radius: 7.5px;")
    middle_container.setStyleSheet(f"background-color: {current_theme['panel_bg']}; border: none; border-radius: 7.5px;")
    bottom_container.setStyleSheet(f"background-color: {current_theme['panel_bg']}; border: none; border-radius: 7.5px;")
    
    TOMLabel.setStyleSheet(f"background-color: {current_theme['panel_bg']}; color: {current_theme['text']}; padding: 10px; border-radius: 5px; border-style: outset; border-width: 1.5px; border-color: {current_theme['border']};")
    
    btn_update_style = f"QPushButton {{background-color: {current_theme['history_bg']}; border-radius: 17px;}}QPushButton:hover {{background-color: #D0D5CE;}}"
    HistoryButton.setStyleSheet(btn_update_style)
    ConverterButton.setStyleSheet(btn_update_style)
    AddButton.setStyleSheet(btn_update_style)

def save_to_history():
    input_val = InputTextBox.text()
    output_val = OutputTextBox.text()
    u1 = Unit1DropDownList.currentText()
    u2 = Unit2DropDownList.currentText()

    if input_val: 
        history_entry = f"{input_val} {u1} ➔ {output_val} {u2}"
        if not conversion_history or conversion_history[0] != history_entry:
            conversion_history.insert(0, history_entry)
            if len(conversion_history) > 12:
                conversion_history.pop()
            HistoryLogDisplay.setText("\n".join(conversion_history))

def toggle_page_view():
    current_page = page_stack.currentIndex()
    if current_page == 0:
        page_stack.setCurrentIndex(1)
        HistoryButton.setIcon(QIcon("Portfolio Projects/Univeral Unit Converter/Icons/history-svgrepo-com.svg"))
        HistoryTitle.setStyleSheet("font-weight: bold; font-size: 16px; color: black; border: none;")
        HistoryLogDisplay.setStyleSheet("font-size: 14px; background-color: #f8f9fa; color: black; padding: 15px; border-radius: 6px;")
    else:
        page_stack.setCurrentIndex(0)
        HistoryButton.setIcon(QIcon("Portfolio Projects/Univeral Unit Converter/Icons/calculator-svgrepo-com.svg"))

# ==========================================
# 7. SIGNALS & EXECUTION
# ==========================================
# Wiring up dropdowns and text changes
EntityDropDownList.currentTextChanged.connect(DropDownListChanging)
InputTextBox.textChanged.connect(perform_conversion)
Unit1DropDownList.currentIndexChanged.connect(perform_conversion)
Unit2DropDownList.currentIndexChanged.connect(perform_conversion)
EntityDropDownList.currentIndexChanged.connect(perform_conversion)

# Wiring up buttons
SwapButton.clicked.connect(swap_dropdowns)
HistoryThemeButton.clicked.connect(lambda: toggle_theme(HistoryThemeButton))
ConverterThemeButton.clicked.connect(lambda: toggle_theme(ConverterThemeButton))
AddButton.clicked.connect(save_to_history)
HistoryButton.clicked.connect(toggle_page_view)
ConverterButton.clicked.connect(toggle_page_view)

# Run the app
MainWindow.show()
sys.exit(app.exec())
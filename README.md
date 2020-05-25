# Overview
This is a heart monitor application using stm32f103c8 microcontroller and AD8232 integrated signal conditioning block for ECG. The project is split into an embedded application written in C language to be downloaded on the MCU, and a python application to communicate with the MCU over a serial link.

# Python Application
## Libraries used
-   **PyQt5**
Used to design the whole GUI. QT Designer was used to design the UI elements visually, then Pyuic5 utility was used to convert the design to a Python class.
    

-   **Matplotlib**
 There is no built-in components in PyQt to add the graph to the GUI. There is an external library, QtCharts, that is compatible with PyQt, but it doesn’t support real-time updating. So Matplotlib was used for the graph.
    

-   **Pyserial**
Used for sending and receiving data between the application and the embedded application over the serial link.

## Graphical User Interface
![GUI](/Documentation/GUI.png)

## Code Structure
![Code Structure](/Documentation/Class%20Diagram.png)

## General Comments
- The GUI is designed for an average user who is not experienced with communication or embedded software:
  - The UI elements are categorized by function into groups for easier user experience.
  - The UI elements contain the default values for communication, with automatic **port detection**.
  - Label text elements are added to report any error in the data validation to the user.
- OOP principles were used to separate the UI creation and logic from the main application.


# Message Encryption/Decryption GUI

## Overview
This project implements a simple graphical user interface (GUI) for encrypting and decrypting messages using a Caesar cipher. The GUI is built using the Tkinter library in Python.

## Components

### 1. Encryption and Decryption Functions
The `encrypt_message` and `decrypt_message` functions perform the Caesar cipher encryption and decryption on the input message based on the selected key.

### 2. Process Message Function
The `process_message` function reads the input message, selected operation (Encrypt or Decrypt), and key from the GUI. It then processes the message accordingly and updates the output text area.

### 3. GUI Elements
- **Input Text Area:** Allows users to input the message for encryption or decryption.
- **Operation Selection Dropdown:** Enables users to choose between encryption and decryption.
- **Key Entry:** Accepts the key for encryption or decryption.
- **Process Button:** Triggers the processing of the message based on the selected operation and key.
- **Output Text Area:** Displays the result of the encryption or decryption.

## Usage
1. **Install Python:**
   - Ensure you have Python installed on your system.

2. **Run the GUI:**
   - Execute the provided code in a Python environment.
   - A window will appear with input and output areas.

3. **Input Message:**
   - Enter the message in the "Input Message" text area.

4. **Select Operation:**
   - Choose between "Encrypt" and "Decrypt" from the dropdown.

5. **Enter Key:**
   - Input the key in the "Key" entry.

6. **Process Message:**
   - Click the "Process" button to perform the encryption or decryption.

7. **Review Output:**
   - The processed message will be displayed in the "Output Message" text area.

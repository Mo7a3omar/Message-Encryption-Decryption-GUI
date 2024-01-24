import tkinter as tk

def process_message():
    message = input_text.get("1.0", tk.END).strip()
    operation = selection.get()
    key = int(key_entry.get())

    if operation == "Encrypt":
        processed_message = encrypt_message(message, key)
    elif operation == "Decrypt":
        processed_message = decrypt_message(message, key)
    else:
        processed_message = "Invalid operation selected."
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, processed_message)

def encrypt_message(message, key):
    encrypted_message = ""
    
    for char in message:
        if char.isalpha():
            char_code = ord(char)
            shifted_code = (char_code + key) % 26  
            encrypted_char = chr(shifted_code + ord('A'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    
    return encrypted_message

def decrypt_message(message, key):
    decrypted_message = ""
    
    for char in message:
        if char.isalpha():
            char_code = ord(char)
            shifted_code = (char_code - key) % 26 
            decrypted_char = chr(shifted_code + ord('A'))
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    
    return decrypted_message

# GUI window
window = tk.Tk()
window.title("Message Encryption/Decryption")
window.geometry("400x400")
window.configure(background="#333333") 

#input label
input_label = tk.Label(window, text="Input Message:", fg="#ffffff", font=("Arial", 12), bg="#333333")
input_label.pack(pady=10)
input_text = tk.Text(window, height=5, width=30, font=("Arial", 10))
input_text.pack()

#selection label
selection_label = tk.Label(window, text="Select Operation:", fg="#ffffff", font=("Arial", 12), bg="#333333")
selection_label.pack(pady=10)
selection = tk.StringVar(window)
selection.set("Encrypt") 
selection_dropdown = tk.OptionMenu(window, selection, "Encrypt", "Decrypt")
selection_dropdown.config(font=("Arial", 10), bg="#cccccc", width=10)
selection_dropdown.pack()

#key label
key_label = tk.Label(window, text="Key:", fg="#ffffff", font=("Arial", 12), bg="#333333")
key_label.pack(pady=10)
key_entry = tk.Entry(window, width=10, font=("Arial", 10))
key_entry.pack()

#process button
process_button = tk.Button(window, text="Process", command=process_message, font=("Arial", 12), bg="#b3e6cc", fg="#333333")
process_button.pack(pady=20)

#outputlabel
output_label = tk.Label(window, text="Output Message:", fg="#ffffff", font=("Arial", 12), bg="#333333")
output_label.pack()
output_text = tk.Text(window, height=5, width=30, font=("Arial", 10))
output_text.pack()

window.mainloop()

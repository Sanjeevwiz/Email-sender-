import smtplib
import tkinter as tk
from tkinter import messagebox
from threading import Thread

# Function to send the email
def send_email(smtp_server, port, sender_email, sender_password, recipient_email, subject, body):
    try:
        # Establish connection to the SMTP server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Upgrade the connection to secure
        server.login(sender_email, sender_password)

        # Construct the email
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        server.sendmail(sender_email, recipient_email, message)
        server.quit()
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")

# Function to trigger the email sending process in a new thread
def send_email_thread():
    sender_email = entry_sender_email.get()
    sender_password = entry_sender_password.get()
    recipient_email = entry_recipient_email.get()
    subject = entry_subject.get()
    body = text_body.get("1.0", "end-1c")
    
    # Validate inputs
    if not sender_email or not sender_password or not recipient_email or not subject or not body:
        messagebox.showerror("Input Error", "Please fill all the fields.")
        return

    # SMTP server and port for Gmail (you can change this for other providers)
    smtp_server = "smtp.gmail.com"
    port = 587  # For TLS

    # Start sending email in a new thread to keep the GUI responsive
    thread = Thread(target=send_email, args=(smtp_server, port, sender_email, sender_password, recipient_email, subject, body))
    thread.start()

# Set up the GUI
root = tk.Tk()
root.title("Email Sender")

# Create and place widgets
tk.Label(root, text="Sender Email:").grid(row=0, column=0, padx=10, pady=5)
entry_sender_email = tk.Entry(root, width=40)
entry_sender_email.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Sender Password:").grid(row=1, column=0, padx=10, pady=5)
entry_sender_password = tk.Entry(root, width=40, show="*")
entry_sender_password.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Recipient Email:").grid(row=2, column=0, padx=10, pady=5)
entry_recipient_email = tk.Entry(root, width=40)
entry_recipient_email.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Subject:").grid(row=3, column=0, padx=10, pady=5)
entry_subject = tk.Entry(root, width=40)
entry_subject.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Body:").grid(row=4, column=0, padx=10, pady=5)
text_body = tk.Text(root, width=40, height=10)
text_body.grid(row=4, column=1, padx=10, pady=5)

# Button to send the email
send_button = tk.Button(root, text="Send Email", command=send_email_thread)
send_button.grid(row=5, column=1, padx=10, pady=10)

# Run the GUI
root.mainloop()
import tkinter as tk
from actual_main import run_program

# Create the main window
root = tk.Tk()
root.title("Input Window")
root.geometry("400x400")
root.config(bg="green")
root.title("Farmers Only")

# Create an Entry widget for user input
label=tk.Label(root, text="Enter your address")
label.place(relx=0.5,rely=0.4,anchor="center")
entry = tk.Entry(root, width=30)
entry.place(relx=0.5,rely=0.5,anchor="center")

def submit_button_clicked():
    user_input=entry.get()
    print(user_input)
    main=run_program()
    final_list=main.start_game(user_input)
    for widget in root.winfo_children():
        widget.destroy()
    text_box = tk.Text(root, width=40, height=10)
    text_box.place(relx=0.5,rely=0.5,anchor="center")
    label2=tk.Label(root, text="Crops that are best suited for you :")
    label2.place(relx=0.5,rely=0.2,anchor="center")
    count=1
    for item in final_list:
        text_box.insert(tk.END, str(count)+". "+str(item.seed_name)+": $"+str(round(item.profit,3)) + '\n')
        count=count+1

label=tk.Label(root, text="Enter how much you are willing to pay per acre (in dollars)")
label.place(relx=0.5,rely=0.6,anchor="center")
entry2 = tk.Entry(root, width=30)
entry2.place(relx=0.5,rely=0.7,anchor="center")

# Create a Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_button_clicked)
submit_button.place(relx=0.5,rely=0.9,anchor="center")

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

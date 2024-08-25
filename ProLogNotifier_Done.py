import tkinter as tk 
from tkinter import messagebox 
from PIL import Image, ImageTk 
import os 
import time 
import psutil 
import smtplib 
import schedule 
import threading 
from email import encoders 
from email. mime. text import MIMEText 
from email. mime. base import MIMEBase 
from email. mime. multipart import MIMEMultipart 
import urllib. error 
import urllib. request 

def main(): 
    def is_connected(): 
        try: 
            urllib. request. urlopen('http://www. gmail. com') 
            return True 
        except urllib. error. URLError as err: 
            return False 

    def MailSender(filename,timestamp,sender,app_password,receiver): 
        try: 
            msg = MIMEMultipart() 
            msg['From'] = sender 
            msg['To'] = receiver 

            body = f""" 
            Hello {receiver}, 
            Welcome to Our RCPIT Company! 

            Here are the details: 
            - Log file created at: {timestamp}. 
            - Document: Process Log 

            Best regards, 

            Paresh Bharat Patil 
            Shirpur, Dhule 
            """ 
            subject = f"RCPIT Process log generated at : {timestamp}"
            msg ['Subject'] = subject 
            msg. attach(MIMEText(body,'plain')) 

            with open(filename,"rb") as attachment: 
                p = MIMEBase('application','octet-stream') 
                p. set_payload(attachment. read()) 
                encoders. encode_base64(p) 
                p. add_header('Content-Disposition', f"attachment; filename= {os. path. basename(filename)}") 
                msg. attach(p) 

            s = smtplib. SMTP('smtp. gmail. com', 587) 
            s. starttls() 
            s. login(sender, app_password) 
            text = msg. as_string() 
            s. sendmail(sender, receiver, text) 
            s. quit() 

            print("Log file successfully sent through Mail") 
        except Exception as e: 
            print("Unable to send mail ", e)

    def ProcessLog(log_dir='RCPIT',sender='',app_password='',receiver=''): 
        listprocess = [] 
        if not os. path. exists(log_dir): 
            try: 
                os. mkdir(log_dir) 
            except Exception as e: 
                print("Unable to create directory:",e) 
                return 
 
        separator = "" * 80 
        timestamp = time. strftime("%Y%m%d-%H%M%S") 
        log_path = os. path. join(log_dir,f"RCPITLog_{timestamp}. log") 
        with open(log_path, 'w') as f:
            f. write(separator + "\n") 
            f. write("RCPIT Process Logger : Logging: " + str(time. ctime()))
            f. write(separator + "\n") 
            f. write("\n") 
 
            for proc in psutil. process_iter(): 
                try: 
                    pinfo = proc. as_dict(attrs=['pid', 'name', 'username']) 
                    vms = proc. memory_info(). vms/(1024 * 1024) 
                    pinfo['vms'] = vms 
                    listprocess.append(pinfo) 
                except (psutil. NoSuchProcess,psutil. AccessDenied,psutil. ZombieProcess): 
                    pass 
            for element in listprocess: 
                f. write("%s\n" % element) 
        print ("The log file is successfully generated at location " + str(log_path)) 
            
        if is_connected(): 
            start_time = time. time() 
            MailSender(log_path,time. ctime(),sender,app_password,receiver) 
            end_time = time. time() 
            print ('Took %s seconds to send mail' % (end_time - start_time))
        else: 
            print("There is no internet connection")
 
    def start_logging(): 
        global sender,app_password,receiver,interval 
        sender = entry_sender. get() 
        app_password = entry_password. get() 
        receiver = entry_receiver. get() 
        try: 
            interval = int(entry_interval. get()) 
        except ValueError: 
            messagebox. showerror("Invalid input", "You have to provided a valid integer for interval. ") 
            return 
        
        if not all([sender,app_password,receiver,interval]): 
            messagebox. showerror("Missing input”, “It is mandatory to fill all the spaces. ") 
            return 
        schedule.every(interval).minutes.do(ProcessLog,sender=sender,app_password=app_password,receiver=receiver) 
        
        def run_schedule(): 
            while running: 
                schedule. run_pending() 
                time. sleep(1) 
            
                global schedule_thread 
                schedule_thread = threading. Thread(target=run_schedule) 
                schedule_thread. start() 
                print("Started logging processes. ") 
 
    def stop_logging(): 
        global running 
        running = False 
        schedule_thread. join() 
        print("Stopped logging processes. ") 
    
    font_style = ("Times New Roman", 12, "bold") 
    
    app = tk. Tk() 
    app. title("ProLogNotifier") 
    app. geometry("1560x1200") 
    
    bg_image_path = r"C:\Users\patil\OneDrive\Desktop\Placement\GitHub Repos\ProLogNotifier\upload.jpg" 
    bg_image = Image. open(bg_image_path) 
    bg_image = bg_image. resize((1560, 900), Image. Resampling. LANCZOS) 
    bg_image_tk = ImageTk. PhotoImage(bg_image) 
    
    canvas = tk. Canvas(app,width=1560,height=800) 
    canvas. pack(fill=tk. BOTH,expand=True) 
    
    canvas. create_image(0,0,image=bg_image_tk,anchor=tk. NW) 
    
    frame_main = tk. Frame(app,bg='lightpink',padx=20,pady=20) 
    frame_main. place(relx=0.5,rely=0.5,anchor=tk. CENTER) 
    
    label_bg_color = 'lightpink' 
    entry_bg_color = 'lightgrey' 
    
    font_style = ("Times New Roman", 12, "bold") 
    
    tk. Label(frame_main,text="Sender Mail-Id  : ",bg=label_bg_color,font=font_style). grid(row=0,column=0,sticky='w',pady=5) 
    entry_sender = tk. Entry(frame_main,width=50,bg=entry_bg_color) 
    entry_sender. grid(row=0,column=1,pady=10) 
    
    tk. Label(frame_main,text="App Password  : ",bg=label_bg_color,font=font_style). grid(row=1,column=0,sticky='w',pady=5) 
    entry_password = tk. Entry(frame_main,width=50,show='*',bg=entry_bg_color) 
    entry_password. grid(row=1,column=1,pady=5) 
    
    tk. Label(frame_main,text="Receiver Mail-Id  : ",bg=label_bg_color,font=font_style). grid(row=2,column=0,sticky='w',pady=5) 
    entry_receiver = tk. Entry(frame_main,width=50,bg=entry_bg_color) 
    entry_receiver. grid(row=2,column=1,pady=5) 
    
    tk. Label(frame_main,text="Time (in minute) : ",bg=label_bg_color,font=font_style). grid(row=3,column=0,sticky='w',pady=5) 
    entry_interval = tk. Entry(frame_main,width=50,bg=entry_bg_color) 
    entry_interval. grid(row=3,column=1,pady=5) 
    
    frame_buttons = tk. Frame(frame_main,bg='pink') 
    frame_buttons. grid(row=4,columnspan=2,pady=10) 
    
    btn_start = tk. Button(frame_buttons,text="Start",command=start_logging) 
    btn_start. pack(side=tk. LEFT,padx=5) 
 
    btn_stop = tk. Button(frame_buttons,text="Stop",command=stop_logging) 
    btn_stop. pack(side=tk. LEFT,padx=5) 
    
    app. mainloop() 
    
if __name__ == "__main__": 
        main()

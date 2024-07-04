# Monitor Operating System's CPU and Send Alert

## Prerequisites

- Install Python
- `psutil` library installed (`pip install psutil`): This module provides an interface for retrieving system statistics, including CPU usage.

## Writing the 'cpu_monitor.py' Script

- Once all the dependencies are downloaded, we start by writing a python script, that will send an Email to an address from another address, both configured in the script, if the CPU of the machine is higher than 80%.
- The CPU usage data is recieved with the `psutil` module and is inserted in the `usage` variable to be used later for condition testing. (line 42: `usage = psutil.cpu_percent(interval=1)`).
- The Email is sent with the following modules:
    - smtplib: This module defines an SMTP client session object that can be used to send mail to any internet machine using the SMTP protocol.
    - email.mime.text.MIMEText and email.mime.multipart.MIMEMultipart: These classes from the email.mime module are used to construct the email message.
- *The example script: `cpu_monitor.py`.
- *a picture of the workflow of the script: `flowchart.jpg`.

## Writing in ini File for the Service

- After the script is written, we write an `ini` file to configure the new service that will run on the machine.
- *The example `ini` file: `cpu_monitor.service`
- Then, we write the following commands in the terminal, in order for the service to start and also start again whenever the machine is rebooted (enable command):
    - sudo systemctl daemon-reload
    - sudo systemctl start cpu_monitor.service
    - sudo systemctl enable cpu_monitor.service
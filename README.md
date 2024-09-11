<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body> 
    <h1>ProLogNotifier</h1>
    <p>ProLogNotifier is a sophisticated GUI-based application designed for monitoring and logging active processes in system RAM. It efficiently generates detailed log files and automatically dispatches them to a designated email address.</p>
    <h2>Features</h2> 
    <ul>
        <li><strong>Process Monitoring:</strong> Tracks and logs active processes in system RAM.</li>
        <li><strong>Detailed Logging:</strong> Generates comprehensive log files with process details.</li>
        <li><strong>Email Dispatch:</strong> Automatically sends log files to a specified email address.</li>
    </ul>
    <h2>Topics Covered</h2>
    <ul>
        <li><strong>Logger:</strong> Implements the logging functionality to capture process details.</li>
        <li><strong>Email Sender:</strong> Utilizes SMTP server to dispatch logs via email.</li>
        <li><strong>Processes:</strong> Monitors and tracks active processes in system RAM.</li>
        <li><strong>SMTP Server:</strong> Configures and uses an SMTP server for email dispatch.</li>
        <li><strong>Python 3:</strong> Developed using Python 3 for its versatility and robust libraries.</li>
        <li><strong>Tkinter GUI:</strong> Provides a user-friendly graphical interface for easy interaction.</li>
    </ul>
    <h2>Installation</h2>
    <ol>
        <li><strong>Clone the Repository:</strong>
            <pre><code>git clone https://github.com/yourusername/ProLogNotifier.git</code></pre>
        </li>
        <li><strong>Navigate to the Project Directory:</strong>
            <pre><code>cd ProLogNotifier</code></pre>
        </li>
        <li><strong>Install Dependencies:</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
    </ol>
    <h2>Configuration</h2>
    <ul>
        <li><strong>SMTP Settings:</strong> Update the <code>config.py</code> file with your SMTP server details and email credentials.</li>
        <li><strong>Email Recipient:</strong> Specify the recipient email address in the <code>config.py</code> file.</li>
    </ul>
    <h2>Usage</h2>
    <ol>
        <li><strong>Run the Application:</strong>
            <pre><code>python main.py</code></pre>
        </li>
        <li><strong>Using the GUI:</strong>
            <ul>
                <li><strong>Start Monitoring:</strong> Click the "Start Monitoring" button to begin tracking processes.</li>
                <li><strong>Stop Monitoring:</strong> Click the "Stop Monitoring" button to halt the process tracking.</li>
                <li><strong>View Logs:</strong> Access the generated log files via the GUI.</li>
            </ul>
        </li>
        <li><strong>Sending Logs:</strong> Logs will be automatically sent to the designated email address as specified in the configuration.</li>
    </ol>
</body>
</html>

import webbrowser
import os

def openWebBrowser():
    path_to_html_file = os.path.abspath('OutputData/announcementInfo.html')  # Get the path of that html file

    announcementInfo_file = f'file://{path_to_html_file}'
    webbrowser.open(announcementInfo_file)
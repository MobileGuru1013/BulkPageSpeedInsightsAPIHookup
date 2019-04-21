import pagespeed
import sys
import csv

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

urls_to_check = []
gathered_data = {}
selected_strategy = 'desktop'

p = pagespeed.PageSpeed()

def openFile():
    file_path = filedialog.askopenfilename()
    if not file_path:
        print("Bad File Path")
        exit()
    else:
        with open(file_path, 'r') as f:
            for line in f:
                urls_to_check.append(line)


def selectStrategy():
    result = messagebox.askquestion("Are you checking desktop speed?", "Are you checking desktop speed?", icon='warning')
    if result == 'yes':
        selected_strategy = 'desktop'
    else:
        selected_strategy = 'mobile'

def gatherData():
    for line in urls_to_check:
        gathered_data[line.strip()] = p.fetch(line.strip(), strategy=selected_strategy) 

def exportToCSV():
    vals = []
    with open("pagespeedinsights.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["URL", "Page Title", "Response Code", "Speed Score", "Total Roundtrips", "Total Render Blocking Roundtrips", "# of Hosts", "# of Resources", "# of CSS Resources", "# of JS Resources", "# of Static Resources", "HTML Response Bytes", "CSS Response Bytes", "JS Response Bytes", "Image Response Bytes", "Text Response Bytes", "Other Response Bytes", "Total Request Bytes"])
        for value in gathered_data.keys():
            writer.writerow([gathered_data[value].url, gathered_data[value].title, gathered_data[value].response_code, gathered_data[value].speed, gathered_data[value].total_roundtrips, gathered_data[value].total_render_blocking_roundtrips, gathered_data[value].number_hosts, gathered_data[value].number_resources, gathered_data[value].number_css_resources, gathered_data[value].number_js_resources, gathered_data[value].number_static_resources, gathered_data[value].html_response_bytes, gathered_data[value].css_response_bytes, gathered_data[value].javascript_response_bytes, gathered_data[value].image_response_bytes, gathered_data[value].text_response_bytes, gathered_data[value].other_response_bytes, gathered_data[value].total_request_bytes])

def run():
    openFile()
    selectStrategy()
    gatherData()
    exportToCSV()

if __name__ == '__main__':
    run()
import pathlib
import re
import pandas as pd
import plotly.graph_objects as go
from collections import defaultdict

# User settings

target_dir = pathlib.Path("/Users/will/Dropbox/zettelkasten/")
csv = "/Users/will/Dropbox/Projects/zkgraphs/stats.csv"
UUID_sign = "›"


# functions


def append_new_line(filename, text_to_append):
    # Append given text as a new line at the end of file
    # Open the file in append & read mode ('a+')
    with open(filename, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)


# Initialize counters

tw = 0
tl = 0
tz = 0

# Regex

date_pattern = re.compile(r"\d{8}")
link_pattern = re.compile(r"(?<!{UUID_sign})\[\[.*?\d{8}|]]‹|§\d{8}")

# Initalize output csv with headers

f = open(csv, "w+")
append_new_line(csv, "date,tz,tw,tl")

# Files is a dictionary mapping of a date to the list of files with that date

files = defaultdict(list)
for child in target_dir.iterdir():
    # Skip directories
    if child.is_dir():
        continue
    match = date_pattern.search(child.name)
    # Skip files that do not match the date pattern
    if match is None:
        continue
    file_date = match.group()
    files[file_date].append(child)

for date in sorted(files):

    for filename in files[date]:

        ## Word Count
        file = open(filename, "r")
        data = file.read()
        words = data.split()
        w = len(words)
        tw += w

        ## Link Count
        l = len(re.findall(link_pattern, data))
        tl += l

        ## Zettel Count
        tz += 1

        # print(date,tz, tw, tl, w, l) # For troubleshooting
        append_new_line(csv, f"{date},{tz},{tw},{tl}")
        file.close()

## Make graphs
# Word Count
def zk_word_count():
    zk = pd.read_csv(csv)

    zk["date"] = pd.to_datetime(zk["date"], format="%Y%m%d", errors="coerce")

    fig = go.Figure(go.Line(x=zk["date"], y=zk["tw"], name="Word count"))

    fig.update_layout(
        title="My zettelkasting progress (word count)",
        plot_bgcolor="rgb(230, 230,230)",
        showlegend=True,
    )

    fig.show()


# Link Count


def zk_link_count():
    zk = pd.read_csv(csv)

    zk["date"] = pd.to_datetime(zk["date"], format="%Y%m%d", errors="coerce")

    fig = go.Figure(go.Line(x=zk["date"], y=zk["tl"], name="Link count"))

    fig.update_layout(
        title="My zettelkasting progress (link count)",
        plot_bgcolor="rgb(230, 230,230)",
        showlegend=True,
    )

    fig.show()


# Zettel count
def zk_zettel_count():
    zk = pd.read_csv(csv)
    return zk
    # zk["date"] = pd.to_datetime(zk["date"], format="%Y%m%d", errors="coerce")

    # fig = go.Figure(go.Line(x = zk['date'], y = zk['tz'],
    #                 name='Zettel count'))

    # fig.update_layout(title='My zettelkasting progress (zettel count)',
    #                 plot_bgcolor='rgb(230, 230,230)',
    #                 showlegend=True)

    # fig.show()
    


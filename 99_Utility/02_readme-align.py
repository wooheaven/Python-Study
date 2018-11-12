readme = []

with open('99_Utility/table-of-contents.txt', 'r') as file:
    for line in file.readlines():
        readme.append(str(line).replace('\n', "").replace('\r', ""))

# 1st
for i in range(len(readme)):
    line = readme[i].replace("├──", "╠══")
    line = line.replace("└──", "╚══")
    line = line.replace("│", "║")
    line = line.replace('║   ╠', '║&ensp;&ensp;&nbsp;╠')
    line = line.replace('║   ║', '║&ensp;&ensp;&nbsp;║')
    line = line.replace('║   ╚', '║&ensp;&ensp;&nbsp;╚')
    line = line.replace('║   ║', '║&ensp;&ensp;&nbsp;║')
    line = line.replace('║       ╚', '║&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;╚')
    line = line.replace('║       ╠', '║&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;╠')
    line = line.replace('║       ║', '║&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;║')
    readme[i] = line + "  "

# print readme
for i,line in enumerate(readme):
    print(line)
    #print(i, line)


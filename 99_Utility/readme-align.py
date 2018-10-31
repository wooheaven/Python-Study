def add_indent(indent, line):
    return indent -1, "║&ensp;" + line

readme = []

with open('table-of-contents.txt', 'r') as file:
	for line in file.readlines():
		#print(line)
		readme.append(str(line).replace('\n', '').replace('\r', ''))

# 1st
for i in range(len(readme)):
	readme[i] = "╠═" + str(readme[i]) + "  "

# 2nd
for i in range(len(readme)):
	indent = len(readme[i].split('.'))
	while indent > 1:
		indent, readme[i] = add_indent(indent, readme[i])

# 3rd
for i in range(len(readme)):
	if i+1 < len(readme):
		current_indent = len(readme[i].split('.'))
		next_indent = len(readme[i+1].split('.'))
		if current_indent - next_indent == 1:
			readme[i] = readme[i].replace("╠═", "╚═")

# 4th
global_indent = len(readme[len(readme)-1].split('.'))
for i in reversed(range(len(readme))):
	if 0 < i-1:
		current_indent = len(readme[i].split('.'))
		before_indent = len(readme[i-1].split('.'))
		#print(global_indent, current_indent, before_indent, readme[i])
		if current_indent - before_indent == 1 and current_indent <= global_indent:
			readme[i] = readme[i].replace("╠═", "╚═").replace("║&ensp;", "&ensp;&ensp;")
			global_indent = before_indent
			#print(global_indent, current_indent, before_indent, readme[i])
		if global_indent == 1 and current_indent == 1:
			readme[i] = readme[i].replace("╠═", "╚═")
			#print(global_indent, current_indent, before_indent, readme[i])

# print readme
for i,line in enumerate(readme):
	print(line)
	#print(i, line)


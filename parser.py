import sys
import pydot

graph = pydot.Dot(graph_type='graph')

CFG = dict();
with open("CFG.txt","r") as file:
	for line in file:
		left, right = line.split(": ")
		if left not in CFG:
			CFG[left] = list()
			right_array = right.split()
			CFG[left].append(right_array)
		else:
			right_array = right.split()
			CFG[left].append(right_array)
print("CFG is")
for left in CFG:
	sys.stdout.write(left+":")
	print(CFG[left])

string = raw_input('\nEnter string to parse: ')
sarray = string.split()

def fun(sym,sarray):
	if sym in CFG:
		b = list();
		flag = False
		for rule in CFG[sym]:
			a = list()
			dup = list(sarray)
			edge = list()
			for x in rule:

				val,tarray = fun(x,dup)
				a.append(val)
				dup = tarray
				if val == True:	
					sarray = tarray 
					edge.append(pydot.Edge(sym,x))
					
				else:
					edge = list();
					break;
			if all(a):
				flag=True;
				#print("|"+sym)
				sarray = dup;
				break;
			else: 
				edge = list();
							
			
		if flag == True:
			for e in edge:
				graph.add_edge(e)
				
			return True, sarray
		else:
			return False, sarray
	else:
		
		if len(sarray) == 0:
			return True, sarray
		else:
			if sym == sarray[0]:
				sarray.remove(sym)
				#print("-->"+sym)
				return True, sarray
			else:
				return False, sarray
sol, f = fun("S",sarray)
if(sol):
	print("Success")
	#print(graph.del_node(pydot.Node("door")))
	graph.write_png('example1_graph.png')
else:
	print("Fail")


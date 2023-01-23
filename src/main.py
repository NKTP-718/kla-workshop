from reader import read_source


M1 = "Milestone_Input/Milestone 1/Format_Source.txt"
R1 = "results/Milestone 1.txt"
M2 = "Milestone_Input/Milestone 2/Source.txt"
P2 = "Milestone_Input/Milestone 2/POI.txt"
R2 = "results/Milestone 2.txt"
M3 = "Milestone_Input/Milestone 3/Source.txt"
P3 = "Milestone_Input/Milestone 3/POI.txt"
R3 = "results/Milestone 3.txt"
M4 = "Milestone_Input/Milestone 4/Source.txt"
P4 = "Milestone_Input/Milestone 4/POI.txt"
R4 = "results/Milestone 4.txt"
M5 = "Milestone_Input/Milestone 5/Source.txt"
P5 = "Milestone_Input/Milestone 5/POI.txt"
R5 = "results/Milestone 5.txt"
M6 = "Milestone_Input/Milestone 6/Source.txt"
P6 = "Milestone_Input/Milestone 6/POI.txt"
R6 = "results/Milestone 6.txt"
M7 = "Milestone_Input/Milestone 7/Source.txt"
P7 = "Milestone_Input/Milestone 7/POI.txt"
R7 = "results/Milestone 7.txt"

M,P,R = M7,P7,R7

template = read_source(M)
pois = read_source(P)

for polygon in template:
	match_flag = True
	for poi in pois:
		if not polygon.is_match(poi):
			match_flag = False
			break
	if match_flag:
		polygon.record_polygon(R)
from reader import read_source

# # Milestone 1
# template = read_source("Milestone_Input/Milestone 1/Format_Source.txt")
# template[0].record_polygon("results/Milestone 1.txt")
# template[1].record_polygon("results/Milestone 1.txt")
# exit(0)

# Other Milestones
N = 4
SEARCH_AREA = f"Milestone_Input/Milestone {N}/Source.txt"
TEMPLATE = f"Milestone_Input/Milestone {N}/POI.txt"
RESULTS = f"results/Milestone {N}.txt"

search_area_polygons = read_source(SEARCH_AREA)
template_polygons = read_source(TEMPLATE)

for polygon in search_area_polygons:

	for template_polygon in template_polygons:
		if template_polygon.foo(polygon):
			polygon.record_polygon(RESULTS)
			break

# Milestones passed : 1,2,3,5,6
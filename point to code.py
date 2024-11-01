points=[(142,467),(439,355),(746,477)]



for i in range(0, len(points)-1):
    s=f"output.extend(midpointlinedraw({points[i][0]}, {points[i][1]}, {points[i+1][0]}, {points[i+1][1]}))"
    print(s)
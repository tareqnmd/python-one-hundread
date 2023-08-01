import colorgram

rgb_colors = []
colors = colorgram.extract("Day 18/painting.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

vegi = ["carrot", "broccoli", "spinach", "pepper", "tomato"]
print(f"{vegi[0]}, {vegi[-2]}, {vegi[-3]}")
vegi.append("cucumber")
print(vegi)
vegi.insert(1,"onion")
print(vegi)
vegi[-2] = "lettuce"
print(vegi)
print(len(vegi))
print(vegi.index("carrot"))
vegi.reverse()
print(vegi)
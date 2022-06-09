print("\n")

# Simple JSON construct with at least two attributes.
data = {
    "name":"Python",
    "designer":"Guido van Rossum",
    "paradigm":["imperative", "procedural", "functional", "object oriented"],
    "year": 1991
}

# Write JSON to a file.
import json
text = json.dumps(data)
with open("data.json", "w") as file:
    file.write(text)

# Read from a file.
with open("data.json", "r") as file:
    text2 = file.read()
    data2 = json.loads(text2)

print("designer:", data2["designer"])
print("the third paradigm is:", data2["paradigm"][2])

print("\n")
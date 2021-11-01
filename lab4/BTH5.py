import math
T = ["lorem", "simply", "ipsum", "industry", "popular", "many", "is", "front", "the"]
D = ["doc1: the passage experienced a surge in popular during the 1960s",
    "doc2: when Letraset used it on their dry-transfer sheets",
    "doc3: desktop publishers bundled the text with their software",
    "doc4: today it's seen all around the web",
    "doc5: use our generator to get your own ",
    "doc6: or read on for the authoritative history of lorem ipsum",
    "doc7: if you are going to use a passage of lorem ipsum",
    "doc8: surge bundled get with over the years",
    "doc9: many desktop publishing packages and web page editors now use lorem ipsum as their default model text",
    "doc10: lorem Ipsum is simply dummy text of the printing and typesetting industry"]
Q = "the lorem ipsum"

def outputVector(T, d):
    d = d.split(" ")
    vector = []
    for i in T:
        vector.append(d.count(i))
    return vector

def normalize(vectorInput):
    vector = [i**2 for i in vectorInput]
    vectorOutput = []
    for i in vectorInput:
        if sum(vector) == 0:
            vectorOutput.append(0)
            continue
        vectorOutput.append(float(i/math.sqrt(sum(vector))))
    return vectorOutput

def sim(vQuery, vDoc):
    vector = [a*b for a,b in zip(vQuery,vDoc)]
    return sum(vector)

q = outputVector(T,Q)
print("vector truy vấn: ",q)
scores = []
for i in range(len(D)):
    vDoc = outputVector(T,D[i])
    v1Doc = normalize(vDoc)
    print("vector đơn vị văn bản %d: " %(i+1), normalize(v1Doc))
    scores.append(sim(q, v1Doc))
print("điểm số côsin: ", scores)

d = {}
for i in range(len(D)):
    d[D[i]] = scores[i]

items_sorted = sorted(d.items(), reverse=True, key = lambda x : x[1])
print("Danh sách văn bản được sắp xếp: ")
for a,b in items_sorted:
    print("%s : %f" %(a,b))
_nkeys = [14, 14, 14, 14, 13]
width = 10

out = ""
for nkey in _nkeys:
    if nkey == 13:
        out += " " * (width // 2)
    for key in range(nkey):
        k = "XXX,"
        spaces = " " * (width - len(k))
        out += k + spaces
    out += "\n"
print(out)

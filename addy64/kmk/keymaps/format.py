def format_keyboard(fn, key_columns=14, key_rows=5):
    import inspect
    import re

    print("Pretty formatting...")

    current_block = None
    out = {}
    extract = False
    for line in inspect.getsourcelines(fn)[0]:
        if a := re.search(r'mapping\["(?P<name>\w+)"\]', line):
            current_block = a["name"]
            out[current_block] = []
            extract = True
            continue
        if line.strip() == "]":
            extract = False
        if extract:
            keys = re.findall(r"([\w\(\)\.]+),(?:\s{1,}|\n)", line)
            if len(keys) != key_columns:
                for idx, k in enumerate(keys):
                    print(idx, k)
                raise ValueError(f"Wrong number of keys in {current_block} on line {len(out[current_block]) // key_columns}")
            out[current_block].extend(keys)
    w = 13
    for key in out:
        to_format = [f"{k}," for k in out[key]]
        print(f'    mapping["{key}"] = [')
        print(((" " * 8 + (f"{{:{w}}}" * key_columns + "\n")) * 5).format(*to_format), end="")
        print("    ]")

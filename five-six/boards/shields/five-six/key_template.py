#!/usr/bin/env python3

from enum import StrEnum


# Reference Layout
# ┌───────────────┬───────────────┬───────────────┬───────────────┬───────────────┬────────────────┐
# ├───────────────┼───────────────┼───────────────┼───────────────┼───────────────┼────────────────┤
# ├───────────────┼───────────────┼───────────────┼───────────────┼───────────────┼────────────────┤
# ├───────────────┼───────────────┼───────────────┼───────────────┼───────────────┼────────────────┤
# └───────────────┴───────────────┴───────────────┴───────┬───────┴───────┬───────┴───────┬────────┴──────┐
#                                                         └───────────────┴───────────────┴───────┬───────┴──────┐
#                                                                                                 └──────────────┘
class CoordinateClass(StrEnum):
    JUNC = "+"
    KEY = "-"
    EMPTY = " "


CC = CoordinateClass


class TableChars(StrEnum):
    TL = "┌"
    TR = "┐"
    TM = "┬"
    ML = "├"
    MR = "┤"
    MM = "┼"
    BL = "└"
    BR = "┘"
    BM = "┴"
    KEY = "─"


layout_as_lines = [
    (0, 6),
    (0, 6),
    (0, 6),
    (0, 6),
    (0, 6),
    (3.5, 3),
    (6, 1),
]
max_width = max(sum(x) for x in layout_as_lines)

# Convert layout to character grid, handling fractional offsets
filled_layout = []
matrix_scale = 3
for offset, count in layout_as_lines:
    # Calculate spaces needed (multiply by 2 to handle 0.5 increments)
    spaces = int(offset * (matrix_scale + 1))
    padding = [CC.EMPTY for _ in range(spaces)]
    row = padding
    for key in range(count):
        row.append(CC.JUNC)
        row.extend([CC.KEY for _ in range(matrix_scale)])
        if key == count - 1:
            row.append(CC.JUNC)
    tail_spaces = [
        CC.EMPTY for _ in range((max_width * (matrix_scale + 1) + 1) - len(row))
    ]
    row.extend(tail_spaces)
    filled_layout.append(row)
    # print("".join(row))


def coord_surrounds(r, c):
    above, below, left, right = CC.EMPTY, CC.EMPTY, CC.EMPTY, CC.EMPTY
    if r > 0:
        above = filled_layout[r - 1][c]
    if r < len(filled_layout) - 1:
        below = filled_layout[r + 1][c]
    if c > 0:
        left = filled_layout[r][c - 1]
    if c < len(filled_layout[r]) - 1:
        right = filled_layout[r][c + 1]
    return above, below, left, right


key_width = 15
for row_idx, row in enumerate(filled_layout):
    line = "|"
    for col_idx, cell in enumerate(row):
        preds = coord_surrounds(row_idx, col_idx)
        line += "".join([x or " " for x in preds])
        line += "|"
    print(line)

for row_idx, row in enumerate(filled_layout):
    line = ""
    for col_idx, cell in enumerate(row):
        preds = coord_surrounds(row_idx, col_idx)
        above, below, left, right = preds

        match above, below, left, right:
            case (CC.JUNC, CC.JUNC, l, r):
                match l, r:
                    case (CC.KEY, CC.KEY):
                        line += TableChars.MM
                    case (CC.KEY, CC.EMPTY):
                        line += TableChars.MR
                    case (CC.EMPTY, CC.KEY):
                        line += TableChars.ML
                    case _:
                        raise Exception(f"Invalid surround {preds}")
            case (CC.JUNC, CC.EMPTY, l, r):
                match l, r:
                    case (CC.KEY, CC.KEY):
                        if cell == CC.JUNC:
                            line += TableChars.BM
                        else:
                            line += TableChars.KEY
                    case (CC.EMPTY, CC.JUNC) | (CC.EMPTY, CC.KEY):
                        line += TableChars.BL
                    case (CC.JUNC, CC.EMPTY) | (CC.KEY, CC.EMPTY):
                        line += TableChars.ML
                    case (CC.EMPTY, CC.EMPTY):
                        line += " "
                    case _:
                        raise Exception(f"Invalid surround {preds}")
            case (CC.EMPTY, CC.JUNC, l, r):
                match l, r:
                    case (CC.EMPTY, CC.KEY):
                        line += TableChars.TL
                    case (CC.KEY, CC.KEY):
                        line += TableChars.TM
                    case (CC.KEY, CC.EMPTY):
                        line += TableChars.TR
            case (CC.EMPTY, CC.EMPTY, l, r):
                match l, r:
                    case (CC.EMPTY, CC.EMPTY) | (CC.EMPTY, CC.JUNC) | (CC.JUNC, CC.EMPTY):
                        line += " "
                    case (CC.EMPTY, CC.KEY) | (CC.KEY, CC.EMPTY):
                        line += TableChars.BR
                    case (CC.JUNC, CC.KEY) | (CC.KEY, CC.JUNC):
                        line += TableChars.KEY
                    case _:
                        raise Exception(f"Invalid surround {preds}")
            case (CC.EMPTY, CC.KEY, _, _):
                line += TableChars.KEY
            case (CC.KEY, CC.JUNC, CC.KEY, CC.KEY):
                line += TableChars.TM
            case (CC.KEY, CC.EMPTY, CC.KEY, _):
                line += TableChars.KEY
            case (CC.KEY, CC.EMPTY, _, CC.KEY):
                line += TableChars.KEY
            case (CC.KEY, CC.EMPTY, CC.EMPTY, CC.EMPTY):
                line += " "
            case (CC.KEY, CC.KEY, _, _):
                line += TableChars.KEY
            case (CC.EMPTY, CC.EMPTY, _, _):
                line += " "
            case _:
                line += "."
                # raise Exception(f"Invalid surround {preds}")
    print(line)

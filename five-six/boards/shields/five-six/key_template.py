#!/usr/bin/env python3
# run with something like:
# ./boards/shields/five-six/key_template.py --width 8 --spacing 1 --comment "//"

from enum import StrEnum
import argparse


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
    EMPTY = " "


def convert_layout_to_character_grid(layout_as_lines):
    # Convert layout to character grid, handling fractional offsets
    filled_layout = []
    matrix_scale = args.width
    max_width = max(sum(x) for x in layout_as_lines)

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
    return filled_layout


def coord_surrounds(r, c, filled_layout):
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


def draw_layout(filled_layout, debug=False):
    final_layout = []
    for row_idx, row in enumerate(filled_layout):
        line = ""
        for col_idx, cell in enumerate(row):
            preds = coord_surrounds(row_idx, col_idx, filled_layout)
            above, below, left, right = preds
            error_message = f"Invalid at {row_idx}, {col_idx} {cell!r} {''.join([str(x) for x in preds])!r}"
            match above, below, left, right:
                case (CC.JUNC, CC.JUNC, l, r):
                    match l, r:
                        case (CC.KEY, CC.KEY):
                            if cell == CC.JUNC:
                                line += TableChars.MM
                            else:
                                line += TableChars.TM
                        case (CC.KEY, CC.EMPTY):
                            line += TableChars.MR
                        case (CC.EMPTY, CC.KEY):
                            line += TableChars.ML
                        case _:
                            raise Exception(error_message)
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
                            line += TableChars.BR
                        case (CC.EMPTY, CC.EMPTY):
                            line += TableChars.EMPTY
                        case _:
                            raise Exception(error_message)
                case (CC.EMPTY, CC.JUNC, l, r):
                    match l, r:
                        case (CC.EMPTY, CC.KEY):
                            line += TableChars.TL
                        case (CC.KEY, CC.KEY):
                            line += TableChars.TM
                        case (CC.KEY, CC.EMPTY):
                            line += TableChars.TR
                        case (CC.EMPTY, CC.EMPTY):
                            line += TableChars.TR
                        case _:
                            raise Exception(error_message)
                case (CC.EMPTY, CC.EMPTY, l, r):
                    match l, r:
                        case (CC.EMPTY, CC.JUNC) | (CC.JUNC, CC.EMPTY):
                            line += TableChars.EMPTY
                        case (CC.JUNC, CC.EMPTY):
                            line += TableChars.EMPTY
                        case (CC.EMPTY, CC.EMPTY):
                            line += TableChars.EMPTY
                        case (CC.EMPTY, CC.KEY) | (CC.KEY, CC.EMPTY):
                            line += TableChars.BR
                        case (CC.JUNC, CC.KEY) | (CC.KEY, CC.JUNC):
                            line += TableChars.KEY
                        case (CC.KEY, CC.KEY):
                            line += TableChars.KEY
                        case _:
                            raise Exception(error_message)
                case (CC.EMPTY, CC.KEY, l, r):
                    match l, r:
                        case (CC.JUNC, CC.KEY) | (CC.KEY, CC.JUNC) | (CC.KEY, CC.KEY):
                            line += TableChars.KEY
                        case (
                            (CC.EMPTY, CC.JUNC)
                            | (CC.JUNC, CC.EMPTY)
                            | (CC.EMPTY, CC.EMPTY)
                        ):
                            line += TableChars.KEY
                        case (CC.EMPTY, CC.KEY) | (CC.KEY, CC.EMPTY):
                            line += TableChars.BM
                        case _:
                            raise Exception(error_message)
                case (CC.KEY, CC.EMPTY, l, r):
                    match l, r:
                        case (CC.JUNC, CC.KEY) | (CC.KEY, CC.JUNC) | (CC.KEY, CC.KEY):
                            if cell == CC.JUNC:
                                line += TableChars.BM
                            else:
                                line += TableChars.KEY
                        case (
                            (CC.EMPTY, CC.JUNC)
                            | (CC.JUNC, CC.EMPTY)
                            | (CC.EMPTY, CC.EMPTY)
                        ):
                            line += TableChars.EMPTY
                        case (CC.EMPTY, CC.KEY):
                            line += TableChars.BL
                        case _:
                            raise Exception(error_message)
                case (CC.KEY, CC.JUNC, l, r):
                    match l, r:
                        case (CC.KEY, CC.KEY):
                            line += TableChars.TM
                        case (CC.KEY, CC.EMPTY):
                            line += "F"
                        case (CC.EMPTY, CC.KEY):
                            line += "G"
                        case _:
                            raise Exception(error_message)
                case (CC.JUNC, CC.KEY, l, r):
                    match l, r:
                        case (CC.KEY, CC.KEY):
                            line += TableChars.BM
                        case (CC.KEY, CC.EMPTY):
                            line += TableChars.BM
                        case _:
                            raise Exception(error_message)
                case (CC.KEY, CC.KEY, _, _):
                    line += TableChars.KEY
                case _:
                    raise Exception(f"Invalid surround {preds}")
            if debug:
                print(line[-1], end="")
        if debug:
            print()
        final_layout.append(line)
    return final_layout


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Enable debug output")
    parser.add_argument("--width", "-w", type=int, default=15, help="Width of each key")
    parser.add_argument(
        "--comment",
        "-c",
        type=str,
        default="",
        help="Comment to add to the beginning drawn line",
    )
    parser.add_argument(
        "--spacing", "-s", type=int, default=1, help="Add newline between keys"
    )
    args = parser.parse_args()

    layout_as_lines = [
        (0, 6),
        (0, 6),
        (0, 6),
        (0, 6),
        (0, 6),
        (3.5, 3),
        (6, 1),
    ]
    filled_layout = convert_layout_to_character_grid(layout_as_lines)
    final_layout = draw_layout(filled_layout, debug=args.debug)

    for line in final_layout:
        line = args.comment + " " + line
        for _ in range(args.spacing):
            line += "\n"
        print(line)

    for line in final_layout:
        rev = args.comment + " "
        for c in line[::-1]:
            n = TableChars(c).name
            if "L" in n:
                n = n.replace("L", "R")
            elif "R" in n:
                n = n.replace("R", "L")
            rev += TableChars[n]
        for _ in range(args.spacing):
            rev += "\n"
        print(rev)

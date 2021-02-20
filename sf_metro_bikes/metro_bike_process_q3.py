from functools import partial
from datetime import datetime


def process_datestring(string):
    dt = datetime.strptime(string, datestring_format)
    return quoted(dt.isoformat().replace("T", " "))


def quoted(string):
    return f"\"{string}\""


def try_convert(f, value):
    try:
        return f(value)
    except ValueError:
        return "\"\""


try_int = partial(try_convert, int)
try_float = partial(try_convert, float)

datestring_format = "%m/%d/%Y %H:%M"
f_in_name = "q3.csv"
f_out_name = "q3_processed.csv"

with open(f_in_name) as f_in:
    processors = [
        try_int,
        try_int,
        process_datestring,
        process_datestring,
        try_int,
        try_float,
        try_float,
        try_int,
        try_float,
        try_float,
        try_int,
        try_int,
        quoted,
        quoted,
        quoted
    ]

    col_names = next(f_in)

    with open(f_out_name, "w") as f_out:
        f_out.write(",".join(map(quoted, col_names.strip().split(","))) + "\n")

        for line in f_in:
            values = line.strip().split(",")
            processed = map(str, (proc(value)
                                  for proc, value in zip(processors, values)))

            f_out.write(",".join(processed) + "\n")

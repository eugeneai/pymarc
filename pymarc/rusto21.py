"Converts RUSMARC to MARC21"
from pymarc import Record, Field

CONV={
    ("100", None, None):("008", None, None,
                         {"a" : None}),
    ("101",  "a", None):("041",  "a", " ",
                         {}),
    #("102") # FIXME -> 886
    #("105") # FIXME -> 886
    ("200",  "a", None):("245",  "a", "0",
                         {"e":"b", "f":"c",
                          "h":"n", "l":"p"}),
}

from enum import Enum

class JsonNodeType(str, Enum):
    ARRAY = "ARRAY",
    BINARY = "BINARY",
    BOOLEAN = "BOOLEAN",
    MISSING = "MISSING",
    NUMBER = "NUMBER",
    OBJECT = "OBJECT",
    POJO = "POJO",
    STRING = "STRING",


CYRILLIC_SYMBOLS = "абвгґдеёєжзиіїйклмнопрстуфхцчшщъыьэюя"
TRANSLATION = ("a", "b", "v", "h", "g", "d", "e", "e", "ie" "zh", "z",
               "y", "i", "yi", "y", "j", "k", "l", "m", "n", "o", "p",
               "r", "s", "t", "u", "f", "kh", "ts", "ch", "sh", "shch",
               "", "y", "", "e", "yu", "ya")

BAD_SYMBOLS = ("%", "*", " ", "-")

TRANS = {}
for c, t in zip(list(CYRILLIC_SYMBOLS), TRANSLATION):
    TRANS[ord(c)] = t
    TRANS[ord(c.upper())] = t.upper()

for i in BAD_SYMBOLS:
    TRANS[ord(i)] = "_"


def normalize(name: str) -> str:
    trans_name = name.translate(TRANS)
    return trans_name


if __name__ == "__main__":
    print(normalize("****Привіт-Світ%****"))
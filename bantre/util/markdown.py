import marko


#wrapper function for marko.convert()
def to_markdown(text):
    return marko.convert(text)

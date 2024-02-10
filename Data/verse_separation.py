def separate(lyrics):
    delimiters = "\n\n", "।।", "॥"
    regex_pattern = '|'.join(map(re.escape, delimiters))
    verses = re.split(regex_pattern, lyrics)

    for i in range(len(verses)):
        verses[i] = verses[i].replace('\n', ' ')
        verses[i] = verses[i].strip()

    # Remove empty strings from the list
    verses = [verse for verse in verses if verse]

    return verses
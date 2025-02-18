import re
import os


# Functions to parse CHAT formatted files by extracting and cleaning child speech
# as per CHAT Manual: https://doi.org/10.21415/3mhn-0z89


def parse_cha_text(text):
    # split text into lines
    lines = text.split("\n")
    # extract lines from text that start with *CHA:
    cha_lines = [
        re.sub(r"^\*CHI:\t*", "", line) for line in lines if line.startswith("*CHI:")
    ]
    child_speech = " ".join(cha_lines)
    # Remove special characters defined by CHAT Manual. 2 types: Outside of words and within words
    # Depending on meaning the character is replaced with "" or " " to ensure the child's speech is unedited and uniform
    # Remove outside of word characters , . ; ? ! [ ] < >
    child_speech = re.sub(r"[,.;?!]|\[.*?\]|\<.*?\>", " ", child_speech)
    # Remove withing word characters + _ - @ () &
    # @ is followed by a letter or two and indicates a special form such as unintelligible, made up, etc.
    child_speech = re.sub(r"@.*?\W", " ", child_speech)
    # & represents a phonological fragment. CHAT Manual states the material following the ampersand symbol is ignored.
    child_speech = re.sub(r"&.*?\W", " ", child_speech)
    # xxx yyy www are unintelligible speech, phonological coding, untranscribable material respectively
    child_speech = re.sub(r"xxx|yyy|www", " ", child_speech)
    # () can represent an incomplete word which the transcriber is completing
    child_speech = re.sub(r"\(|\)", "", child_speech)
    # 0word is an ommission of a word which the transcriber is completing
    child_speech = re.sub(r"0.*?\s", "", child_speech)
    # + is used as additional information such as a pause or hesitation or combining of words.
    # ex: "+..."" or "E.T." becomes "E+T"
    child_speech = re.sub(r"\+.*?\s", "", child_speech)

    # Remove extra whitespace
    child_speech = re.sub(r"\s+", " ", child_speech)
    child_speech = child_speech.lower()
    return child_speech


def parse_cha_dutch_text(text):
    text = parse_cha_text(text)
    # Remove any other special characters
    child_speech = re.sub(r"[^\wÀ-ÿ\s]", "", text)
    return child_speech


def parse_cha_spanish_text(text):
    text = parse_cha_text(text)
    # Remove any other special characters
    child_speech = re.sub(r"[^\wáéíóúñ\s]", "", text)
    return child_speech


def parse_cha_eng_text(text):
    text = parse_cha_text(text)
    # Remove any other special characters
    child_speech = re.sub(r"[^\w\s]", "", text)
    return child_speech


def parse_cha_file(file_path, language="english"):
    with open(file_path, "r") as file:
        text = file.read()
    if language == "dutch":
        return parse_cha_dutch_text(text)
    elif language == "spanish":
        return parse_cha_spanish_text(text)
    elif language == "english":
        return parse_cha_eng_text(text)
    else:
        raise ValueError(f"Language {language} not supported")


def parse_cha_folder(folder_path, language="english"):
    # Returns parsed text with each file's text separated by a newline
    print(f"Parsing {folder_path} with language {language}")
    text = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".cha"):
            file_path = os.path.join(folder_path, file_name)
            text.append(parse_cha_file(file_path, language=language))
    text = "\n".join(text)
    return text

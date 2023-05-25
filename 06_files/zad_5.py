def get_content():
    with open("pan_tadeusz.txt", encoding="utf-8") as fopen:
        content = fopen.read()
    return content

content = content.replace(',', '').split()
content = set(content)

def find_longest_word ():
    longest_word = ""
    for word in content:
        if len(word) > len(longest_word):
            longest_word = word


def main():
    quotes = get_content()




main()

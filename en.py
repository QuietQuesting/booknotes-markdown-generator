# Book notes markdown generator

def get_sections():
    """ Asks for all the sections of the book one after the other.
        Confirms if the user entered the right amount of sections,
        in case he didn't get_sections calls itself for another try (recursive) """ 

    sections = []

    print("\nJust press Enter to stop entering Chapters.\n")

    current_section = input("Enter first chapter name: ")

    while current_section != "":
        sections.append(current_section)
        current_section = input("Enter next chapter name: ")

    choice = input(f"You have entered {len(sections)} Chapters. In case that's right press just enter.")
    if choice != "":
        sections = get_sections()

    return sections


def build_file_content(title, name, sections):
    """ Bulds the content for the file in the following order:
        Title - Table of Contents - Headlines
        Table of Contens are clickable links to the following Headlines.
        title: title of the book: str, name: author name: str,
        sections: sectios of the book: list[str] """

    file_content = [f'# My notes for the book "{title}" of {name}\n', '### Table of Contents:\n']

    for num in range(1, len(sections)+1):
        section = sections[num-1]
        file_content.append(f"{num}. [{section}](#{num}. {section} "\n")

    for _ in range(2):
        file_content.append("\n")

    for num in range(1, len(sections)+1):
        file_content.extend((f"### {num}. {sections[num-1]}", "\n", "\n"))

    return file_content


def write_content_to_file(title, content):
    """ Writes the given content to a markdown file
        title: str, content: list[str] """

    with open(f"{title} Notizen.md", "w", ) as file:
        file.writelines(content)


def main():
    """ Main flow of the script. """

    print("Booknotes - markdown - file - generator.!")

    book_title = input("Enter booktitle: ")
    author_name = input("Enter authorname: ")

    book_sections = get_sections()

    file_content = build_file_content(book_title, author_name, book_sections)

    write_content_to_file(book_title, file_content)


if __name__ == "__main__":
    main()


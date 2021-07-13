# Book notes markdown generator

import gettext
supported_languages = "en", "de"

def get_locale():
    """ Try to read lang from file. """
    try:
        with open("lang.txt") as file:
            lang = file.read().lower()

        if lang in supported_languages:
            return lang
        return None

    except FileNotFoundError:
        return None


def set_locale():
    """ Writes lang to file. """
    choice = input("Choose a language: ")
    while choice not in supported_languages:
        choice = input(f"Supported languages: {supported_languages}").lower()

    with open("lang.txt", "w") as file:
        file.write(choice)
    return choice

NOTES_TRANSLATION = _("notes")

def get_sections():
    """ Asks for all the sections of the book one after the other.
        Confirms if the user entered the right amount of sections,
        in case he didn't get_sections calls itself for another try (recursive) """ 

    sections = []

    print("\n" + _("Just press Enter to stop entering Chapters.") +"\n")

    current_section = input(_("Enter first chapter name: "))

    while current_section != "":
        sections.append(current_section)
        current_section = input(_("Enter next chapter name: "))

    choice = input(_(f"You have entered {len(sections)} Chapters. In case that's right press just enter."))
    if choice != "":
        sections = get_sections()

    return sections


def build_file_content(title, name, sections):
    """ Bulds the content for the file in the following order:
        Title - Table of Contents - Headlines
        Table of Contens are clickable links to the following Headlines.
        title: title of the book: str, name: author name: str,
        sections: sectios of the book: list[str] """

    file_content = [_('# My notes for the book') + title + _('of') + name]
    file_content.append('\n### Table of Contents:\n')

    for num in range(1, len(sections)+1):
        section = sections[num-1]
        file_content.append(f"{num}. [{section}](#{num}. {section} \n")

    for _ in range(2):
        file_content.append("\n")

    for num in range(1, len(sections)+1):
        file_content.extend((f"### {num}. {sections[num-1]}", "\n", "\n"))

    return file_content


def write_content_to_file(title, content):
    """ Writes the given content to a markdown file
        title: str, content: list[str] """

    with open(f"{title} {NOTES_TRANSLATION}.md", "w", ) as file:
        file.writelines(content)


def main():
    """ Main flow of the script. """

    lang = get_locale()
    if lang is None:
        lang = set_locale()



    print(f"{NOTES_TRANSLATION}.md {_('generator')}!")

    book_title = input(_("Enter book title: "))
    author_name = input(_("Enter author name: "))

    book_sections = get_sections()

    file_content = build_file_content(book_title, author_name, book_sections)

    write_content_to_file(book_title, file_content)


if __name__ == "__main__":
    main()

 #


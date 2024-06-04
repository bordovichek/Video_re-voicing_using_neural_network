from voiceover_of_the_text import Voiceover


def main():
    file_name = input("Enter the name of the text file to be read. No need to specify format\n")
    language = input("Please enter the language (example 'ru' or 'eng'): ")

    voice = Voiceover(file_name, language)

    voice.launch()
    voice.text_to_file()
    voice.speak()


if __name__ == "__main__":
    main()

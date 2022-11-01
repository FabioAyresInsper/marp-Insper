# pylint: disable=missing-docstring
import os

BUILD_DIR = os.path.join(os.getcwd(), '..', 'build')
LECTURE_DIR = os.path.join(os.getcwd(), '..', 'example')
LECTURE_FILE = 'Aula.md'


def process_lecture(slides):
    slides = slides.replace('&aula', '1')
    slides = slides.replace('&proximo', 'Ha!')
    return slides


def main():
    # Remove files in ./build
    for filename in os.listdir(BUILD_DIR):
        os.remove(os.path.join(BUILD_DIR, filename))

    # Read the file, replace variables and save Markdown
    filename = os.path.join(LECTURE_DIR, LECTURE_FILE)
    with open(filename, 'r', encoding='utf8') as file:
        slides = file.read()

    # you can get this info from other sources
    slides = process_lecture(slides)

    filename = os.path.join(BUILD_DIR, LECTURE_FILE)
    with open(filename, 'w', encoding='utf8') as file:
        file.write(slides)

    # Call marp to build pdf of the slides
    os.system(' '.join([
        'marp',
        '--pdf',
        '--allow-local-files',
        '--theme insper-theme.css',
        filename,
    ]))

    # Clean markdown in build
    for filename in os.listdir(BUILD_DIR):
        if filename.endswith(".md"):
            os.remove(os.path.join(BUILD_DIR, filename))


if __name__ == '__main__':
    main()

import os

# Remove files in ./build

filelist = [f for f in os.listdir('./build/')]
for f in filelist:
    os.remove(os.path.join('./build/', f))

# Read the file, replace variables and save Markdown
with open('./src/Aula.md', 'r') as file:
    slides = file.read()

slides = slides.replace('&aula', '1') # you can get this info from other sources
slides = slides.replace('&proximo', 'Ha!')

with open('./build/Aula.md', 'w') as file:
    file.write(slides)

# Call marp to build pdf of the slides

os.system('marp --pdf --allow-local-files ./build/Aula.md')

# Clean markdown in build

filelist = [f for f in os.listdir('./build/') if f.endswith(".md")]
for f in filelist:
    os.remove(os.path.join('./build/', f))
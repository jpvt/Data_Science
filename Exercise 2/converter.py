import nbconvert
import nbformat

with open('Questao_2.ipynb') as nb_file:
    nb_contents = nb_file.read()

# Convert using the ordinary exporter
notebook = nbformat.reads(nb_contents, as_version=4)
exporter = nbconvert.HTMLExporter()
body, res = exporter.from_notebook_node(notebook)

# Create a dict mapping all image attachments to their base64 representations
images = {}
for cell in notebook['cells']:
    if 'attachments' in cell:
        attachments = cell['attachments']
        for filename, attachment in attachments.items():
            for mime, base64 in attachment.items():
                images[f'attachment:{filename}'] = f'data:{mime};base64,{base64}'

# Fix up the HTML and write it to disk
for src, base64 in images.items():
    body = body.replace(f'src="{src}"', f'src="{base64}"')
with open('Questao_2.html', 'w') as output_file:
    output_file.write(body)
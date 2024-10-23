import argparse
import os
from string import Template

parser = argparse.ArgumentParser()
parser.add_argument('output_dir')
parser.add_argument('--AUTHOR')
parser.add_argument('--TITLE')

args = parser.parse_args()

latex_stub_template_path = os.path.join(
    os.path.dirname(__file__),
    '../templates/latex-stub_tex.template'
)
with open(latex_stub_template_path, 'r') as f:
    content = f.read()

latex_stub_template = Template(content)
latex_stub = latex_stub_template.safe_substitute(**vars(args))

with open(args.output_dir + '/main.tex', 'w') as f:
    f.write(latex_stub)

with open(args.output_dir + '/refs.bib', 'w') as f:
    f.write('')
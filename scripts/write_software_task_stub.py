import argparse
import os
from string import Template

SOFTWARE_TASK_TEMPLATE = '../templates/softwaretask-stub_yml.template'

DEFAULT_OUTPUT_DIR = os.environ['GROUP_HOME'] + '/tools/hpc-setup/setup-tasks/software'

parser = argparse.ArgumentParser()
parser.add_argument(
    'output_dir',
    nargs='?',
    default=DEFAULT_OUTPUT_DIR
)
parser.add_argument('--APP')
parser.add_argument('--VERSION')

args = parser.parse_args()

stub_template_path = os.path.join(
    os.path.dirname(__file__),
    SOFTWARE_TASK_TEMPLATE
)
with open(stub_template_path, 'r') as f:
    content = f.read()

stub_template = Template(content)
stub = stub_template.safe_substitute(**vars(args))

output_path = f'{args.output_dir}/{args.APP}.yml'

with open(output_path, 'w') as f:
    f.write(stub)
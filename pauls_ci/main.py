#!/usr/bin/env python


import argparse
import os

from jinja2 import Template


TEMPLATES = [
    {
        'name': 'current_version',
        'path': '',
    },
    {
        'name': 'docker-compose.yaml',
        'path': '',
    },
    {
        'name': 'Dockerfile',
        'path': '',
    },
    {
        'name': '__init__.py',
        'path': 'app',
    },
    {
        'name': 'Makefile',
        'path': '',
    },
    {
        'name': 'requirements.txt',
        'path': 'app',
    },
    {
        'name': 'start.py',
        'path': 'app',
    },
    {
        'name': 'test_requirements.txt',
        'path': '',
    },
    {
        'name': '__init__.py',
        'path': 'test',
    },
    {
        'name': 'pylint.conf',
        'path': 'test',
    },
    {
        'name': 'test_start.py',
        'path': 'test',
    }
]


TEMPLATE_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'templates/{name}.j2'
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('project_name')
    parser.add_argument('base_path', default='.')
    args = parser.parse_args()
    
    project_path = os.path.join(
        os.path.abspath(args.base_path),
        args.project_name
    )
    
    for template in TEMPLATES:
        with open(TEMPLATE_PATH.format(name=template['name'])) as f:
            raw_template = Template(f.read())

        rendered_template = raw_template.render(name='1')

        target_directory = os.path.join(project_path, template['path'])
        template_target = os.path.join(target_directory, template['name'])
        
        if not os.path.isdir(target_directory):
            os.makedirs(target_directory)
        
        with open(template_target, 'w') as f:
            f.write(rendered_template)

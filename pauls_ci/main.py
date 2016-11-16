#!/usr/bin/env python


import argparse
import os
import yaml

from jinja2 import Template


TEMPLATE_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'templates/{name}.j2')


def load_manifest(**kwargs):
    manifest_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'manifest.yml.j2')

    with open(manifest_path) as f:
        manifest_template = Template(f.read())

    manifest = yaml.load(manifest_template.render(**kwargs))
    
    return manifest


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument('project_name')
    parser.add_argument('base_path', default='.')
    template_args = vars(parser.parse_args())
    
    project_path = os.path.join(
        os.path.abspath(template_args['base_path']),
        template_args['project_name'])
    
    templates = load_manifest(**template_args)

    for template in templates:
        print template
        with open(TEMPLATE_PATH.format(name=template['name'])) as f:
            raw_template = Template(f.read())

        rendered_template = raw_template.render(**template_args)

        target_directory = os.path.join(project_path, template['path'])
        template_target = os.path.join(target_directory, template['name'])
        
        if not os.path.isdir(target_directory):
            os.makedirs(target_directory)
        
        with open(template_target, 'w') as f:
            f.write(rendered_template)

#!/usr/bin/env python


import os
import yaml

from jinja2 import Template


def load_manifest(**kwargs):
    manifest_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'manifest.yml.j2')

    with open(manifest_path) as f:
        manifest_template = Template(f.read())

    manifest = yaml.load(manifest_template.render(**kwargs))
    
    return manifest


def load_template(manifest, **kwargs):
    template_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'templates/{name}.j2')
    
    with open(template_path.format(name=manifest['name'])) as f:
        raw_template = Template(f.read())

    rendered_template = raw_template.render(**kwargs)

    return rendered_template


def write_rendered_template(rendered_template, project_path, manifest):
    target_directory = os.path.join(project_path, manifest['path'])
    template_target = os.path.join(target_directory, manifest['name'])

    if not os.path.isdir(target_directory):
        os.makedirs(target_directory)

    with open(template_target, 'w') as f:
        f.write(rendered_template)

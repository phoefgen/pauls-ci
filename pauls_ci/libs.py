#!/usr/bin/env python


import os
import yaml

from jinja2 import Template


def load_manifests(**kwargs):
    """Render and load the manifests.

    The manifests describe the name and location of each
    file that must be created from a template.

    The manifests are in a Jinja2 template of a YAML file. The
    manifests will be rendered with any keyword arguments
    that are given to this function.

    :returns: the manifests
    :rtype: list(dict)
    """
    manifest_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'manifests.yml.j2')

    with open(manifest_path) as f:
        manifest_template = Template(f.read())

    manifests = yaml.load(manifest_template.render(**kwargs))
    
    return manifests


def load_template(manifest, **kwargs):
    """Render and load a template.

    Templates are in Jinja2 (.j2) format. They will be
    rendered with any extra keyword arguments that are
    given to this function.

    :param dict manifest: the properties of the template
    
    :returns: the rendered template
    :rtype: str
    """
    template_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'templates/{name}.j2')
    
    with open(template_path.format(name=manifest['name'])) as f:
        raw_template = Template(f.read())

    rendered_template = raw_template.render(**kwargs)

    return rendered_template


def write_rendered_template(rendered_template, project_path, manifest):
    """Write a rendered template to the file system.

    :param str rendered_template: the template, rendered as a string
    :param str project_path: the base path of the new project
    :param dict manifest: the properties of the template
    """
    target_directory = os.path.join(project_path, manifest['path'])
    template_target = os.path.join(target_directory, manifest['name'])

    if not os.path.isdir(target_directory):
        os.makedirs(target_directory)

    with open(template_target, 'w') as f:
        f.write(rendered_template)

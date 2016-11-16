#!/usr/bin/env python


import argparse
import os


import libs


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument('project_name')
    parser.add_argument('base_path', default='.')
    
    # Get the command line arguments. Convert to dict.
    template_args = vars(parser.parse_args())
    
    # Define the path at which the new project should be created.
    project_path = os.path.join(
        os.path.abspath(template_args['base_path']),
        template_args['project_name'])
    
    # Render and load the manifest.yml.j2 file.
    # The manifest is a list of dicts. Each dict describes the name
    # and location of a file that must be created from a template.
    manifests = libs.load_manifests(**template_args)

    # Iterate through each manifest.
    for manifest in manifests:
        # Render and load each template.
        rendered_template = libs.load_template(manifest, **template_args)
        
        # Write the rendered template to the file system.
        libs.write_rendered_template(rendered_template, project_path, manifest)

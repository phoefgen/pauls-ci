#!/usr/bin/env python


import argparse
import os


import libs


def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument('project_name')
    parser.add_argument('base_path', default='.')
    template_args = vars(parser.parse_args())
    
    project_path = os.path.join(
        os.path.abspath(template_args['base_path']),
        template_args['project_name'])
    
    manifests = libs.load_manifest(**template_args)

    for manifest in manifests:
        rendered_template = libs.load_template(manifest, **template_args)
        libs.write_rendered_template(rendered_template, project_path, manifest)

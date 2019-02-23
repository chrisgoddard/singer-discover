import os
import sys
import argparse
import json
from singer import metadata
import tty

from PyInquirer import prompt
# import questionary
# from prompt_toolkit.input import create_input, set_default_input
# from prompt_toolkit.input.defaults import create_pipe_input
# from prompt_toolkit.input import Input


def breadcrumb_name(breadcrumb):
    name = ".".join(breadcrumb)
    name = name.replace('properties.', '')
    name = name.replace('.items', '[]')
    return name


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', '-o', type=str, required=True)

    if sys.stdin.isatty():
        parser.add_argument('--input', '-i', type=str, required=True)

        args = parser.parse_args()

        with open(args.input) as f:
            catalog = json.load(f)

    else:

        args = parser.parse_args()

        catalog = json.loads(sys.stdin.read())

        sys.stdin = sys.stdout

    select_streams = {
        'type': 'checkbox',
        'message': 'Select Streams',
        'name': 'streams',
        'choices': [
            {'name': stream['stream']} for stream in catalog['streams']
        ]
    }

    selected_streams = prompt(select_streams)

    for i, stream in enumerate(catalog['streams']):

        mdata = metadata.to_map(stream['metadata'])

        if stream['stream'] not in selected_streams['streams']:
            mdata = metadata.write(
                mdata, (), 'selected', False
            )
        else:
            mdata = metadata.write(
                mdata, (), 'selected', True
            )

            fields = []

            field_reference = {}

            for breadcrumb, field in mdata.items():

                if breadcrumb != ():
                    selected, disabled = False, False
                    if metadata.get(
                            mdata, breadcrumb, 'inclusion') == 'automatic':
                        selected, disabled = True, "automatic"

                    elif metadata.get(
                            mdata, breadcrumb, 'selected-by-default'):
                        selected, disabled = True, False

                    name = breadcrumb_name(breadcrumb)

                    field_reference[name] = breadcrumb

                    fields.append({
                        'name': name,
                        'checked': selected,
                        'disabled': disabled
                    })

            stream_options = {
                'type': 'checkbox',
                'message': 'Select fields from stream: `{}`'.format(
                    stream['stream']),
                'name': 'fields',
                'choices': fields
            }

            selections = prompt(stream_options)

            selections = [
                field_reference[n] for n in selections['fields']
                if n != "Select All"
            ]

            for breadcrumb in mdata.keys():
                if breadcrumb != ():
                    if (
                        metadata.get(
                            mdata, breadcrumb, 'inclusion') == "automatic"
                    ) or (
                        breadcrumb in selections
                    ):
                        mdata = metadata.write(
                            mdata, breadcrumb, 'selected', True)
                    else:
                        mdata = metadata.write(
                            mdata, breadcrumb, 'selected', False)

            catalog['streams'][i]['metadata'] = metadata.to_list(mdata)

    with open(args.output, 'w') as f:
        json.dump(catalog, f, indent=2)


if __name__ == '__main__':
    main()

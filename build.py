#!/usr/bin/env python
"""Generate html documentation"""

__requires__ = 'Sphinx>=1.1.2'

import sys, os
from pkg_resources import load_entry_point

# Allow this script to find its doc config resource
docs_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,docs_path)

# Make sure conf is a valid Sphinx configuration module
import conf
assert conf

def main(argv=None):
    if argv:
        sys.argv = argv
    # Generate documentation
    return load_entry_point(__requires__, 'console_scripts',
        'sphinx-build')()

if __name__ == "__main__":

    # generate rendered html on the docs/html directory.
    os.chdir(docs_path)
    ret_val = main(
        ['render_docs.py','-b','html','-d','_temp','.','_build/html'])

    if ret_val == 0:
        print ''
        print 'CONGRATULATIONS! Look in _build/html/'
    sys.exit(ret_val)


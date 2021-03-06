# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Script support for validating the WCS keywords in a FITS file.
"""

from __future__ import absolute_import

def main(args=None):
    from . import wcs
    from astropy.utils.compat import argparse

    parser = argparse.ArgumentParser(
        description=("Check the WCS keywords in a FITS file for "
                     "compliance against the standards"))
    parser.add_argument(
        'filename', nargs=1, help='Path to FITS file to check')
    args = parser.parse_args(args)

    print(wcs.validate(args.filename[0]))

#!/usr/bin/env python

import argparse
import subprocess  # nosec

import semver

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=(
            """Bump the version of the latest release tag by a supported version level """
            """modifier and print the tag value to stdout."""
        )
    )

    bump_levels = ['major', 'minor', 'patch', 'prerelease']
    parser.add_argument(
        'bump_level',
        help="level to bump the tag from by one",
        choices=bump_levels,
        type=str
    )

    args = parser.parse_args()

    latest_tag = subprocess.check_output( # nosec
        ['/usr/bin/env', 'git', 'tag', '--sort=-creatordate']
    ).decode().split('\n')[0].replace('v', '')

    if args.bump_level:
        action = getattr(semver, f'bump_{args.bump_level}')
        latest_version = action(latest_tag)

    print(latest_version)

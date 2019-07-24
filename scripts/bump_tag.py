#!/usr/bin/env python

import subprocess
import sys

if __name__ == '__main__':
    bump_level = None
    if len(sys.argv) > 1:
        bump_level = sys.argv[1]
    latest_tag = subprocess.run(
        ['git', 'tag', '--sort=-creatordate'],
        check=True,
        capture_output=True
    ).stdout.decode().split('\n')[0]

    major, minor, patch = map(int, latest_tag.replace('v', '').split('.'))
    new_tag = {
        'major': major,
        'minor': minor,
        'patch': patch
    }

    if bump_level:
        new_tag[bump_level] += 1

    print(f"v{'.'.join(map(str, new_tag.values()))}")

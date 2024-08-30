#!/usr/bin/env python3

import re
import sys

regex = r"(?P<before>.*)(?P<type>class|struct|record|record)(?P<type2> struct)?(?P<classname>[^(]+)\s*\((?P<params>[^)]+)"
next_line_remove_brace = False

filename = sys.argv[1]
with open(filename) as f:
    for line in f:
        match = re.search(regex, line)
        if match and match.group('type') and match.group('classname'):
            params_str = ''.join(list(map(lambda s: f'public {s} {{ get; set; }}', match.group('params').split(',')))) if match.group('params') else ''
            print(f"{match.group('before') or ''}{match.group('type')}{match.group('type2') or ''} {match.group('classname')} {{ {params_str}", end='')
            next_line_remove_brace = True
        else:
            if next_line_remove_brace:
                next_line_remove_brace = False # I mean this does remove it...
                print('')
            else:
                print(line, end='')
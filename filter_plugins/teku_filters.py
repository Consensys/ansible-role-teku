#! /usr/bin/env python

from typing import Union, List


class FilterModule(object):
    def filters(self):
        return {
            'teku_opts_format': self.tekuOptsFormat,
        }

    def tekuOptsFormat(self, teku_env_opts: Union[str, List[str]]):
        if isinstance(teku_env_opts, str):
            teku_env_opts = teku_env_opts.split()

        escaped_teku_env_opts = [item.replace('"', '\\"') for item in teku_env_opts]

        # Quote each option individually
        # ["one", "two", "three"] -> "one" "two" "three"
        return f'''"{'" "'.join(escaped_teku_env_opts)}"'''

"""Treadmill module launcher.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from . import console

# pylint complains "No value passed for parameter ... in function call".
# This is ok, as these parameters come from click decorators.
if __name__ == '__main__':
    console.run()  # pylint: disable=no-value-for-parameter

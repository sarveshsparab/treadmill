"""Implementation of cell API.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from treadmill import admin
from treadmill import context
from treadmill import schema


class API(object):
    """Treadmill Cell REST api."""

    def __init__(self):

        def _admin_cell():
            """Lazily return admin object."""
            return admin.Cell(context.GLOBAL.ldap.conn)

        def _list():
            """List cells."""
            return _admin_cell().list({})

        @schema.schema({'$ref': 'cell.json#/resource_id'})
        def get(rsrc_id):
            """Get cell configuration."""
            result = _admin_cell().get(rsrc_id)
            result['_id'] = rsrc_id
            return result

        @schema.schema(
            {'$ref': 'cell.json#/resource_id'},
            {'allOf': [{'$ref': 'cell.json#/resource'},
                       {'$ref': 'cell.json#/verbs/create'}]}
        )
        def create(rsrc_id, rsrc):
            """Create cell."""
            _admin_cell().create(rsrc_id, rsrc)
            return _admin_cell().get(rsrc_id)

        @schema.schema(
            {'$ref': 'cell.json#/resource_id'},
            {'allOf': [{'$ref': 'cell.json#/resource'},
                       {'$ref': 'cell.json#/verbs/update'}]}
        )
        def update(rsrc_id, rsrc):
            """Update cell."""
            _admin_cell().update(rsrc_id, rsrc)
            return _admin_cell().get(rsrc_id)

        @schema.schema({'$ref': 'cell.json#/resource_id'})
        def delete(rsrc_id):
            """Delete cell."""
            _admin_cell().delete(rsrc_id)

        self.list = _list
        self.get = get
        self.create = create
        self.update = update
        self.delete = delete

# Copyright (c) 2015 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
fbx Output node App for use with Toolkit's Houdini engine.
"""

import sgtk


class TkfbxNodeApp(sgtk.platform.Application):
    """The fbx Output Node."""

    def init_app(self):
        """Initialize the app."""

        tk_houdini_fbx = self.import_module("tk_houdini_fbx")
        self.handler = tk_houdini_fbx.TkfbxNodeHandler(self)

    def convert_to_regular_fbx_nodes(self):
        """Convert Toolkit fbx nodes to regular fbx nodes.

        Convert all Toolkit fbx nodes found in the current script to
        regular fbx nodes. Additional Toolkit information will be stored in
        user data named 'tk_*'

        Example usage::

        >>> import sgtk
        >>> eng = sgtk.platform.current_engine()
        >>> app = eng.apps["tk-houdini-fbxnode"]
        >>> app.convert_to_regular_fbx_nodes()

        """

        self.log_debug("Converting Toolkit fbx nodes to built-in fbx nodes.")
        tk_houdini_fbx = self.import_module("tk_houdini_fbx")
        tk_houdini_fbx.TkfbxNodeHandler.convert_to_regular_fbx_nodes(self)

    def convert_back_to_tk_fbx_nodes(self):
        """Convert regular fbx nodes back to Tooklit fbx nodes.

        Convert any regular fbx nodes that were previously converted
        from Tooklit fbx nodes back into Toolkit fbx nodes.

        Example usage::

        >>> import sgtk
        >>> eng = sgtk.platform.current_engine()
        >>> app = eng.apps["tk-houdini-fbxnode"]
        >>> app.convert_back_to_tk_fbx_nodes()

        """

        self.log_debug(
            "Converting built-in fbx nodes back to Toolkit fbx nodes."
        )
        tk_houdini_fbx = self.import_module("tk_houdini_fbx")
        tk_houdini_fbx.TkfbxNodeHandler.convert_back_to_tk_fbx_nodes(self)

    def get_nodes(self):
        """
        Returns a list of hou.node objects for each tk fbx node.

        Example usage::

        >>> import sgtk
        >>> eng = sgtk.platform.current_engine()
        >>> app = eng.apps["tk-houdini-fbxnode"]
        >>> tk_fbx_nodes = app.get_nodes()
        """

        self.log_debug("Retrieving tk-houdini-fbx nodes...")
        tk_houdini_fbx = self.import_module("tk_houdini_fbx")
        nodes = tk_houdini_fbx.TkfbxNodeHandler.get_all_tk_fbx_nodes()
        self.log_debug("Found %s tk-houdini-fbx nodes." % (len(nodes),))
        return nodes

    def get_output_path(self, node):
        """
        Returns the evaluated output path for the supplied node.

        Example usage::

        >>> import sgtk
        >>> eng = sgtk.platform.current_engine()
        >>> app = eng.apps["tk-houdini-fbxnode"]
        >>> output_path = app.get_output_path(tk_fbx_node)
        """

        self.log_debug("Retrieving output path for %s" % (node,))
        tk_houdini_fbx = self.import_module("tk_houdini_fbx")
        output_path = tk_houdini_fbx.TkfbxNodeHandler.get_output_path(node)
        self.log_debug("Retrieved output path: %s" % (output_path,))
        return output_path

    def get_work_file_template(self):
        """
        Returns the configured work file template for the app.
        """

        return self.get_template("work_file_template")

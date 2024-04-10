[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/nfa-vfxim/tk-houdini-fbxnode?include_prereleases)](https://github.com/nfa-vfxim/tk-houdini-fbxnode) 
[![GitHub issues](https://img.shields.io/github/issues/nfa-vfxim/tk-houdini-fbxnode)](https://github.com/nfa-vfxim/tk-houdini-fbxnode/issues) 


# fbx Output Node

Support for the Toolkit fbx output node in Houdini.

> Supported engines: tk-houdini

## Requirements

| ShotGrid version | Core version | Engine version |
|------------------|--------------|----------------|
| -                | v0.12.5      | v1.7.1         |

## Configuration

### Strings

| Name                | Description                                                                                                                           | Default value |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------|---------------|
| `default_node_name` | A default name for fbx output nodes created in houdini. Allowed characters include letters, numbers, periods, dashes, or underscores. | sgtk_fbx      |


### Templates

| Name                 | Description                                                                                                                                      | Default value | Fields                   |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|---------------|--------------------------|
| `work_file_template` | A reference to a template which locates a Houdini work file on disk.  This is used to drive the version and optionally the name of output files. |               | context, version, [name] |


### Lists

| Name              | Description                                                                                                                                                                                                                                                                                  | Default value |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| `output_profiles` | A list of dictionaries defining the various fbx output profiles. Each profile contains a unique name that describes the profile, the cach template for writing to disk, a color to distinguish each profile type in the node graph, and optional settings to apply to the internal fbx node. |               |



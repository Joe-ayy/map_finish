#!/usr/bin/env python


from gimpfu import *


def python_finish(timg, tdrw, floorx, floory, steps):
    img = gimp.image_list()[0]
    drw = pdb.gimp_image_get_active_layer(img)

    pdb.gimp_selection_none(img)
    pdb.gimp_image_select_contiguous_color(img, 0, drw, floorx, floory)
    pdb.gimp_selection_invert(img)
    pdb.gimp_context_set_foreground((0, 0, 0))
    pdb.gimp_drawable_edit_fill(drw, 0)
    pdb.gimp_selection_invert(img)
    pdb.gimp_selection_grow(img, steps)
    pdb.gimp_selection_invert(img)
    pdb.gimp_context_set_foreground((204, 204, 204))
    pdb.gimp_drawable_edit_fill(drw, 0)
    pdb.gimp_selection_none(img)

    gimp.displays_flush


register(
    "python_fu_finish",
    "Finish up mapping",
    "Finish editing the map",
    "Austin Herman, modified by Joey Harrison",
    "AH, JH",
    "2018",
    "<Image>/Tools/Transform Tools/Map Cleanup/_Finish",
    "RGB*, GRAY*",
    [
        (PF_INT, "floorx", "Sales Floor X Coordinate: ", 0),
        (PF_INT, "floory", "Scale Floor Y Coordinate: ", 0),
        (PF_INT, "steps", "Thickness: ", 0)
    ],
    [],
    python_finish)

main()
import numpy as np


def augment_data(problem, solution, debug=False):
    if debug:
        print('Augmenting data...')
    
    # Data lebelling inconsistent
        # NODE_COORD_SECTION (correct)
        # DISPLAY_DATA_SECTION (false)
    
    # TODO cluster
    # TODO augment data
        # relative coords to gride center
        # relative coords to node cluster
        # coords of previous in tau
        # coords of next in tau
        # boolean, is in tau
    return problem
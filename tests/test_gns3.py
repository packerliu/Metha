import os
import sys
import pytest
#sys.path.append('..')
import GNS3.gns3_interface

def test_rungns3():
    """
    Runs GNS3 using provided configuration files
    :param args: Argument namespace from argparse
    """
    path = os.path.abspath('../ExampleNet')
    gp, adj = gns3_interface.init_gns_from_files(get_dir(path))
    
    for name in gp.nodes:
        node = gp.nodes[name]
        if issubclass(type(node), PyEZNode):
            node.pyez_connection.close()
            node.pyez_connection = None

    print('Running GNS3')
    input('Press any key to stop execution')

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4
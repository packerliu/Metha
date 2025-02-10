import os
import sys
import pytest
#sys.path.append('..')
#import GNS3.gns3_interface


import rt_comparator
import test_coordinator
from Evaluation import eval_metrics
from GNS3 import gns3_interface
from GNS3.Nodes.pyez_node import PyEZNode
from GNS3.router_types import RouterTypes
from RouterConfiguration import feature_parser
from Systems.Batfish import batfish_interface
from Systems.CBGP import cbgp_interface
from Systems.NV import nv_interface
from test_generator import CombinatorialTestGenerator, BoundedTestGenerator, RandomTestGenerator
from utils import filter_optional

from metha import get_dir

def test_rungns3():
    """
    Runs GNS3 using provided configuration files
    :param args: Argument namespace from argparse
    """
    path = os.path.abspath('ExampleNet')
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


if __name__ == '__main__':
    test_rungns3()
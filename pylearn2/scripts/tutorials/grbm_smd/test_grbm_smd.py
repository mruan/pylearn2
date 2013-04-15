import pylearn2
from pylearn2.utils.serial import load_train_file
import os
from nose.plugins.skip import SkipTest
from pylearn2.testing import no_debug_mode
from theano import config

@no_debug_mode
def test_train_example():
    """ tests that the grbm_smd example script runs correctly """
    assert config.mode != "DEBUG_MODE"
    if 'TRAVIS' in os.environ and os.environ['TRAVIS'] == '1':
        raise SkipTest()
    path = pylearn2.__path__[0]
    train_example_path = path + '/scripts/tutorials/grbm_smd'
    cwd = os.getcwd()
    print cwd
    try:
#        os.chdir(train_example_path)
        train_yaml_path = 'cifar_grbm_smd.yaml'
        train_object = load_train_file(train_yaml_path)

        #make the termination criterion really lax so the test won't run for long
        train_object.algorithm.termination_criterion.prop_decrease = 0.5
        train_object.algorithm.termination_criterion.N = 1

        train_object.main_loop()
    finally:
        os.chdir(cwd)

if __name__ == '__main__':
    test_train_example()

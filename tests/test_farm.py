# -*- coding: utf-8 -*-

import pytest
import cafe.farm as cf
import cafe.importData as importData
import numpy as np

__author__ = "Mathematical Michael"
__copyright__ = "Mathematical Michael"
__license__ = "mit"


def test_farm_instantiation_defaults():
    test_farm = cf.Farm()
    # TODO: add some basics here and assert them
    print("Current working directory:")
    !pwd
    
    assert test_farm.totalCuerdas == 1
    assert test_farm.pruneYear == None
    assert test_farm.treeType == 'borbon'
    
    testDict = importData.openYaml("../data/trees.yml")
    test_farm02 = cf.Farm(treeAttributes = testDict)
    assert test_farm02.treeType == 'borbon'
    

    # this is another syntax structure to accomplish the above
    # but it is new to me, personally -- mm
    #with pytest.raises(AssertionError):


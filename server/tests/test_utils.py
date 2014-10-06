from OSOM_server import utils

TEST_LIST = [0,1,2,3,4,5,6]

def test_pick_one_random_item():
    trials = 10
    res_list = []
    for i in xrange(trials):
        res_list.append(utils.pick_one_random_item(TEST_LIST))
    # expect atleast 3 different items in res_list
    ver_list = {}
    for item in res_list:
        if item not in ver_list:
            ver_list[item] = 0
        else:
            ver_list[item] += 1
    assert len(ver_list) > 2

def test_pick_one_random_item_empty_list():
    assert utils.pick_one_random_item([]) is None

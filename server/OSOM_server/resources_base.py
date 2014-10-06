
class Resource(object):

    def __init__(self):
        self._init()

    # Implement the following functions in a child class
    # to access these properties

    def _init(self):
        """
        Can be implemented in child classes for initializing the child class
        """

    @property
    def name(self):
        """
        Name of the Resource. return string
        """
        raise NotImplementedError

    def pick_one(self,res):
        """
        Query the resource and pick one item to be served from the response
        """
        raise NotImplementedError

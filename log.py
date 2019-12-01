
class Log:
    VERBOSITY_NONE = 0
    VERBOSITY_VERBOSE = 1
    class __Log:
        def __init__(self, verbosity):
            self.verbosity = verbosity

        def trace(self, message):
            if self.verbosity>0: print message

        def setVerbosity(self, verbosity):
            self.verbosity = verbosity

    instance = None
    def __init__(self):
        if not Log.instance:
            Log.instance = Log.__Log(Log.VERBOSITY_NONE)
    

    def trace(self, message):
        if Log.instance:
            Log.instance.trace(message)

    def setVerbosity(self, verbosity):
        if Log.instance:
            Log.instance.setVerbosity(verbosity)


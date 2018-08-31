# Utils library used by the openapi

# Approximated KM to LA/LO values based on London's elevation
KM_TO_LA = 0.009
KM_TO_LO = 0.0145

class Utils(object):

	# Used often to get ranges around a value (esp in search queries)
    @staticmethod
    def max_min_value(value, range):
        min_value = value - range
        max_value = value + range
        return min_value, max_value
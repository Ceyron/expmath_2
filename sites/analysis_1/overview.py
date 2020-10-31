"""
Overview of all the apps under this topic
"""

from sites.analysis_1.info import details as details_info

from sites.analysis_1.epsilon import details as details_epsilon
from sites.analysis_1.sums import details as details_sums
from sites.analysis_1.simple_functions import details as details_simple_functions

overview = {
    "german": {
        "apps": {
            "Übersicht": {
                "name": "info",
                "type": "simple",
                "details": details_info,
            },
            "Epsilon Kriterium": {
                "name": "epsilon",
                "type": "regular",
                "details": details_epsilon,
            },
            "Partialsummen und Reihen": {
                "name": "sums",
                "type": "regular",
                "details": details_sums,
            },
            "Standardfunktionen": {
                "name": "simple_functions",
                "type": "regular",
                "details": details_simple_functions,
            },
        }
    }
}
"""
Overview of all the apps under this topic
"""

from sites.analysis_1.epsilon import details as details_epsilon
from sites.analysis_1.sums import details as details_sums

overview = {
    "german": {
        "apps": {
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
        }
    }
}
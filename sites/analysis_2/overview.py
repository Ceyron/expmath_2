"""
Contains the overview of all apps that belong to this topic
"""

from sites.analysis_2.info import details as details_info
from sites.analysis_2.parameterization_3d import details as details_paramerization_3d

overview = {
    "german": {
        "apps": {
            "Übersicht": {
                "name": "info",
                "type": "simple",
                "details": details_info,
            },
            "Parametrisierung (3D)": {
                "name": "parameterization_3d",
                "type": "regular",
                "details": details_paramerization_3d,
            },
        }
    }
}
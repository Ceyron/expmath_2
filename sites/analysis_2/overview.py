"""
Contains the overview of all apps that belong to this topic
"""

from sites.analysis_2.info import details as details_info
from sites.analysis_2.parameterization_3d import details as details_paramerization_3d
from sites.analysis_2.fourier_series import details as details_fourier_series

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
            "Fourier-Reihen": {
                "name": "fourier_series",
                "type": "regular",
                "details": details_fourier_series,
            },
        }
    }
}

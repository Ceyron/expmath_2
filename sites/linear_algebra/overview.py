"""
Contains the overview of all apps that belong to this topic
"""

from sites.linear_algebra.info import details as details_info
from sites.linear_algebra.complex_roots import details as details_complex_roots

overview = {
    "german": {
        "apps": {
            "Übersicht": {
                "name": "info",
                "type": "simple",
                "details": details_info,
            },
            "Komplexe Wurzeln": {
                "name": "complex_roots",
                "type": "regular",
                "details": details_complex_roots,
            },
        }
    }
}
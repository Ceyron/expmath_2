"""
Contains the overview of all apps that belong to this topic
"""

from sites.linear_algebra.complex_roots import details as details_complex_roots

overview = {
    "german": {
        "apps": {
            "Komplexe Wurzeln": {
                "name": "complex_roots",
                "type": "regular",
                "details": details_complex_roots,
            },
        }
    }
}
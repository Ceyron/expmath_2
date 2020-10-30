"""
Contains the overview of all apps that belong to this topic
"""

from sites.pde.info import details as details_info
from sites.pde.diffusion import details as details_diffusion

overview = {
    "german": {
        "apps": {
            "Übersicht": {
                "name": "info",
                "type": "simple",
                "details": details_info,
            },
            "Wärmeleitung": {
                "name": "diffusion",
                "type": "regular",
                "details": details_diffusion,
            }
        }
    }
}
"""
Contains the overview of all apps that belong to this topic
"""

from sites.pde.diffusion import details as details_diffusion

overview = {
    "german": {
        "apps": {
            "Wärmeleitung": {
                "name": "diffusion",
                "type": "regular",
                "details": details_diffusion,
            }
        }
    }
}
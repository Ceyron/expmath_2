"""
Comprises an overview of all the sites and the respective structure. D
"""
from sites.analysis_1.overview import overview as overview_analysis_1
from sites.linear_algebra.overview import overview as overview_linear_algebra
from sites.analysis_2.overview import overview as overview_analysis_2
from sites.ode.overview import overview as overview_ode
from sites.analysis_3.overview import overview as overview_analysis_3
from sites.pde.overview import overview as overview_pde

site_overview = {
    "german": {
        "topics": {
            "Analysis 1": {
                "name": "analysis_1",
                "overview": overview_analysis_1,
            },
            "Lineare Algebra": {
                "name": "linear_algebra",
                "overview": overview_linear_algebra,
            },
            "Analysis 2": {
                "name": "analysis_2",
                "overview": overview_analysis_2,
            },
            "Gewöhnliche DGL": {
                "name": "ode",
                "overview": overview_ode,
            },
            "Analysis 3": {
                "name": "analysis_3",
                "overview": overview_analysis_3,
            },
            "Partielle DGL": {
                "name": "pde",
                "overview": overview_pde,
            },
        }
    }
}
# coding=utf-8
from . import activities
from . import parameters
from . import activities

class Config:
    def __init__(self, target_database, version):
        """
        Create new config

        Parameters
        ----------
        target_database : str
            Name of the database to use to store parasol activities
        version : str
            Version string of ecoinvent database such as "3.7", "3.9" ...

        Returns
        -------
        config

        """
        self.prefix = "[parasol] "
        self.version = version
        self.target_database = target_database
        self.biosphere = f"ecoinvent-{version}-biosphere"
        self.technosphere = f"ecoinvent-{version}-cutoff"

    @staticmethod
    def from_dict(d : dict):
        """
        Create config from dictionnary

        Parameters
        ----------
        d : dict
        expected keys:
            - target_database = database to use to store new activities (string)
            - version = ecoinvent version used (string)
            - (optional) prefix = prefix for created activities (string)
            - (optional) biosphere = biosphere database name (string)
            - (optional) technosphere = technosphere database name (string)

        Returns
        -------
        config

        """
        conf = Config(d["target_database"], d["version"])
        conf.prefix = d.get("prefix", conf.prefix)
        conf.biosphere = d.get("biosphere", conf.biosphere)
        conf.technosphere = d.get("technosphere", conf.technosphere)
        return conf


def create(conf : Config|dict):
    """Create the updated PV system dataset, related activities, and 2 impact
    models with PARASOL_LCA.

    Parameters
    ----------
    conf: dict
        expected keys:
            - target_database = database to use to store new activities (string)
            - version = ecoinvent version used (string)
            - (optional) prefix = prefix for created activities (string)
            - (optional) biosphere = biosphere database name (string)
            - (optional) technosphere = technosphere database name (string)

    """
    if isinstance(conf, dict):
        conf = Config.from_dict(conf)
    #ensure_metalisation(conf)
    activities.ensure_impact_model_per_kWh(conf)

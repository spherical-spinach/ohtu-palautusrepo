from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        project = toml.loads(content)

        name = project["tool"]["poetry"]["name"]
        description = project["tool"]["poetry"]["description"]
        dependencies = project["tool"]["poetry"]["dependencies"]
        dev_dependencies = project["tool"]["poetry"]["group"]["dev"]["dependencies"]
        authors = project["tool"]["poetry"]["authors"]
        license = project["tool"]["poetry"]["license"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies, authors, license)

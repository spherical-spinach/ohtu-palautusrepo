class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, authors, license):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.authors = authors
        self.license = license

    def _stringify_dependencies(self, dependencies):
        return "\n- ".join([""] + list(dependencies.keys()))

    def _stringify_authors(self, authors):
        return "\n- ".join([""] + authors)


    def __str__(self):
        dependencies = "\n- ".join([""] + list(self.dependencies.keys()))
        dev_dependencies = "\n- ".join([""] + list(self.dev_dependencies.keys()))

        return (
            f"Name: {self.name}\n"
            f"Description: {self.description or '-'}\n"
            f"License: {self.license}\n\n"
            f"Authors:\n" + "\n".join(["- " + author for author in self.authors]) + "\n\n"
            f"Dependencies:{dependencies}\n\n"
            f"Development dependencies:{dev_dependencies}"
        )


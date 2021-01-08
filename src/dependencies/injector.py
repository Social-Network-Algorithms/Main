from src.dependencies.dao_module import DAOModule
from src.dependencies.activity_module import ActivityModule
from src.dependencies.process_module import ProcessModule


class Injector():
    """
    The Injector is used to initialize all the modules used to inject
    dependencies
    """

    def __init__(self, config):
        self.config = config

        self.dao_module = None
        self.process_module = None
        self.activity_module = None

    def get_dao_module(self) -> DAOModule:
        if self.dao_module is None:
            self.dao_module = DAOModule(self.config)

        return self.dao_module

    def get_process_module(self) -> ProcessModule:
        if self.process_module is None:
            dao_module = self.get_dao_module()
            self.process_module = ProcessModule(dao_module)

        return self.process_module

    def get_activity_module(self) -> ActivityModule:
        if self.activity_module is None:
            dao_module = self.get_dao_module()
            process_module = self.get_process_module()
            self.activity_module = ActivityModule(self, dao_module,
                process_module)

        return self.activity_module

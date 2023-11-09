""" ClassInitizalizer module """
from importlib import import_module
from typing import TypeVar

# from tests.robot.tools.DirtyLogger import DirtyLogger


class ClassInitializer:
    """class ClassInitializer"""
    _is_mocked = False
    T = TypeVar("T")

    @classmethod
    def create_object(cls, expected_lib: T, *args, **kwargs) -> T:
        """
        Usage:
        from tests.robot.core.RadioJson import RadioJson
        object = ClassInitializer.create_object(RadioJson, self.hw_variant)
        if is_mocked is False then just creates provided object
        if is_mocked is True:
            get module name:
            'tests.robot.core.RadioJson'
            add "Mock" to end: 'tests.robot.core.RadioJsonMock'
            then try to import class like:
            from tests.robot.core.RadioJsonMock import RadioJsonMock
            if Mock object does not exist then just create expected object.
        Works with typehint, so:
        object = ClassInitializer.create_object(RadioJson, self.hw_variant)
        object. will have hits for "RadioJson".
        """
        if not cls._is_mocked:
            # DirtyLogger().trace(f'Loading: {expected_lib.__name__} class')
            return expected_lib(*args, **kwargs)
        module_path = expected_lib.__module__
        mocked_module_path = f"{module_path}Mock"
        try:
            imported_module = import_module(mocked_module_path)
            imported_class = getattr(imported_module, mocked_module_path.split('.')[-1])
            # DirtyLogger().info(f'Loading Mock class: {imported_class.__name__}')
            return imported_class(*args, **kwargs)
        except ModuleNotFoundError as exc:
            # DirtyLogger().trace(exc)
            # DirtyLogger().info(f'No Mocked class found, loading: {expected_lib.__name__} class')
            return expected_lib(*args, **kwargs)

    @classmethod
    def set_is_mocked(cls):
        """_is_mocked class attribute  setter"""
        cls._is_mocked = False

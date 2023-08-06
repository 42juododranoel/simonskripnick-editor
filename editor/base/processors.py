from abc import abstractmethod


class BaseProcessor:
    """Any processor should derive from this one."""

    @abstractmethod
    def __init__(self) -> None:
        ...

    @abstractmethod
    def validate(self) -> None:
        ...

    @abstractmethod
    def run(self) -> None:
        ...

    def __call__(self) -> None:
        self.validate()
        return self.run()

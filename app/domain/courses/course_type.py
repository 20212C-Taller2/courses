from enum import Enum, auto


class StrEnum(str, Enum):
    # noinspection PyMethodParameters
    def _generate_next_value_(name, start, count, last_values) -> str:  # type: ignore
        """
        Uses the name as the automatic value, rather than an integer

        See https://docs.python.org/3/library/enum.html#using-automatic-values for reference
        """
        return name


class CourseType(StrEnum):
    WEB_DEVELOPMENT = auto()
    COOKING = auto()
    WOODWORKING = auto()
    MATHEMATICS = auto()
    YOGA = auto()
    GRAPHIC_DESIGN = auto()

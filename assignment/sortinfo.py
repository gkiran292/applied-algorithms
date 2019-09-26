# Auto generated code begins (source: https://app.quicktype.io?share=iY2RZ7Zi6BWId16RjKBm)
from dataclasses import dataclass
from typing import List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class SortInfo:
    sort_technique: str
    iteration_number: int
    input_n: int
    time_in_secs: float
    sort_list: List[int]

    @staticmethod
    def from_dict(obj: Any) -> 'SortInfo':
        assert isinstance(obj, dict)
        sort_technique = from_str(obj.get("sort_technique"))
        iteration_number = from_int(obj.get("iteration_number"))
        input_n = from_int(obj.get("input_n"))
        time_in_secs = from_float(obj.get("time_in_secs"))
        sort_list = from_list(from_int, obj.get("sort_list"))
        return SortInfo(sort_technique, iteration_number, input_n, time_in_secs, sort_list)

    def to_dict(self) -> dict:
        result: dict = {"sort_technique": from_str(self.sort_technique),
                        "iteration_number": from_int(self.iteration_number), "input_n": from_int(self.input_n),
                        "time_in_secs": to_float(self.time_in_secs), "sort_list": from_list(from_int, self.sort_list)}
        return result


def sort_info_from_dict(s: Any) -> List[SortInfo]:
    return from_list(SortInfo.from_dict, s)


def sort_info_to_dict(x: List[SortInfo]) -> Any:
    return from_list(lambda sort_info: to_class(SortInfo, sort_info), x)
# Auto generated code ends

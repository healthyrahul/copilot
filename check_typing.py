from typing import List, Tuple, Set, Union, Any

def parse_permission(json: List[Any]) -> Tuple[bool, List]:
    flag = True
    # json = [{}, {}]
    return flag, json


flag, json = parse_permission([{}, {}])
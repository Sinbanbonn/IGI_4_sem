BASE_TYPES = r"str|int|float|bool|NoneType|list|dict"
ELEMENT = fr"\s*(\<(?P<key>{BASE_TYPES})\>(?P<value>([^<>]*)|(?R)+)\</(?:{BASE_TYPES})\>)\s*"

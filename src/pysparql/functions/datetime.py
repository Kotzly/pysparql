from .base import Function


class Now(Function):
    _keyword = "NOW"


class Year(Function):
    _keyword = "YEAR"


class Month(Function):
    _keyword = "MONTH"


class Day(Function):
    _keyword = "DAY"


class Hours(Function):
    _keyword = "HOURS"


class Minutes(Function):
    _keyword = "MINUTES"


class Seconds(Function):
    _keyword = "SECONDS"


class Timezone(Function):
    _keyword = "TIMEZONE"


class TZ(Function):
    _keyword = "TZ"

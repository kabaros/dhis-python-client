from enum import Enum


class HtmlPushAnalyticsJobParametersMode(str, Enum):
    EXECUTOR = "EXECUTOR"
    RECEIVER = "RECEIVER"

    def __str__(self) -> str:
        return str(self.value)

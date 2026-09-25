
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum


@dataclass
class SuspiciousAction:

    timestamp: datetime
    reason: str

class UserStatus(Enum):

    DEFAULT = 'default'
    PREMIUM = 'premium'


class User():

    def __init__(self, name: str, balance: float, status: UserStatus = UserStatus.DEFAULT,
                 is_blocked: bool = False, suspicious_actions_history: list[SuspiciousAction] = None) -> None:

        self.name = name
        self.balance = balance
        self.status = status
        self.is_blocked = is_blocked
        self.suspicious_actions_history = suspicious_actions_history if suspicious_actions_history else []

    def add_suspicious_action(self, time: datetime, reason: str) -> None:

        susp_action = SuspiciousAction(timestamp=time, reason=reason)

        self.suspicious_actions_history.append(susp_action)


    def get_recent_suspicious_count(self, minutes: int = 30) -> int:

        counter = 0

        time_start = datetime.now() - timedelta(minutes=minutes)

        for action in self.suspicious_actions_history:

            if action.timestamp > time_start:

                counter += 1

        return counter






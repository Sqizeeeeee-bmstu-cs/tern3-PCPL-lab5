import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from datetime import datetime, timedelta
from user import User, UserStatus, SuspiciousAction



def test_user_initialization():

    user1 = User(name="Alice", balance=1000.0)
    user2 = User(name="Bob", balance=500.0)

    assert user1.name == 'Alice'
    assert user1.balance == 1000.0
    assert user1.status == UserStatus.DEFAULT
    assert user1.is_blocked == False

    assert len(user1.suspicious_actions_history) == 0

    assert user2.suspicious_actions_history is not user1.suspicious_actions_history



def test_add_suspicious_action():

    user = User(name="Charlie", balance=2000.0)
    now = datetime.now()
    reason = "High volume transaction"
    
    user.add_suspicious_action(time=now, reason=reason)
    
    assert len(user.suspicious_actions_history) == 1

    action = user.suspicious_actions_history[0]

    assert isinstance(action, SuspiciousAction)

    assert action.reason == reason
    assert action.timestamp == now



def test_get_recent_suspicious_count_time_window():

    user = User(name="Diana", balance=1500.0)
    
    now = datetime.now()
    time_fresh_1 = now - timedelta(minutes=5)
    time_fresh_2 = now - timedelta(minutes=25)
    time_old = now - timedelta(minutes=35)
    
    user.add_suspicious_action(time=time_fresh_1, reason="Fresh 1")
    user.add_suspicious_action(time=time_fresh_2, reason="Fresh 2")
    user.add_suspicious_action(time=time_old, reason="Old action")
    

    assert user.get_recent_suspicious_count(30) == 2

    assert user.get_recent_suspicious_count(40) == 3

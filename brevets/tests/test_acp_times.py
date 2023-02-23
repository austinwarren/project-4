"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

from acp_times import open_time, close_time
import arrow
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_brevet1():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    dist = 200
    checkpoints = { 
        0:   (start_time, start_time.shift(hours=1)),
        50:  (start_time.shift(hours=1, minutes=28), start_time.shift(hours=3.5)),
        150: (start_time.shift(hours=4, minutes=25), start_time.shift(hours=10)),
        200: (start_time.shift(hours=5, minutes=53), start_time.shift(hours=13.5))
    }
    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close


def test_brevet2():
    start_time = arrow.get("2023-02-22 00:00", "YYYY-MM-DD HH:mm")
    dist = 400
    checkpoints = { 
        0:   (start_time, start_time.shift(hours=1)),
        400:  (start_time.shift(hours=12, minutes=8), start_time.shift(hours=3))
    }
    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close

def test_brevet3():
    start_time = arrow.get("2023-02-22 00:00", "YYYY-MM-DD HH:mm")
    dist = 300
    checkpoints = { 
        0:   (start_time, start_time.shift(hours=1)),
        100.3:  (start_time.shift(hours=2, minutes=56), start_time.shift(hours=6, minutes=40)),
        176.2: (start_time.shift(hours=5, minutes=11), start_time.shift(hours=11, minutes=44)),
        300.0: (start_time.shift(hours=9), start_time.shift(hours=20))
    }
    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close

def test_brevet4():
    start_time = arrow.get("2023-02-22 00:00", "YYYY-MM-DD HH:mm")
    dist = 600
    checkpoints = { 
        0:   (start_time, start_time.shift(hours=1)),
        338:  (start_time.shift(hours=10, minutes=12), start_time.shift(hours=22, minutes=32)),
        478.2: (start_time.shift(hours=14, minutes=44), start_time.shift(hours=7, minutes=52)),
        480: (start_time.shift(hours=14, minutes=48), start_time.shift(hours=8)),
        500: (start_time.shift(hours=15, minutes=28), start_time.shift(hours=9, minutes=20)),
        578: (start_time.shift(hours=18, minutes=4), start_time.shift(hours=14, minutes=32)),
        600: (start_time.shift(hours=18, minutes=48), start_time.shift(hours=16)),
    }
    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close

def test_brevet5():
    start_time = arrow.get("2023-02-22 00:00", "YYYY-MM-DD HH:mm")
    dist = 1000
    checkpoints = { 
        0:   (start_time, start_time.shift(hours=1)),
        1:   (start_time.shift(hours=0, minutes=2), start_time.shift(hours=1, minutes=3)),
        223: (start_time.shift(hours=6, minutes=36), start_time.shift(hours=14, minutes=52)),
        333: (start_time.shift(hours=10, minutes=2), start_time.shift(hours=22, minutes=12)),
        654: (start_time.shift(hours=20, minutes=44), start_time.shift(hours=20, minutes=44)),
        874: (start_time.shift(hours=4, minutes=35), start_time.shift(hours=15, minutes=59)),
        1000:(start_time.shift(hours=9, minutes=5), start_time.shift(hours=3)),
    }
    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close


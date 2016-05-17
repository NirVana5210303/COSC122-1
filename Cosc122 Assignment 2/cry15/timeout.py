import signal

DEFAULT_TIMEOUT = 30

class TimeoutException(Exception):
    """A timeout has occurred."""
    pass

class call_with_timeout:
    def __init__(self, function, timeout=DEFAULT_TIMEOUT):
        self.timeout = timeout
        self.function = function

    def handler(self, signum, frame):
        signal.signal(signal.SIGALRM, self.old)
        signal.alarm(0)
        info_string = 'TIMED OUT after ' + str(self.timeout) + ' seconds'
        raise AssertionError(info_string)

    def __call__(self, *args):
        # get the old SIGALRM handler
        self.old = signal.signal(signal.SIGALRM, self.handler)
        # set the alarm
        signal.alarm(self.timeout)
        try:
            result = self.function(*args)
        finally:
            # restore existing SIGALRM handler
            signal.signal(signal.SIGALRM, self.old)
        signal.alarm(0)
        return result

    def __get__(self, obj, objtype):
        """Support instance methods."""
        import functools
        return functools.partial(self.__call__, obj)

def timeout(timeout):
    """This decorator takes a timeout parameter in seconds.
    Test timing-out:
    >>> import time

    >>> @timeout(timeout=2)
    ... def return_later():
    ...     time.sleep(3)
    ...     return 'later'
    >>>
    >>> return_later()
    Traceback (most recent call last):
        ...
    TimeoutException
    """
    def wrap_function(function):
        return call_with_timeout(function, timeout)
    return wrap_function

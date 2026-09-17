from gamebasic.signal.signal import Signal


class SignalBus:
    def __init__(self) -> None:
        self._signals:dict[str,Signal] = {}

    def add(self, signal:Signal) -> None:
        self._signals[signal.name] = signal

    def check(self, signal_name: str) -> bool:
        return signal_name in self._signals

    def get(self, signal_name: str) -> Signal:
        ret:Signal|None = self._signals.get(signal_name)
        if ret is None:
            raise KeyError("No key found!")

        return ret

    def pop(self, signal_name: str) -> Signal:
        """
        returns and removes signal.
        prefered to use frequently than get function.
        """
        ret = self._signals.pop(signal_name)
        return ret
        

    def remove(self, signal_name: str)->None:
        self._signals.pop(signal_name)

    def clear(self) -> None:
        self._signals.clear()
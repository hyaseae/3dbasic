from gamebasic.objects.signal import Signal


class SignalBus:
    def __init__(self) -> None:
        self._signals:dict[str,Signal] = {}

    def add(self, signal:Signal) -> None:
        self._signals[signal.name] = signal

    def check(self, signal_name: str) -> bool:
        return self._signals.get(signal_name, None) is None

    def get(self, signal_name: str) -> Signal:
        ret:Signal|None = self._signals.get(signal_name)
        if ret is None:
            raise KeyError("No key found!")

        return ret

        

    def remove(self, signal_name: str)->None:
        self._signals.pop(signal_name)

    def clear(self) -> None:
        self._signals.clear()
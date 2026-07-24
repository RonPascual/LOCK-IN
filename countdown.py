from dataclasses import dataclass
import math
import time


@dataclass
class CountdownUpdate:
    started: bool = False
    reset: bool = False
    opened_website: bool = False
    countdown_second: int | None = None


@dataclass
class CountdownState:
    required_detection_time: int = 5
    absence_reset_time: int = 30
    phone_detected: bool = False
    phone_detected_time: float = 0.0
    phone_last_seen_time: float = 0.0
    last_countdown_second: int | None = None

    def update(self, saw_phone, now=None):
        if now is None:
            now = time.time()

        update = CountdownUpdate()

        if saw_phone:
            self.phone_last_seen_time = now

            if not self.phone_detected:
                self.phone_detected = True
                self.phone_detected_time = now
                self.last_countdown_second = self.required_detection_time
                update.started = True
                update.countdown_second = self.required_detection_time
                return update

            elapsed = now - self.phone_detected_time
            if elapsed >= self.required_detection_time:
                self.phone_detected = False
                self.phone_detected_time = 0.0
                self.phone_last_seen_time = 0.0
                self.last_countdown_second = None
                update.opened_website = True
                return update

            countdown_second = max(0, math.ceil(self.required_detection_time - elapsed))
            if countdown_second != self.last_countdown_second:
                self.last_countdown_second = countdown_second
                update.countdown_second = countdown_second

            return update

        if self.phone_detected and (now - self.phone_last_seen_time) >= self.absence_reset_time:
            self.phone_detected = False
            self.phone_detected_time = 0.0
            self.phone_last_seen_time = 0.0
            self.last_countdown_second = None
            update.reset = True

        return update

    def current_countdown(self, now=None):
        if not self.phone_detected:
            return None

        if now is None:
            now = time.time()

        return max(0, math.ceil(self.required_detection_time - (now - self.phone_detected_time)))
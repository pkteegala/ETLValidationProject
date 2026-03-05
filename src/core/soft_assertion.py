
class SoftAssert:
    def __init__(self):
        self._errors: list[str] = []

    def check(self, condition: bool, message: str):
        if not condition:
            self._errors.append(message)

    def assert_all(self):
        if self._errors:
            joined = "\n".join(f"- {e}" for e in self._errors)
            raise AssertionError(f"Multiple assertion failures:\n{joined}")
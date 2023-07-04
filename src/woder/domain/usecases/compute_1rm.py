from dataclasses import dataclass


@dataclass
class Compute1RMRequest:
    weight: float
    number_of_reps: int


@dataclass
class Compute1RMResponse:
    max_load: float


class Compute1RMUsecase:
    def handle(self, request: Compute1RMRequest) -> Compute1RMResponse:
        max_load = 36 * request.weight / (37 - request.number_of_reps)
        return Compute1RMResponse(max_load=round(max_load, ndigits=1))

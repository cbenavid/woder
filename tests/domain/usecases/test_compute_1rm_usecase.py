import pytest

from woder.domain.usecases.compute_1rm import Compute1RMRequest, Compute1RMUsecase


class TestCompute1RMUsecase:
    def setup(self) -> None:
        self.usecase = Compute1RMUsecase()

    def test_given_zero_weight_and_zero_reps_when_compute_then_result_is_zero(
        self,
    ) -> None:
        # Arrange
        request = Compute1RMRequest(weight=0, number_of_reps=0)

        # Act
        response = self.usecase.handle(request)

        # Assert
        assert response.max_load == 0

    @pytest.mark.parametrize("weight", [1, 2])
    def test_given_any_weight_and_one_rep_when_compute_then_result_is_same_weight(
        self, weight: float
    ) -> None:
        # Arrange
        request = Compute1RMRequest(weight=weight, number_of_reps=1)

        # Act
        response = self.usecase.handle(request)

        # Assert
        assert response.max_load == weight

    @pytest.mark.parametrize("weight,expected", [(50, 66.7), (34, 45.3)])
    def test_given_any_weight_and_any_number_of_reps_when_compute_then_result_is_coherent(
        self, weight: float, expected: float
    ) -> None:
        # Arrange
        request = Compute1RMRequest(weight=weight, number_of_reps=10)

        # Act
        response = self.usecase.handle(request)

        # Assert
        assert response.max_load == expected

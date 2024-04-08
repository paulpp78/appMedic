import pytest
from faker import Faker
from src.models.signalement import Signalement

fake = Faker()


@pytest.mark.parametrize(
    "pseudo, code_cip, expected_exception",
    [
        (fake.user_name(), str(fake.random_number(digits=3)), ValueError),
        (fake.user_name(), str(fake.random_number(digits=7)), None),
        (fake.user_name(), str(fake.random_number(digits=13)), None),
        (fake.user_name(), str(fake.random_number(digits=0)), ValueError),
        (fake.user_name(), str(fake.random_number(digits=14)), ValueError),
        (fake.user_name(), str(fake.random_number(digits=4)), ValueError),
        (fake.user_name(), str(fake.random_number(digits=10)), ValueError),
    ],
)
def test_signalement_validation(pseudo, code_cip, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            Signalement(pseudo=pseudo, code_cip=code_cip)
    else:
        signalement = Signalement(pseudo=pseudo, code_cip=code_cip)
        assert signalement.pseudo == pseudo
        assert signalement.code_cip == str(code_cip)

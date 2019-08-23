from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert True


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert False


def test__cat_years_to_hooman_years__0__returns_0():
    if 1==1 or 4==4:
        assert False
    else:
        assert False


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True

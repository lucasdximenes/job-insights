from src.pre_built.sorting import sort_by

'''
def sort_by(jobs: List[Dict], criteria: str) -> None:
    """
    Sorts jobs by a given criteria, in-place.

    Sorting must be descending, except for `min_salary` criteria.
    Jobs missing the criteria should end up last.
    Invalid criteria should raise ValueError.

    Parameters
    ----------
    jobs : list
        List of dicts representing the jobs.
    criteria : str
        One of `min_salary`, `max_salary` or `date_posted`.
    """
    criteria_keys = {
        "date_posted": date_posted_key,
        "max_salary": max_salary_key,
        "min_salary": min_salary_key,
    }

    try:
        key = criteria_keys[criteria]
    except KeyError:
        raise ValueError(f"invalid sorting criteria: {criteria}")

    reverse = criteria in ["max_salary", "date_posted"]

    jobs.sort(key=key, reverse=reverse)
'''


def test_sort_by_criteria():
    jobs = [
        {"max_salary": "1000"},
        {"max_salary": "2000"},
        {"max_salary": "3000"},
    ]
    sort_by(jobs, "max_salary")
    assert jobs == [
        {"max_salary": "3000"},
        {"max_salary": "2000"},
        {"max_salary": "1000"},
    ]

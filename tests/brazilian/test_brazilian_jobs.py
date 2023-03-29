from src.pre_built.brazilian_jobs import read_brazilian_file
from unittest.mock import patch

'''
def read_brazilian_file(path: str) -> List[Dict]:
    """Reads a portuguese file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    dict_jobs = jobs.read(path)
    for job in dict_jobs:
        job["title"] = job.pop("titulo")
        job["salary"] = job.pop("salario")
        job["type"] = job.pop("tipo")

    return dict_jobs
'''


mock_jobs = [
    {
        "titulo": "titulo",
        "salario": "salario",
        "tipo": "tipo",
    }
]


def test_brazilian_jobs():
    with patch("src.insights.jobs.read", return_value=mock_jobs) as mock_read:
        assert read_brazilian_file("path") == [
            {
                "title": "titulo",
                "salary": "salario",
                "type": "tipo",
            }
        ]
        mock_read.assert_called_once_with("path")

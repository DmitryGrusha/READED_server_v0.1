from enum import Enum

class Genre(Enum):
    Romance = 1
    Adventure = 2
    Thriller = 3
    Fantasy = 4
    YoungAdult = 5
    Mystery = 6
    Historical = 7
    Horror = 8
    ScienceFiction = 9
    Humorous = 10
    Christian = 11
    Western = 12


def get_array_of_ids_by_name(cases_names: [str]) -> [int]:
    results = []
    for case_name in cases_names:
        for genre_case in Genre.__members__:
            if case_name.lower() == genre_case.lower():
                results.append(Genre[genre_case].value)
    return results

def get_array_of_names_by_ids(cases_ids: [int]) -> [str]:
    results = []
    for case_id in cases_ids:
        for genre in Genre:
            if case_id == genre.value:
                results.append(Genre[case_id])
    return results
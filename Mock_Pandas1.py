# Problem 1 biggest_single_number
import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    counts = my_numbers['num'].value_counts()
    num = counts[counts ==1].index
    if len(num) == 0:
        df = pd.DataFrame([None], columns = ['num'])
    else:
        df = pd.DataFrame([sorted(num)[-1]], columns = ['num'])
    return df

# Problem 2 not_boring_movies
import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema[(cinema['id']%2 != 0) & (cinema['description'] != 'boring')].sort_values('rating', ascending = False)


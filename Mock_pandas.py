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


# Problem 3 Market Analysis I
import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders = orders[(orders['order_date'] >= "2019-01-01") & (orders['order_date'] <= "2019-12-31")]
    df = users.merge(orders, left_on = 'user_id', right_on = 'buyer_id', how = 'left')
    return df.groupby(['user_id', 'join_date']).agg(orders_in_2019 = ('order_id', 'count'))\
             .reset_index().rename(columns = {'user_id': 'buyer_id'})

# Problem 4 sales_analysis III
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    
    sales_in_2019 = sales[(sales['sale_date'] >= '2019-01-01') & (sales['sale_date'] <= '2019-03-31')][['product_id']]
    sales_other = sales[(sales['sale_date'] < '2019-01-01') | (sales['sale_date'] > '2019-03-31')][['product_id']]
    
    sales_exclsuive_in_2019 = sales_in_2019[~sales_in_2019['product_id'].isin(sales_other['product_id'])].drop_duplicates()
    
    return sales_exclsuive_in_2019.merge(product, on = 'product_id', how = 'inner').drop(columns = ['unit_price'])
from data.melbourne import melbourne_data, Cols, format_mae_price
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import GradientBoostingRegressor

features = [
    Cols.YEAR_BUILT,
    Cols.LANDSIZE,
    Cols.BATHROOM,
    Cols.BEDROOM2,
    Cols.ROOMS,
    Cols.BUILDING_AREA,
    Cols.DISTANCE,
    Cols.PROPERTY_COUNT,
    Cols.CAR,
    Cols.LATTITUDE,
    Cols.LONGITUDE
]

data_length = len(melbourne_data)
melbourne_data = melbourne_data[[Cols.PRICE, *features]]
melbourne_data =  melbourne_data.dropna(axis=0)
data_length_after_drop = len(melbourne_data)

print(f'Z {data_length} wierszy po wykluczeniu tych z brakującymi danymi pozostało {data_length_after_drop}. Pozostało więc {(data_length_after_drop /data_length * 100):.2f}% danych')

# drop 5% most expensive and cheapest apartments
melbourne_data = melbourne_data.sort_values(Cols.PRICE)
row_count = melbourne_data.shape[0]
five_percent = int(0.05 * row_count)
melbourne_data = melbourne_data.iloc[five_percent:-five_percent]

# features and predicate
features_X = melbourne_data[features] # X
predicate_Y = melbourne_data[Cols.PRICE] # y

# train 80% of data and choose 20% for testing
train_X, test_X, train_Y, test_Y = train_test_split(features_X, predicate_Y, random_state=0, test_size=0.2)

# gradient boosting regression
model_gradient_boosted = GradientBoostingRegressor(n_estimators=500, random_state=1)
model_gradient_boosted.fit(train_X, train_Y)
model_boosted_predictions = model_gradient_boosted.predict(test_X)
mae = format_mae_price(mean_absolute_error(model_boosted_predictions, test_Y))

print(f'Przewidywane ceny mieszkań różnią się zazwyczaj (przy technice budowania lepszych drzew) o {mae}')
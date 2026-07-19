from utils.loader import load_data, validate_dataset, dataset_summary

df = load_data()
validate_dataset(df)

print(dataset_summary(df))
print(df.head())
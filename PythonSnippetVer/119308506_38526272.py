df_list = generate_data_frames(94, 5)

# Append all data frames together using reduce
df_append = reduce(lambda df_1, df_2 : df_1.append(df_2), df_list)

# Aggregate by Code 1 and Code 2
df_append_grouped = df_append.groupby(['Code 1', 'Code 2'], as_index=False)
df_append_result = df_append_grouped.aggregate(np.mean)
df_append_result
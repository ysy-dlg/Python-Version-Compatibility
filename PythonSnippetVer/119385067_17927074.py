def find_average_record(sen_set, voting_dict):
    count = len(sen_set)
    return [sum(col) / count for col in zip(*(voting_dict[sen] for sen in sen_set))]
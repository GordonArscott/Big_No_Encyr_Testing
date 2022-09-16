def fix_is_store_open(current_time, opening_times):
    current_time = current_time.replace(':', '')
    opening_time_list = opening_times.replace(':', '').split('-')
    start = opening_time_list[0]
    end = opening_time_list[1]
    # you can also explictly convert to int, strings work though:
    if current_time > '2359' or start > '2359' or end > '2359':
        return 'invalid time'
    else:
        return start <= current_time <= end



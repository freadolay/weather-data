def check_for_element(label, p_elements):
    for x in p_elements:
        if label in x.get_text():
            tf = True
            element = x
            return tf, element
    return False, None

def weeks_lkp(season):
    if season == 2021:
        week_nums = range(1,19)
    else:
        week_nums = range(1,18)
    ## Create a Week Number, Label, and href
    # Week Number
    week_numbers = []
    week_labels = []
    week_hrefs = []
    for week_num in week_nums:
        week_numbers.append(week_num)
        week_labels.append(f'Week {week_num}')
        if season == 2010:
            week_hrefs.append(f'week-{week_num}-2')
        else:
            week_hrefs.append(f'week-{week_num}')
    playoff_games = [
        'Wild Card',
        'Divisional',
        'Conf Champ',
        'Super Bowl'
    ]
    playoff_hrefs = [
        'wildcard-weekend',
        'divisional-playoffs',
        'conf-championships',
        'superbowl'
    ]
    for i, label in enumerate(playoff_games):
        week_numbers.append(week_numbers[-1]+1)
        week_labels.append(label)
        if season==2010:
            week_hrefs.append(playoff_hrefs[i]+'-2')
        else:
            week_hrefs.append(playoff_hrefs[i])
    return week_numbers, week_labels, week_hrefs
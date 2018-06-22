MAP_DESCRIPTIONS = {
    'H003': 'Housing units (100% count)',
    'H006': 'Occupancy status',
    'H009': 'Race of householder',
    'H030': 'Units in structure',
    'H034': 'Year structure built',
    'H035': 'Median year structure built',
    'H074': 'Value for specified owner-occupied housing units',
    'H076': 'Median value for specified owner-occupied housing units',
    'H080': 'Mortgage status',
    'H085': 'Median value for ALL owner-occupied housing units',
    'P003': 'Population (100% count)',
    'P006': 'Race',
    'P052': 'Household income in 1999',
    'P053': 'Median household income in 1999',
}

MAP_NAMES = {
    'H003': 'housing_units_total',
    'H006': [None, 'housing_units_occupied', 'housing_units_vacant'],
    'H009': [
        None,
        'population_white',
        'population_black',
        'population_american_indian_or_native',
        'population_asian',
        'population_hawaiian_or_pacific',
        'population_other',
        'population_multi'
    ],
    'H030': [
        None, 'housing_units_detached', 'housing_units_attached',
        None, None, None, None, None, None, None, None
    ],
    'H034': [
        None,
        'built_1999_to_2000',
        'built_1995_to_1998',
    ],
    'H035': 'Median year structure built',
    'H074': 'Value for specified owner-occupied housing units',
    'H076': 'Median value for specified owner-occupied housing units',
    'H080': 'Mortgage status',
    'H085': 'Median value for ALL owner-occupied housing units',
    'P003': 'Population (100% count)',
    'P006': 'Race',
    'P052': 'Household income in 1999',
    'P053': 'Median household income in 1999',
}

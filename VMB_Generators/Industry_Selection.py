

def Get_Subindustry(input_sector):
    dict_sectors = {'Communication Services': ['Advertising', 'Broadcasting', 'Interactive Home Entertainment',
                                               'Interactive Media & Services', 'Movies & Entertainment',
                                               'Publishing', 'Wireless Telecommunication Services'],
                    'Information Technology': ['Application Software', 'Communications Equipment',
                                               'Data Processing & Outsourced Services', 'Systems Software'],
                    'Industrials': ['Air Freight & Logistics', 'Human Resource & Employment Services',
                                    'Research & Consulting Services'],
                    'Utilities': ['Renewable Electricity'],
                    'Consumer Discretionary': ['Education Services', 'General Merchandise Stores',
                                               'Hotels, Resorts & Cruise Lines',
                                               'Internet & Direct Marketing Retail',
                                               'Restaurants', 'Specialized Consumer Services'],
                    'Energy': ['Oil & Gas Equipment & Services'],
                    'Financials': ['Financial Exchanges & Data'],
                    'Health Care': ['Health Care Technology'],
                    'Real Estate': ['Real Estate Services']
                    }
    sector_selection = input_sector
    list_subindustry = dict_sectors.get(sector_selection)

    return list_subindustry


def Get_Activities(input_subindustry):
    dict_subindustries = {'Advertising': ['Advertising', 'Marketing', 'Media', 'Social Media',
                                          'Social Networking', 'Strategy', 'Targeting'],
                          'Broadcasting': 'News',
                          'Interactive Home Entertainment': 'Gaming',
                          'Interactive Media & Services': ['Entertainment', 'Market Research'],
                          'Movies & Entertainment': 'Music',
                          'Publishing': 'Publishing',
                          'Wireless Telecommunication Services': 'Telecommunications',
                          'Application Software': ['Cloud Computing', 'Database Management',
                                                   'Enterprise Software', 'Information Management', 'Operations'],
                          'Communications Equipment': ['Classifieds', 'Network / Hosting / Infrastructure',
                                                       'Server Design'],
                          'Data Processing & Outsourced Services': 'Analytics',
                          'Systems Software': ['Security', 'Solution Providing'],
                          'Air Freight & Logistics': 'Transportation',
                          'Human Resource & Employment Services': ['Career / Job Search', 'Human Resources (HR)'],
                          'Research & Consulting Services': 'CRM',
                          'Renewable Electricity': 'CleanTech',
                          'Education Services': 'Education',
                          'General Merchandise Stores': ['Retail', 'Sales'],
                          'Hotels, Resorts & Cruise Lines': ['Space Travel', 'Travel'],
                          'Internet & Direct Marketing Retail': ['E-Commerce', 'Email', 'Mobile'],
                          'Restaurants': 'Food & Beverages',
                          'Specialized Consumer Services': 'Services',
                          'Oil & Gas Equipment & Services': 'Energy',
                          'Financial Exchanges & Data': 'Finance',
                          'Health Care Technology': 'Healthcare',
                          'Real Estate Services': 'Real Estate'
                          }
    subindustry_selection = input_subindustry
    list_activities = dict_subindustries.get(subindustry_selection)
    return list_activities


def Get_Activity_Value(input_activity):
    dict_activities = {'Advertising': 0,
                       'Analytics': 1,
                       'Career / Job Search': 3,
                       'Classifieds': 4,
                       'CleanTech': 5,
                       'Cloud Computing': 6,
                       'CRM': 2,
                       'Database Management': 7,
                       'E-Commerce': 8,
                       'Education': 9,
                       'Email': 10,
                       'Energy': 11,
                       'Enterprise Software': 12,
                       'Entertainment': 13,
                       'Finance': 14,
                       'Food & Beverages': 15,
                       'Gaming': 16,
                       'Healthcare': 17,
                       'Human Resources (HR)': 18,
                       'Information Management': 19,
                       'Market Research': 20,
                       'Marketing': 21,
                       'Media': 22,
                       'Mobile': 23,
                       'Music': 24,
                       'Network / Hosting / Infrastructure': 25,
                       'News': 26,
                       'Operations': 27,
                       'Publishing': 28,
                       'Real Estate': 29,
                       'Retail': 30,
                       'Sales': 31,
                       'Security': 32,
                       'Server Design': 33,
                       'Services': 34,
                       'Social Media': 35,
                       'Social Networking': 36,
                       'Solution Providing': 37,
                       'Space Travel': 38,
                       'Strategy': 39,
                       'Targeting': 40,
                       'Telecommunications': 41,
                       'Transportation': 42,
                       'Travel': 43
                       }
    activity_selection = input_activity
    value_activity = dict_activities.get(activity_selection)
    return value_activity

import csv
import requests
from io import StringIO
import pandas as pd
from datetime import datetime


def kuldeep_data_one():
    # URL of the raw CSV file on GitHub
    url = 'https://github.com/shree7796/indian_player_datasets/raw/main/kuldeep.csv'

    # Download the CSV file
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Read the CSV data from the response content
    csv_data = StringIO(response.text)

    # Parse CSV data into a list of dictionaries
    csv_reader_kuldeep = csv.DictReader(csv_data)
    data_11 = [row for row in csv_reader_kuldeep]

    return data_11


def jasprit_data_one():
    # URL of the raw CSV file on GitHub
    url = 'https://github.com/shree7796/indian_player_datasets/raw/main/jasprit.csv'

    # Download the CSV file
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Read the CSV data from the response content
    csv_data = StringIO(response.text)

    # Parse CSV data into a list of dictionaries
    csv_reader_jasprit = csv.DictReader(csv_data)
    data_11 = [row for row in csv_reader_jasprit]

    return data_11


def shami_data_one():
    # URL of the raw CSV file on GitHub
    url = 'https://github.com/shree7796/indian_player_datasets/raw/main/shami.csv'

    # Download the CSV file
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Read the CSV data from the response content
    csv_data = StringIO(response.text)

    # Parse CSV data into a list of dictionaries
    csv_reader_shami = csv.DictReader(csv_data)
    data_11 = [row for row in csv_reader_shami]

    return data_11


def jadeja_data_one():
    # URL of the raw CSV file on GitHub
    url = 'https://github.com/shree7796/indian_player_datasets/raw/main/jadeja.csv'

    # Download the CSV file
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Read the CSV data from the response content
    csv_data = StringIO(response.text)

    # Parse CSV data into a list of dictionaries
    csv_reader_jadeja = csv.DictReader(csv_data)
    data_11 = [row for row in csv_reader_jadeja]

    return data_11


def hardik_data_one():
    # URL of the raw CSV file on GitHub
    url = 'https://github.com/shree7796/indian_player_datasets/raw/main/hardik.csv'

    # Download the CSV file
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Read the CSV data from the response content
    csv_data = StringIO(response.text)

    # Parse CSV data into a list of dictionaries
    csv_reader_hardik = csv.DictReader(csv_data)
    data_11 = [row for row in csv_reader_hardik]

    return data_11


def sky_data_one():
    # URL of the raw CSV file on GitHub
    url = 'https://github.com/shree7796/indian_player_datasets/raw/main/sky.csv'

    # Download the CSV file
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Read the CSV data from the response content
    csv_data = StringIO(response.text)

    # Parse CSV data into a list of dictionaries
    csv_reader_sky = csv.DictReader(csv_data)
    data_11 = [row for row in csv_reader_sky]

    return data_11


def shreyas_data_one():
    # URL of the raw CSV file on GitHub
    url = 'https://github.com/shree7796/indian_player_datasets/raw/main/shreyas.csv'

    # Download the CSV file
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Read the CSV data from the response content
    csv_data = StringIO(response.text)

    # Parse CSV data into a list of dictionaries
    csv_reader_shreyas = csv.DictReader(csv_data)
    data_11 = [row for row in csv_reader_shreyas]

    return data_11


def shubhman_data_one():
    # URL of the raw CSV file on GitHub
    url = 'https://github.com/shree7796/indian_player_datasets/raw/main/shubhman.csv'

    # Download the CSV file
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Read the CSV data from the response content
    csv_data = StringIO(response.text)

    # Parse CSV data into a list of dictionaries
    csv_reader_gill = csv.DictReader(csv_data)
    data_11 = [row for row in csv_reader_gill]

    return data_11


def kl_dataframe_one():
    # URL of the raw CSV file on GitHub
    url = 'https://github.com/shree7796/indian_player_datasets/raw/main/kl_rahul.csv'

    # Download the CSV file
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Read the CSV data from the response content
    csv_data = StringIO(response.text)

    # Parse CSV data into a list of dictionaries
    csv_reader_kl = csv.DictReader(csv_data)
    data_11 = [row for row in csv_reader_kl]

    return data_11


def rohit_data_one():
    # URL of the raw CSV file on GitHub
    url = 'https://github.com/shree7796/indian_player_datasets/raw/main/ODI.csv'

    # Download the CSV file
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Read the CSV data from the response content
    csv_data = StringIO(response.text)

    # Parse CSV data into a list of dictionaries
    csv_reader_rohit = csv.DictReader(csv_data)
    data_11 = [row for row in csv_reader_rohit]

    return data_11


def virat_data():
    # URL of the raw CSV file on GitHub
    url = 'https://github.com/shree7796/indian_player_datasets/raw/main/Virat_Kohli.csv'

    # Download the CSV file
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Read the CSV data from the response content
    csv_data = StringIO(response.text)

    # Parse CSV data into a list of dictionaries
    csv_reader_virat = csv.DictReader(csv_data)
    data_11 = [row for row in csv_reader_virat]

    return data_11


# Dataframe for all players

def virat_dataframe():
    # Virat Kohli Start========>
    data_11 = virat_data()
    # Sort the data by date
    sorted_data = sorted(data_11, key=lambda x: datetime.strptime(x['Start Date'], '%d-%b-%y'))

    # Get last 5 Match data
    grounds = [match['Ground'] if match.get('Ground') else "" for match in sorted_data]
    grounds = grounds[-5:]

    match_date = [match['Start Date'] if match.get('Start Date') else "" for match in sorted_data]
    match_date = match_date[-5:]

    runs = [int(runs['Runs']) if runs.get('Runs') else 0 for runs in sorted_data]
    runs = runs[-5:]

    fours = [int(fours['4s']) if fours.get('4s') else 0 for fours in sorted_data]
    fours = fours[-5:]

    six = [int(sixs['6s']) if sixs.get('6s') else 0 for sixs in sorted_data]
    six = six[-5:]

    df = pd.DataFrame({
        'Ground': grounds,
        'Start Date': match_date,
        'Runs': runs,
        '4s': fours,
        '6s': six
    })
    # Virat Kohli End========>
    return df


# Rohit Sharma Start========>
def rohit_dataframe():
    rohit_data = rohit_data_one()
    # Get last 5 Years Performance
    for i in range(len(rohit_data)):
        if rohit_data[i].get("Year") == "Total":
            del rohit_data[i]

    ro_years = [match['Year'] if match.get('Year')!="Total" else "" for match in rohit_data]
    ro_years = ro_years

    rohit_runs = [int(match['Runs']) if match.get('Runs') else "" for match in rohit_data]
    rohit_runs = rohit_runs

    rohit_fours = [int(fours['4s']) if fours.get('4s') else 0 for fours in rohit_data]
    rohit_fours = rohit_fours

    rohit_six = [int(sixs['6s']) if sixs.get('6s') else 0 for sixs in rohit_data]
    rohit_six = rohit_six

    return pd.DataFrame({
        'Years': ro_years,
        'Runs': rohit_runs,
        '4s': rohit_fours,
        '6s': rohit_six
    })
# Rohit Sharma End========>


# KL Rahul Start========>
def kl_rahul_dataframe():
    kl_rahul_data = kl_dataframe_one()
    # Get last 5 Years Performance
    for i in range(len(kl_rahul_data)):
        if kl_rahul_data[i].get("Year") == "Total":
            del kl_rahul_data[i]

    kl_years = [int(match['Year']) if match.get('Year')!="Total" else "" for match in kl_rahul_data]
    kl_years = kl_years

    kl_runs = [int(match['Runs']) if match.get('Runs') else "" for match in kl_rahul_data]
    kl_runs = kl_runs

    kl_100s = [int(fours['100s']) if fours.get('100s') else 0 for fours in kl_rahul_data]
    kl_100s = kl_100s

    kl_50s = [int(sixs['50s']) if sixs.get('50s') else 0 for sixs in kl_rahul_data]
    kl_50s = kl_50s

    return pd.DataFrame({
        'Year': kl_years,
        'Runs': kl_runs,
        '100s': kl_100s,
        '50s': kl_50s
    })
# KL Rahul End========>


# Shubhman Start========>
def shubhman_dataframe():
    shubhman_data = shubhman_data_one()
    # Get last 5 Years Performance
    for i in range(len(shubhman_data)):
        if shubhman_data[i].get("Year") == "Total":
            del shubhman_data[i]

    shubhman_years = [int(match['Year']) if match.get('Year')!="Total" else "" for match in shubhman_data]
    shubhman_years = shubhman_years

    shubhman_runs = [int(match['Runs']) if match.get('Runs') else "" for match in shubhman_data]
    shubhman_runs = shubhman_runs

    shubhman_100s = [int(fours['100s']) if fours.get('100s') else 0 for fours in shubhman_data]
    shubhman_100s = shubhman_100s

    shubhman_50s = [int(sixs['50s']) if sixs.get('50s') else 0 for sixs in shubhman_data]
    shubhman_50s = shubhman_50s

    return pd.DataFrame({
        'Year': shubhman_years,
        'Runs': shubhman_runs,
        '100s': shubhman_100s,
        '50s': shubhman_50s
    })
# Shubhman End========>


# Shreyas Start========>
def shreyas_data_dataframe():
    shreyas_data = shreyas_data_one()
    for i in range(len(shreyas_data)):
        if shreyas_data[i].get("Year") == "Total":
            del shreyas_data[i]

    shreyas_data_years = [int(match['Year']) if match.get('Year')!="Total" else "" for match in shreyas_data]
    shreyas_data_years = shreyas_data_years

    shreyas_data_runs = [int(match['Runs']) if match.get('Runs') else "" for match in shreyas_data]
    shreyas_data_runs = shreyas_data_runs

    shreyas_data_100s = [int(fours['100s']) if fours.get('100s') else 0 for fours in shreyas_data]
    shreyas_data_100s = shreyas_data_100s

    shreyas_data_50s = [int(sixs['50s']) if sixs.get('50s') else 0 for sixs in shreyas_data]
    shreyas_data_50s = shreyas_data_50s

    return pd.DataFrame({
        'Year': shreyas_data_years,
        'Runs': shreyas_data_runs,
        '100s': shreyas_data_100s,
        '50s': shreyas_data_50s
    })
# Shreyas End========>


# SKY Start========>
def sky_data_dataframe():
    sky_data = sky_data_one()
    # Get last 5 Years Performance
    for i in range(len(sky_data)):
        if sky_data[i].get("Year") == "Total":
            del sky_data[i]

    sky_years = [int(match['Year']) if match.get('Year')!="Total" else "" for match in sky_data]
    sky_years = sky_years

    sky_runs = [int(match['Runs']) if match.get('Runs') else "" for match in sky_data]
    sky_runs = sky_runs

    sky_100s = [int(fours['100s']) if fours.get('100s') else 0 for fours in sky_data]
    sky_100s = sky_100s

    sky_50s = [int(sixs['50s']) if sixs.get('50s') else 0 for sixs in sky_data]
    sky_50s = sky_50s

    return pd.DataFrame({
        'Year': sky_years,
        'Runs': sky_runs,
        '100s': sky_100s,
        '50s': sky_50s
    })
# SKY End========>


# Hardik Start========>
def hardik_data_dataframe():
    hardik_data = hardik_data_one()
    # Get last 5 Years Performance
    for i in range(len(hardik_data)):
        if hardik_data[i].get("Year") == "Total":
            del hardik_data[i]

    hardik_years = [int(match['Year']) if match.get('Year')!="Total" else "" for match in hardik_data]
    hardik_years = hardik_years

    hardik_runs = [int(match['Runs']) if match.get('Runs') else "" for match in hardik_data]
    hardik_runs = hardik_runs

    hardik_100s = [int(fours['100s']) if fours.get('100s') else 0 for fours in hardik_data]
    hardik_100s = hardik_100s

    hardik_50s = [int(sixs['50s']) if sixs.get('50s') else 0 for sixs in hardik_data]
    hardik_50s = hardik_50s

    return pd.DataFrame({
        'Year': hardik_years,
        'Runs': hardik_runs,
        '100s': hardik_100s,
        '50s': hardik_50s
    })
# Hardik End========>


# Jadeja Start========>
def jadeja_data_dataframe():
    jadeja_data = jadeja_data_one()
    # Get last 5 Years Performance
    for i in range(len(jadeja_data)):
        if jadeja_data[i].get("Year") == "Total":
            del jadeja_data[i]

    jadeja_years = [int(match['Year']) if match.get('Year')!="Total" else "" for match in jadeja_data]
    jadeja_years = jadeja_years

    jadeja_runs = [int(match['Runs']) if match.get('Runs') else "" for match in jadeja_data]
    jadeja_runs = jadeja_runs

    jadeja_100s = [int(fours['100s']) if fours.get('100s') else 0 for fours in jadeja_data]
    jadeja_100s = jadeja_100s

    jadeja_50s = [int(sixs['50s']) if sixs.get('50s') else 0 for sixs in jadeja_data]
    jadeja_50s = jadeja_50s

    return pd.DataFrame({
        'Year': jadeja_years,
        'Runs': jadeja_runs,
        '100s': jadeja_100s,
        '50s': jadeja_50s
    })
# Jadeja End========>


# Shami Start========>
def shami_data_dataframe():
    shami_data = shami_data_one()
    # Get last 5 Years Performance
    for i in range(len(shami_data)):
        if shami_data[i].get("Year") == "Total":
            del shami_data[i]

    shami_years = [int(match['Year']) if match.get('Year')!="Total" else "" for match in shami_data]
    shami_years = shami_years

    shami_runs = [int(match['R']) if match.get('R') else "" for match in shami_data]
    shami_runs = shami_runs

    shami_wickets = [int(fours['W']) if fours.get('W') else 0 for fours in shami_data]
    shami_wickets = shami_wickets

    shami_4wickets = [int(sixs['4W']) if sixs.get('4W') else 0 for sixs in shami_data]
    shami_4wickets = shami_4wickets

    return pd.DataFrame({
        'Year': shami_years,
        'Runs': shami_runs,
        'shami_wickets': shami_wickets,
        'shami_4wickets': shami_4wickets
})
# Shami End========>


# Jasprit Start========>
def jasprit_data_dataframe():
    jasprit_data = jasprit_data_one()
    # Get last 5 Years Performance
    for i in range(len(jasprit_data)):
        if jasprit_data[i].get("Year") == "Total":
            del jasprit_data[i]

    jasprit_years = [int(match['Year']) if match.get('Year')!="Total" else "" for match in jasprit_data]
    jasprit_years = jasprit_years

    jasprit_runs = [int(match['R']) if match.get('R') else "" for match in jasprit_data]
    jasprit_runs = jasprit_runs

    jasprit_wickets = [int(fours['W']) if fours.get('W') else 0 for fours in jasprit_data]
    jasprit_wickets = jasprit_wickets

    jasprit_4wickets = [int(sixs['4W']) if sixs.get('4W') else 0 for sixs in jasprit_data]
    jasprit_4wickets = jasprit_4wickets

    return pd.DataFrame({
        'Year': jasprit_years,
        'Runs': jasprit_runs,
        'jasprit_wickets': jasprit_wickets,
        'jasprit_4wickets': jasprit_4wickets
    })
# Jasprit End========>


# Kuldeep Start========>
def kuldeep_data_dataframe():
    kuldeep_data = kuldeep_data_one()
    # Get last 5 Years Performance
    for i in range(len(kuldeep_data)):
        if kuldeep_data[i].get("Year") == "Total":
            del kuldeep_data[i]

    kuldeep_years = [int(match['Year']) if match.get('Year')!="Total" else "" for match in kuldeep_data]
    kuldeep_years = kuldeep_years

    kuldeep_runs = [int(match['R']) if match.get('R') else "" for match in kuldeep_data]
    kuldeep_runs = kuldeep_runs

    kuldeep_wickets = [int(fours['W']) if fours.get('W') else 0 for fours in kuldeep_data]
    kuldeep_wickets = kuldeep_wickets

    kuldeep_4wickets = [int(sixs['4W']) if sixs.get('4W') else 0 for sixs in kuldeep_data]
    kuldeep_4wickets = kuldeep_4wickets

    return pd.DataFrame({
        'Year': kuldeep_years,
        'Runs': kuldeep_runs,
        'kuldeep_wickets': kuldeep_wickets,
        'kuldeep_4wickets': kuldeep_4wickets
    })
# Kuldeep End========>


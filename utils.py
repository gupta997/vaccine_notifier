import configparser, requests, logging


def create_logger(filename):
    """
    instantiate a logger object
    :param filename:
    :return:
    """
    logging.basicConfig(filename=filename,
                        format='%(asctime)s %(levelname)s %(message)s',
                        filemode='a')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    return logger


def read_configs_file(filepath):
    """
    Read the inputs provided by user in user_input.cfg file
    :return:
    """
    config_file = {f'{filepath}/user_input.cfg': ['DEFAULT', 'REQUIRED', 'OPTIONAL', 'TWILIO']}
    config_parser = configparser.ConfigParser()
    config_parser.optionxform = str

    for file_path, sections in config_file.items():
        config_parser.read(file_path)
        config = {s: dict(config_parser.items(s)) for s in config_parser.sections()}
        config_dict = {**config['REQUIRED'], **config['OPTIONAL'], **config['TWILIO']}

    return config_dict


def get_districts():
    # state_id 12 is for haryana, change for different states
    state_id = 12
    url_district = f'https://cdn-api.co-vin.in/api/v2/admin/location/districts/{state_id}'
    districts = requests.get(url_district, headers=headers).json()
    with open('district_id.json', 'w') as f:
        f.write(districts.text)


def get_state_ids():
    """

    :return:
    """
    url_states = 'https://cdn-api.co-vin.in/api/v2/admin/location/states'
    states = requests.get(url_states, headers=headers).json()
    with open('state_id.json', 'w') as f:
        f.write(states.text)

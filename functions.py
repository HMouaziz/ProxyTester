import csv
import time
import requests
from requests import RequestException


def progress_bar(iterable, prefix='', suffix='', decimals=1, length=100, fill='█', print_end="\r"):
    """
        Call in a loop to create terminal progress bar
        @params:
            iterable    - Required  : iterable object (Iterable)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
    total = len(iterable)

    def print_progress_bar(iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
    # Initial Call
    print_progress_bar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        print_progress_bar(i + 1)
    # Print New Line on Complete
    print()


def get_geonode_configs():  # gets all configs in configs file
    config_list = []
    for line in open("Configs/geonode_proxy_configs.py"):
        if "geonode" and "_config():" in line:
            temp = line.strip()
            temp = (temp.replace('def ', ''))
            config_name = (temp.replace('():', ''))
            config_list.append(config_name)
        else:
            pass
    return config_list


def get_targets(amount):
    num = amount
    with open('data/2022-01-04-halim-75000-random-store-urls.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 1
        target_list = []
        next(csv_reader)
        for row in csv_reader:
            if line_count <= num:
                target_list.append(row[1])
                line_count += 1
            else:
                return target_list


def run_simple_speed_test(test_list):
    for i in test_list:
        row_start = time.perf_counter()
        print(i["Config_Name"])
        response = make_geonode_get_request_for_simple(i["Target"], i["Config"])
        row_timer = time.perf_counter() - row_start
        if not response:
            i["Test_Result"] = row_timer
            print("Individual time:", row_timer, "second(s)\n")
        else:
            i["Test_Result"] = None
    return test_list


def run_speed_comparison_test(test_list):
    for i in progress_bar(test_list, prefix="Progress", suffix='Complete', length=50):
        row_start = time.perf_counter()
        response = make_geonode_get_request_for_comparison(i["Target"], i["Config"])
        row_timer = time.perf_counter() - row_start
        time.sleep(0.01)
        if not response:
            i["Test_Result"] = row_timer
        else:
            i["Test_Result"] = 0.0
    return test_list


def make_test_data_container(target, config_name, config):
    tdc = {"Target": target,
           "Config_Name": config_name,
           "Config": config,
           "Test_Result": None,
           }
    return tdc


def write_report(test_list_data, config_list):
    header = ["Config Name", "Total Time(in seconds)", "Average Time(in seconds)"]
    try:
        with open("Comparison Test Report.csv", "w", encoding="UTF8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            for i in config_list:
                results = []
                for x in test_list_data:
                    instance = []
                    if x["Config_Name"] == i:
                        results.append(x["Test_Result"])
                        total_time = sum(map(float, results))
                    else:
                        pass
                instance.append(i)
                instance.append(total_time)
                instance.append(total_time / len(results))
                writer.writerow(instance)
    except PermissionError:
        print("Please close the Comparison Test Report file before running the test again")


# Could be universal I just don't know yet as I haven't implemented support for other APIs
def make_geonode_get_request_for_simple(url_to_get, proxy):
    try:
        requests.get(url_to_get, proxies=proxy)
        response = False
    except RequestException as e:
        if isinstance(e, RequestException):
            response = True
            print("Encountered a RequestException error.\n")
        else:
            response = True
            print("Encountered an unexpected error.\n")
    return response


def make_geonode_get_request_for_comparison(url_to_get, proxy):
    try:
        requests.get(url_to_get, proxies=proxy)
        response = False
    except RequestException as e:
        if isinstance(e, RequestException):
            response = True
        else:
            response = True
    return response


from InquirerPy import inquirer
from Configs import geonode_proxy_configs
from functions import get_targets, run_simple_speed_test, run_speed_comparison_test, make_test_data_container, \
    write_report


def run_simple_speed_test_handler(test_list):
    results = []
    post_test_list = run_simple_speed_test(test_list)
    for i in post_test_list:
        if i["Test_Result"] is not None:
            results.append(i["Test_Result"])
        else:
            pass
    total_time = sum(map(float, results))
    print("Total total_time:", total_time, "Second(s)")
    print("Average total_time per url:", (total_time / len(results)), "Second(s)")


def run_speed_comparison_test_handler(test_list, config_list):
    data = run_speed_comparison_test(test_list)
    for i in config_list:
        results = []
        for x in data:
            if x["Config_Name"] == i:
                results.append(x["Test_Result"])
            else:
                pass
        total_time = sum(map(float, results))
        print("Total time for", i, "=", total_time, "second(s)")
        print("Average time for", i, "=", (total_time / len(results)), "\n")
    confirm = inquirer.confirm(message="would you like to generate a CSV report", default=True).execute()
    if confirm is True:
        write_report(data, config_list)
        print("Generating CSV Report")
    else:
        pass


def get_test_list(config_list, amount):
    test_list = []
    target_list = get_targets(amount)
    for c in config_list:
        get_config = getattr(geonode_proxy_configs, c)
        config = get_config()
        for i in target_list:
            test_list.append(make_test_data_container(target=i, config_name=c, config=config))
    return test_list

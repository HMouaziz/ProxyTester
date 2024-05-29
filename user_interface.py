import sys
from InquirerPy import inquirer
from InquirerPy.base import Choice
from functions import get_geonode_configs
from operations import run_simple_speed_test_handler, run_speed_comparison_test_handler, get_test_list


def menu_ui(message):
    if message is None:
        message = "Menu:"
    test_type = None
    while test_type is None:
        test_type = inquirer.select(
            message=message,
            choices=["Run simple proxy speed test",
                     "Run proxy speed comparison test",
                     Choice(value="Exit", name="Exit"), ],
            default=None,
        ).execute()
        if test_type == "Run simple proxy speed test":
            _simple_speed_test_ui()
            break
        elif test_type == "Run proxy speed comparison test":
            _speed_comparison_test_ui()
            break
        elif test_type == "Exit":
            print("Exiting...")
            sys.exit(1)


def _simple_speed_test_ui():
    proxy_config = None
    config_list = []
    while proxy_config is None:
        proxy = inquirer.select(
            message="Which Proxy do you want to test?",
            choices=["Configs Proxy",
                     "Proxy2",
                     "Proxy3",
                     "Proxy4",
                     Choice(value=None, name="Back"), ],
            default=None,
        ).execute()
        if proxy == "Configs Proxy":
            choices = get_geonode_configs()
            choices.append(Choice(value=None, name="Back"))
            proxy_config = inquirer.select(
                message="Which Config do you want to run?",
                choices=choices,
                default=None,
            ).execute()
            if proxy_config is not None:
                try:
                    amount = int(input("Please enter the amount of urls you would like to test:"))
                except ValueError:
                    amount = int(input("Enter an integer you blithering idiot! :"))
                config_list.append(proxy_config)
                test_list = get_test_list(config_list, amount)
                print("Running simple speed test on", amount, "urls.")
                run_simple_speed_test_handler(test_list)
                menu_ui(None)
                break
            else:
                pass
        elif proxy == "Proxy2":
            print("Proxy2 is a placeholder.")
        elif proxy == "Proxy3":
            print("Proxy3 is a placeholder.")
        elif proxy == "Proxy4":
            print("Proxy4 is a placeholder.")
        elif proxy is None:
            menu_ui(None)


# modifications required to test different proxy services
def _speed_comparison_test_ui():
    confirm = False
    while confirm is False:
        config_list = inquirer.checkbox(
            message="Select the configurations you want to compare:",
            choices=get_geonode_configs(),
            validate=lambda result: len(result) >= 2,
            invalid_message="You must select at least 2 configs",
            transformer=lambda result: "%s configs selected" % (len(result),),
            instruction=" Use (space) to select & (enter) to confirm."
        ).execute()
        print("Selected configs:")
        for i in range(len(config_list)):
            print(config_list[i])
        try:
            amount = int(input("Please enter the amount of urls you would like to test: "))
        except ValueError:
            amount = int(input("Enter an integer you blithering idiot! : "))
        confirm = inquirer.confirm(message="Confirm?", default=True).execute()
        test_list = get_test_list(config_list, amount)
        if confirm is True:
            run_speed_comparison_test_handler(test_list, config_list)
            menu_ui(None)
            break
        else:
            pass

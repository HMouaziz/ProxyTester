def geonode_US_rotating_residential_unmetered_config():
    username = "geonode_'replace-me-with-user'-country-US"
    password = "replace_with_secret_key"
    GEONODE_DNS = "rotating-residential.geonode.com:9000"
    proxy_config = {"http":"http://{}:{}@{}".format(username, password, GEONODE_DNS)}

    return proxy_config


def geonode_US_rotating_residential_unmetered_auto_replace_session_config():
    username = "geonode_'replace-me-with-user'-country-US-autoReplace-True"
    password = "replace_with_secret_key"
    GEONODE_DNS = "rotating-residential.geonode.com:9000"
    proxy_config = {"http":"http://{}:{}@{}".format(username, password, GEONODE_DNS)}

    return proxy_config

def geonode_US_static_residential_unmetered_config():
    username = "geonode_'replace-me-with-user'-country-US"
    password = "replace_with_secret_key"
    GEONODE_DNS = "rotating-residential.geonode.com:10000"
    proxy_config = {"http": "http://{}:{}@{}".format(username, password, GEONODE_DNS)}

    return proxy_config


def geonode_US_static_residential_unmetered_auto_replace_session_config():
    username = "geonode_'replace-me-with-user'-country-US-autoReplace-True"
    password = "replace_with_secret_key"
    GEONODE_DNS = "rotating-residential.geonode.com:10000"
    proxy_config = {"http": "http://{}:{}@{}".format(username, password, GEONODE_DNS)}

    return proxy_config


def geonode_US_residential_private_config():
    username = "geonode_'replace-me-with-user'-country-US"
    password = "replace_with_secret_key"
    GEONODE_DNS = "private-residential.geonode.com:10000"
    proxy_config = {"http": "http://{}:{}@{}".format(username, password, GEONODE_DNS)}

    return proxy_config


def geonode_US_residential_private_auto_replace_session_config():
    username = "geonode_'replace-me-with-user'-country-US-autoReplace-True"
    password = "replace_with_secret_key"
    GEONODE_DNS = "private-residential.geonode.com:10000"
    proxy_config = {"http": "http://{}:{}@{}".format(username, password, GEONODE_DNS)}

    return proxy_config


def geonode_US_rotating_residential_premium_config():
    username = "geonode_'replace-me-with-user'-country-US"
    password = "replace_with_secret_key"
    GEONODE_DNS = "premium-residential.geonode.com:9000"
    proxy_config = {"http": "http://{}:{}@{}".format(username, password, GEONODE_DNS)}

    return proxy_config


def geonode_US_rotating_residential_premium_auto_replace_session_config():
    username = "geonode_'replace-me-with-user'-country-US-autoReplace-True"
    password = "replace_with_secret_key"
    GEONODE_DNS = "premium-residential.geonode.com:9000"
    proxy_config = {"http": "http://{}:{}@{}".format(username, password, GEONODE_DNS)}

    return proxy_config


def geonode_US_static_residential_premium_config():
    username = "geonode_'replace-me-with-user'-country-US"
    password = "replace_with_secret_key"
    GEONODE_DNS = "premium-residential.geonode.com:10000"
    proxy_config = {"http": "http://{}:{}@{}".format(username, password, GEONODE_DNS)}

    return proxy_config


def geonode_US_static_residential_premium_auto_replace_session_config():
    username = "geonode_'replace-me-with-user'-country-US-autoReplace-True"
    password = "replace_with_secret_key"
    GEONODE_DNS = "premium-residential.geonode.com:10000"
    proxy_config = {"http": "http://{}:{}@{}".format(username, password, GEONODE_DNS)}

    return proxy_config

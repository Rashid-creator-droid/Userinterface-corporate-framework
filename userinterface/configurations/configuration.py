from integration_template.configurations.environment import Environment


class Configuration:

    @classmethod
    def start_url(cls):
        return Environment.current_environment().get("startUrl")

    @classmethod
    def api_url(cls):
        return Environment.current_environment().get("apiUrl")
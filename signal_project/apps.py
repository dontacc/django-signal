from django.apps import AppConfig


class SignalProjectConfig(AppConfig):
    name = 'signal_project'


    def ready(self):
        import signal_project.signals
  
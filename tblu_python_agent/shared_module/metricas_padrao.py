from .metricas_adapter.entity.metrica_entity import Metrica


class MetricasPadrao:
    def __init__(self, component):
        self.component = component
        self.update = Metrica(componenteUUID=self.component,
                              metricaUUID="b514af82-3c4f-4bb5-b1da-a89a0ced5e6f",
                              module="tblu_python_agent.internal.metric_update",
                              cron="* * * * *")

    def getAll(self):
        return [self.update]

    def getUpdate(self):
        return self.update

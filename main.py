

dic = {
    "name" : "iniciar.calculo.hdp",
    "owner" : "anonymous",
    "payload" : {
        "UnidadeGeradora" : {
            "UnidadeGeradoraId" : "1",
            "UsinaId" : "1",
            "DataEntradaOperacao" : "2019-01-01T00:00:00",
            "DataEventoEOC" : "2019-01-01T00:00:00",
            "Potencias" : [
                {
                    "DataInicio" : "0001-01-01T00:00:00",
                    "ValorPotencia" : 350.0
                }
            ]
        },
        "SuspensoesUnidadeGeradora" : [
            {
                "UnidadeGeradoraId" : "1",
                "DataInicio" : "2019-01-29T00:00:00"
            },
            {
                "UnidadeGeradoraId" : "2",
                "DataInicio" : "2019-01-29T00:00:00"
            },
            {
                "UnidadeGeradoraId" : "3",
                "DataInicio" : "2019-01-29T00:00:00"
            }
        ],
        "Eventos" : [
            {
                "DataVerificada" : "2019-01-01T00:00:00",
                "EstadoOperativoId" : "DAP",
                "CondicaoOperativaId" : "",
                "OrigemId" : "GAC",
                "StatusEvento" : "AGE",
                "Disponibilidade" : 0.0
            },
            {
                "DataVerificada" : "2019-01-06T00:00:00",
                "EstadoOperativoId" : "DPR",
                "CondicaoOperativaId" : "",
                "OrigemId" : "GUM",
                "StatusEvento" : "AGE",
                "Disponibilidade" : 0.0
            },
            {
                "DataVerificada" : "2019-01-29T00:00:00",
                "EstadoOperativoId" : "DCA",
                "CondicaoOperativaId" : "",
                "OrigemId" : "GCB",
                "StatusEvento" : "AGE",
                "Disponibilidade" : 0.0
            },
            {
                "DataVerificada" : "2019-01-31T00:00:00",
                "EstadoOperativoId" : "DAP",
                "CondicaoOperativaId" : "",
                "OrigemId" : "GAC",
                "StatusEvento" : "AGE",
                "Disponibilidade" : 0.0
            }
        ],
        "ControleCalculoId" : "1",
        "ConfiguracaoCenarioId" : "1",
        "ConsolidacaoPeriodoApuracaoId" : "1",
        "DataReferencia" : "2019-01-01T00:00:00"
    },
    "reproduction" : {},
    "scope" : "execution",
    "tag" : None,
    "timestamp" : "2019-03-14T00:00:00"
}


from runner import settings
from sdk.models import Event
import pdb;pdb.set_trace()
event = Event(**dic)
settings.PROCESSOR.process(event)
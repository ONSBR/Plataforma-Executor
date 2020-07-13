from sdk.utils import HttpClient, log
from sdk import settings
from datetime import datetime


def get_app_version(reference_date, processId):        
    return get_appversion_by_validity(processId, reference_date)


def get_appversion_by_validity(process_id, date):
    result = HttpClient.get(_get_appversion_byname_and_date_uri(process_id, date))
    if not result.has_error:
        return result.data


def _get_appversion_byname_and_date_uri(process_id, date):
    return '{}:{}/api/v1/appversion/byprocessidanddate/{}/{}'.format(settings.SCHEMA_URL, settings.SCHEMA_PORT,
                                                                     process_id, date)

from sdk.utils import HttpClient, log
from sdk import settings
from datetime import datetime


def get_app_version(reference_date, processId):
    date_format = '%Y-%m-%d %H:%M:%S.%fZ'
    date_format_return = '%Y-%m-%dT%H:%M:%S.%fZ'
    if reference_date:
        reference_date = datetime.strptime(reference_date, date_format_return)
        referenceDate = reference_date.date().strftime(date_format)
    else:
        referenceDate = datetime.today().strftime(date_format)

    return get_appversion_by_validity(processId, referenceDate)


def get_appversion_by_validity(process_id, date):
    result = HttpClient.get(_get_appversion_byname_and_date_uri(process_id, date))
    if not result.has_error:
        return result.data


def _get_appversion_byname_and_date_uri(process_id, date):
    return '{}:{}/api/v1/appversion/byprocessidanddate/{}/{}'.format(settings.SCHEMA_URL, settings.SCHEMA_PORT,
                                                                     process_id, date)

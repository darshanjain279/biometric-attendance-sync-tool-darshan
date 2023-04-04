
# ERPNext related configs
ERPNEXT_API_KEY = 'c39a9ada7d2e847'
ERPNEXT_API_SECRET = '69bb014336c6496'
ERPNEXT_URL = 'http://192.168.181.133:8000/'
ERPNEXT_VERSION = 14

# operational configs
PULL_FREQUENCY = 1 # in minutes
LOGS_DIRECTORY = 'logs' # logs of this script is stored in this directory
IMPORT_START_DATE = '20230101' # format: '20190501'

# Biometric device configs (all keys mandatory)
    #- device_id - must be unique, strictly alphanumerical chars only. no space allowed.
    #- ip - device IP Address
    #- punch_direction - 'IN'/'OUT'/'AUTO'/None
    #- clear_from_device_on_fetch: if set to true then attendance is deleted after fetch is successful.
                                    #(Caution: this feature can lead to data loss if used carelessly.)
devices = [
    {'device_id':'1','ip':'192.168.0.168', 'punch_direction': 'AUTO', 'clear_from_device_on_fetch': False},
    {'device_id':'2','ip':'192.168.0.100', 'punch_direction': 'AUTO', 'clear_from_device_on_fetch': False}
]

# Configs updating sync timestamp in the Shift Type DocType
shift_type_device_mapping = [
    {'shift_type_name': ['Shift1'], 'related_device_id': ['1','2']}
]

from p4utils.utils.helper import load_topo
from p4utils.utils.sswitch_p4runtime_API import SimpleSwitchP4RuntimeAPI


topo = load_topo('topology.json')
controllers = {}

for switch, data in topo.get_p4rtswitches().items():
    controllers[switch] = SimpleSwitchP4RuntimeAPI(data['device_id'], data['grpc_port'],
                                                  p4rt_path=data['p4rt_path'],
                                                  json_path=data['json_path'])

controller = controllers['s1']                        

# On vide la table, dans le doute
controller.table_clear('t')

# On ajoute les données de la table
controller.table_add('t', 'forward', ['1'], ['2'])
controller.table_add('t', 'forward', ['2'], ['1'])

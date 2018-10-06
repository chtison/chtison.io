""" Create a kubernetes cluster """

def GenerateConfig(context):
	oauthScopes = [
		'https://www.googleapis.com/auth/devstorage.read_only',
	]
	resources = [{
		'name': context.env['deployment'] + '-' + context.env['name'],
		'type': 'container.v1.cluster',
		'properties': {
			'zone': 'europe-west1-d',
			'cluster': {
				'initialClusterVersion': '1.10.7-gke.2',
				'masterAuth': {'username': ''},
				'nodePools': [{
					'name': 'very-low-cost',
					'initialNodeCount': 3,
					'config': {
						'machineType': 'f1-micro',
						'preemptible': True,
						'diskSizeGb': 10,
						'oauthScopes': oauthScopes,
					},
					'management': {
						'autoUpgrade': True,
						'autoRepair': True,
					},
				}],
			},
		},
	}]
	return {'resources': resources}

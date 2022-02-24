datos = {
	'clientes': [
		{
			"_id": "0001",
			"nombre": "Juan Carlos",
			"apellido": "Gonzalez",
			"domicilio": "Paz 1330",
			"tarjetas_credito": [
				{
					"tarjeta": "VISA",
					"numero": "293 392 210",
					"clave": "0882"
				},
				{
					"tarjeta": "MASTERCARD",
					"numero": "228 726 156 432",
					"clave": "7623"
				}
			]            
		},
		{
			"_id": "0002",
			"nombre": "Roberto",
			"apellido": "Gonzalez",
			"domicilio": "Mitre 100",
			"tarjetas_credito": [
				{
					"tarjeta": "VISA",
					"numero": "140 287 210",
					"clave": "0129"
				},
				{
					"tarjeta": "VISA",
					"numero": "190 219 241",
					"clave": "2734"
				}
			]            
		},
		{
			"_id": "0003",
			"nombre": "Mariana",
			"apellido": "Gomez",
			"domicilio": "11 de Septiembre 241",
			"tarjetas_credito": [
				{
					"tarjeta": "NARANJA",
					"numero": "440 187 254 876",
					"clave": "5792"
				}
			]            
		},
		{
			"_id": "0004",
			"nombre": "Mariano",
			"apellido": "Martinez",
			"domicilio": "San Lorenzo 720",
			"tarjetas_credito": [
				{
					"tarjeta": "VISA",
					"numero": "110 222 030",
					"clave": "0882"
				},
				{
					"tarjeta": "AMERICAN EXPRESS",
					"numero": "114 570 156 310",
					"clave": "723"
				}
			]            
		},
		{
			"_id": "0005",
			"nombre": "Marcos",
			"apellido": "Paz",
			"domicilio": "Maipu 1460",
			"tarjetas_credito": [
				{
					"tarjeta": "VISA",
					"numero": "309 236 723",
					"clave": "3211"
				}
			]            
		},
		{
			"_id": "0006",
			"nombre": "Angela",
			"apellido": "Romero",
			"domicilio": "Belgrano 1410",
			"tarjetas_credito": [
				{
					"tarjeta": "AMERICAN EXPRESS",
					"numero": "160 020 615 013",
					"clave": "183"
				}
			]            
		},
	],
	'productos': [
		{
			"_id": "0001",
			"producto": "Notebook Lenovo INTEL",
			"exitencias": 4,
			"exitencias_minimas": 2,
			"precio": {
				"moneda": "ARG",
				"simbolo": "$",
				"importe": 26510
			},
			"categorias": ["Notebook"]
		},
		{
			"_id": "0002",
			"producto": "Monitor Curvo Samsung Cf398 27 In Fhd",
			"exitencias": 10,
			"exitencias_minimas": 4,
			"precio": {
				"moneda": "ARG",
				"simbolo": "$",
				"importe": 11600
			},
			"categorias": ["Monitor", "PC"]
		},
		{
			"_id": "0003",
			"producto": "Benq Zowie Xl2411p 24",
			"exitencias": 1,
			"exitencias_minimas": 8,
			"precio": {
				"moneda": "U$s US",
				"simbolo": "U$s",
				"importe": 280
			},
			"categorias": ["Monitor", "PC"]            
		},
		{
			"_id": "0004",
			"producto": "Monitor Pc Gamer 19 Philips Panel 5ms Hdmi",
			"exitencias": 4,
			"exitencias_minimas": 10,
			"precio": {
				"moneda": "U$s US",
				"simbolo": "U$s",
				"importe": 210
			},
			"categorias": ["Monitor", "PC"]
		},
		{
			"_id": "0005",
			"producto": "Computadora Completa Dual Core 4gb Ddr3 - Monitor",
			"exitencias": 4,
			"exitencias_minimas": 4,
			"precio": {
				"moneda": "ARG",
				"simbolo": "$",
				"importe": 8999
			},
			"categorias": ["PC"]
		},
		{
			"_id": "0006",
			"producto": "Notebook Intel Netbook Cloudbook 32gb Ssd 2gb Ram Windows 10",
			"exitencias": 10,
			"exitencias_minimas": 4,
			"precio": {
				"moneda": "ARG",
				"simbolo": "$",
				"importe": 10999
			},
			"categorias": ["Notebook"]
		},
		{
			"_id": "0007",
			"producto": "Notebook Lenovo V330 Intel Core I3 8va 4gb + 1tb Windows 10",
			"exitencias": 3,
			"exitencias_minimas": 5,
			"precio": {
				"moneda": "ARG",
				"simbolo": "$",
				"importe": 21499
			},
			"categorias": ["Notebook"]
		}
	],
	'carritos': [
		{
			"fecha": '2018-11-28 23:55:59',
			"finalizado": False,
			"productos": [
				'0007', '0001'
			]
		},
		{
			"fecha": '2018-11-29 10:11:23',
			"finalizado": True,
			"productos": [
				'0006'
			],
			"cliente": '0001',
			"metodo_pago": "tarjeta",
			"tarjetas": [
				{
					"tarjeta": "VISA",
					"numero": "293 392 210",
					"clave": "0882"
				}
			]
		},
		{
			"fecha": '2018-11-29 15:10:00',
			"finalizado": True,
			"productos": [
				'0003'
			],
			"cliente": '0004',
			"metodo_pago": "tarjeta",
			"tarjetas": [
				{
					"tarjeta": "AMERICAN EXPRESS",
					"numero": "114 570 156 310",
					"clave": "723"
				}
			]
		},
		{
			"fecha": '2018-11-29 15:15:00',
			"finalizado": False,
			"productos": [
				'0003', '0004'
			]
		},
		{
			"fecha": '2018-11-29 16:15:00',
			"finalizado": False,
			"productos": [
				'0005', '0002'
			]
		},
		{
			"fecha": '2018-12-01 16:55:30',
			"finalizado": False,
			"productos": [
				'0003', '0002'
			]
		},
		{
			"fecha": '2018-12-01 07:05:00',
			"finalizado": False,
			"productos": [
				'0007'
			]
		},
		{
			"fecha": '2018-12-02 15:10:00',
			"finalizado": True,
			"productos": [
				'0004','0001'
			],
			"cliente": '0005',
			"metodo_pago": "tarjeta",
			"tarjetas": [
				{
					"tarjeta": "VISA",
					"numero": "309 236 723",
					"clave": "3211"
				}
			]
		},
		{
			"fecha": '2018-12-03 11:20:00',
			"finalizado": True,
			"productos": [
				'0007', '0003'
			],
			"cliente": '0002',
			"metodo_pago": "tarjeta",
			"tarjetas": [
				{
					"tarjeta": "VISA",
					"numero": "140 287 210",
					"clave": "0129"
				}
			]
		},
		{
			"fecha": '2018-12-04 09:35:30',
			"finalizado": False,
			"productos": [
				'0001', '0006'
			]
		},
		{
			"fecha": '2018-12-04 11:10:00',
			"finalizado": True,
			"productos": [
				'0001'
			],
			"cliente": '0003',
			"metodo_pago": "tarjeta",
			"tarjetas": [
				{
					"tarjeta": "NARANJA",
					"numero": "440 187 254 876",
					"clave": "5792"
				}
			]
		},
		{
			"fecha": '2018-12-05 17:23:15',
			"finalizado": False,
			"productos": [
				'0006', '0001'
			]
		},
		{
			"fecha": '2018-12-05 19:23:15',
			"finalizado": False,
			"productos": [
				'0006'
			]
		},
		{
			"fecha": '2018-12-06 10:15:15',
			"finalizado": False,
			"productos": [
				'0005'
			]
		},
		{
			"fecha": '2018-12-07 10:11:23',
			"finalizado": True,
			"productos": [
				'0006'
			],
			"cliente": '0001',
			"metodo_pago": "tarjeta",
			"tarjetas": [
				{
					"tarjeta": "VISA",
					"numero": "140 287 210",
					"clave": "0129"
				}
			]
		},
		{
			"fecha": '2018-12-06 10:25:25',
			"finalizado": False,
			"productos": [
				'0003'
			]
		},
		{
			"fecha": '2018-12-06 10:26:20',
			"finalizado": False,
			"productos": [
				'0006'
			]
		},
		{
			"fecha": '2018-12-07 11:10:00',
			"finalizado": True,
			"productos": [
				'0006','0001'
			],
			"cliente": '0003',
			"metodo_pago": "tarjeta",
			"tarjetas": [
				{
					"tarjeta": "NARANJA",
					"numero": "440 187 254 876",
					"clave": "5792"
				}
			]
		},
		{
			"fecha": '2018-12-08 11:10:00',
			"finalizado": True,
			"productos": [
				'0002','0001'
			],
			"cliente": '0002',
			"metodo_pago": "tarjeta",
			"tarjetas": [
				{
					"tarjeta": "VISA",
					"numero": "140 287 210",
					"clave": "0129"
				}
			]
		}
	]
}
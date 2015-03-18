class cuboSemantico:
	cubo_semantico = None

	def __init__(self):
		self.cubo_semantico = {
		'IGUAL': {
			'ENTERO': {
				'ENTERO': 'ENTERO',
				'DECIMAL': None,
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': None,
				'DECIMAL': 'DECIMAL',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': 'TEXTO'
			}
		},
		'Y': {
			'ENTERO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None,
				'bool': None
			},
			'DECIMAL': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None,
				'bool': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None,
				'bool': None
			},
			'bool': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None,
				'bool': 'bool'
			}
		},
		'O': {
			'ENTERO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None,
				'bool': None
			},
			'DECIMAL': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None,
				'bool': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None,
				'bool': None
			},
			'bool': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None,
				'bool': 'bool'
			}
		},
		'MAYOR': {
			'ENTERO': {
				'ENTERO': 'bool',
				'DECIMAL': 'bool',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'bool',
				'DECIMAL': 'bool',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': 'bool'
			}
		},
		'MENOR': {
			'ENTERO': {
				'ENTERO': 'bool',
				'DECIMAL': 'bool',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'bool',
				'DECIMAL': 'bool',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': 'bool'
			}
		},
		'DIFERENTE': {
			'ENTERO': {
				'ENTERO': 'bool',
				'DECIMAL': 'bool',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'bool',
				'DECIMAL': 'bool',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': 'bool'
			}
		},
		'MAYORIGUAL': {
			'ENTERO': {
				'ENTERO': 'bool',
				'DECIMAL': 'bool',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'bool',
				'DECIMAL': 'bool',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': 'bool'
			}
		},
		'MENORIGUAL': {
			'ENTERO': {
				'ENTERO': 'bool',
				'DECIMAL': 'bool',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'bool',
				'DECIMAL': 'bool',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': 'bool'
			}
		},
		'IDENTICO': {
			'ENTERO': {
				'ENTERO': 'bool',
				'DECIMAL': 'bool',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'bool',
				'DECIMAL': 'bool',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': 'bool'
			}
		},
		'SUMA': {
			'ENTERO': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'DECIMAL',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'DECIMAL',
				'DECIMAL': 'DECIMAL',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None
			}
		},
		'RESTA': {
			'ENTERO': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'DECIMAL',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'DECIMAL',
				'DECIMAL': 'DECIMAL',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None
			}
		},
		'MULTIPLICACION': {
			'ENTERO': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'DECIMAL',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'DECIMAL',
				'DECIMAL': 'DECIMAL',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None
			}
		},
		'DIVISION': {
			'ENTERO': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'DECIMAL',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'DECIMAL',
				'DECIMAL': 'DECIMAL',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None
			}
		}
	}

	def checarSemanticaExp(self,oper1,oper2,op):
		res = self.cubo_semantico.get(op)
		if res != None:
			res = res.get(oper1)
			if res != None:
				res = res.get(oper2)
		return res
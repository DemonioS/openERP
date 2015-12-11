# -*- coding: utf-8 -*-
from osv import osv, fields

class modulo_ejemplo_objeto(osv.osv):
_name = ‘modulo_ejemplo.objeto’
_description = ‘Objeto’
_columns = {
‘cadena’: fields.char(‘Campo char’, size=200, required=True),
‘cadenados’: fields.char(‘Campo char’, size=200, required=False),

}

modulo_ejemplo_objeto()
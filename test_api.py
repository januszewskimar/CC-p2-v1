from api import app
import unittest

class TestPrediccionesV1(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_prediccion24h(self):
        respuesta = self.app.get('/servicio/v1/prediccion/24horas/')
        self.assertEqual(respuesta.status_code, 200)
        
    def test_prediccion48h(self):
        respuesta = self.app.get('/servicio/v1/prediccion/48horas/')
        self.assertEqual(respuesta.status_code, 200)
        
    def test_prediccion72h(self):
        respuesta = self.app.get('/servicio/v1/prediccion/72horas/')
        self.assertEqual(respuesta.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()

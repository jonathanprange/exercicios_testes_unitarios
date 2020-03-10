from unittest import mock, TestCase
from unittest.mock import Mock, patch

from app.api_cep import _get_somente_numeros, ApiCep


class TestApiCep(TestCase):

    @patch('app.api_cep.re.sub')
    def test_get_somente_numeros(self, mock_re_sub):
        # arrange
        mock_re_sub.return_value = '89068060'

        # action
        resultado = _get_somente_numeros('89ronaldo068-06@0')

        # assertions
        self.assertEqual(resultado, '89068060')
        mock_re_sub.assert_called_once_with('[^0-9]', '', '89ronaldo068-06@0')


    @patch('app.api_cep.requests.get')
    @patch('app.api_cep._get_somente_numeros')
    def test_execute(self, mock_get_somente_numeros, mock_requests_get):
        # arrange
        mock_get_somente_numeros.return_value = '89068060'
        mock_objeto_de_retorno_do_mock_requests_get = Mock()
        mock_objeto_de_retorno_do_mock_requests_get.json.return_value = {
                    'mock_cep': '89035-300', 
                    'mock_logradouro': 'Rua Theodoro Holtrup', 
                    'mock_bairro': 'Vila Nova', 
                    'localidade': 'Blumenau', 
                    'uf': 'SC'
        }
        mock_requests_get.return_value = mock_objeto_de_retorno_do_mock_requests_get
        nova_api_cep = ApiCep()


        # action
        resultado = nova_api_cep.execute('89ronaldo068-06@0')


        # assertions
        self.assertEqual(resultado, {
                    'mock_cep': '89035-300', 
                    'mock_logradouro': 'Rua Theodoro Holtrup', 
                    'mock_bairro': 'Vila Nova', 
                    'localidade': 'Blumenau', 
                    'uf': 'SC'
        })
        mock_get_somente_numeros.assert_called_once_with('89ronaldo068-06@0')
        mock_requests_get.assert_called_once_with('http://www.viacep.com.br/ws/89068060/json/')
        mock_objeto_de_retorno_do_mock_requests_get.json.assert_called_once_with()
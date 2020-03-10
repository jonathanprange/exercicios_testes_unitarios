from run import ApiCep
from unittest import TestCase, mock
from unittest.mock import MagicMock, Mock, patch

from run import consulta_api_viacep


class TestApp(TestCase):

    @patch('run.ApiCep.execute')
    @patch('run.print')
    @patch('run.input')
    def test_consulta_api_viacep(self, mock_input, mock_print, mock_apicep_execute):
        # Arrange

        mock_input.return_value = '89035-300'
        mock_apicep_execute.return_value = {
                    'mock_cep': '89035-300', 
                    'mock_logradouro': 'Rua Theodoro Holtrup', 
                    'mock_bairro': 'Vila Nova', 
                    'localidade': 'Blumenau', 
                    'uf': 'SC'
        }

        # Action
        resultado = consulta_api_viacep()


        # assertions
        self.assertEqual(resultado, 'Cep consultado com sucesso!')
        mock_input.assert_called_once_with('Informe o cep para consulta: ')
        mock_print.assert_called_once_with({
                    'mock_cep': '89035-300', 
                    'mock_logradouro': 'Rua Theodoro Holtrup', 
                    'mock_bairro': 'Vila Nova', 
                    'localidade': 'Blumenau', 
                    'uf': 'SC'
        })
        mock_apicep_execute.assert_called_once_with('89035-300')
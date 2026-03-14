
"""
Função responsável por tratamento de erros na digitação do 
horário
"""
class ValidadorHorario:
    
    def verificar_horario(self, _texto):
        if ":" not in _texto:
            return False
        else:
            partes = _texto.split(":")
        
            if len(partes) != 2:
                return False
            else:     
                hora_str, minuto_str = partes

                if not hora_str.isdigit() or not minuto_str.isdigit():
                    return False
                
                else:
                    hora = int(hora_str)
                    minuto = int(minuto_str)

                    if 0 <= hora <= 23 and 0 <= minuto <= 59:
                        return True
                    else: 
                        return False
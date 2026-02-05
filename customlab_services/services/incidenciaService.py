from customlab_models.repositories.incidenciaRepository import IncidenciaRepository

class IncidenciaService:
    def getIncidencias():
        incidencias = IncidenciaRepository.getIncidencias()
        if incidencias:
            return {
                'success': True,
                'data': list(incidencias)
            }
        return {
            'success': False,
            'message': 'No incidencias found'
        }
    
    def getIncidenciaById(idIncidencia):
        incidencia = IncidenciaRepository.getIncidenciaById(idIncidencia)
        if incidencia:
            return {
                'success': True,
                'data': incidencia
            }
        return {
            'success': False,
            'message': 'Incidencia not found'
        }
    
    def createIncidencia(data):
        success = IncidenciaRepository.createIncidencia(data)
        if success:
            return {
                'success': True,
                'message': 'Incidencia creada exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al crear la incidencia'
        }
    
    def verifyIncidencia(idIncidencia):
        exist = IncidenciaRepository.getIncidenciaById(idIncidencia)
        if exist == False:
            return {
                'success': False,
                'message': 'Incidencia no encontrada'
            }
        return {
            'success': True,
            'data': exist
        }
    
    def updateEstadoIncidencia(idIncidencia, data):
        exist = IncidenciaService.verifyIncidencia(idIncidencia)
        if not exist['success']:
            return exist
        success = IncidenciaRepository.updateEstadoIncidencia(idIncidencia, data)
        if success:
            return {
                'success': True,
                'message': 'Incidencia actualizada exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al actualizar la incidencia'
        }
    
    def deleteIncidencia(idIncidencia):
        exist = IncidenciaService.verifyIncidencia(idIncidencia)
        if not exist:
            return exist
        success = IncidenciaRepository.deleteIncidencia(idIncidencia)
        if success:
            return {
                'success': True,
                'message': 'Incidencia eliminada exitosamente'
            }
        return {
            'success': False,
            'message': 'Error al eliminar la incidencia'
        }
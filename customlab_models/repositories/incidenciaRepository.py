from customlab_models.models import Incidencias
from customlab_models.models import Usuarios

class IncidenciaRepository:
    @staticmethod
    def getIncidencias():
        incidencias = Incidencias.objects.all().order_by('-fecha').values(
            'id_incidencia', 'id_usuario', 'tipo', 'fecha', 'estado_incidencia', 'descripcion'
        )
        if not incidencias.exists():
            return False
        return incidencias
    
    @staticmethod
    def getIncidenciaById(idIncidencia):
        incidencia = Incidencias.objects.filter(id_incidencia=idIncidencia).values(
            'id_incidencia', 'id_usuario', 'tipo', 'fecha', 'estado_incidencia', 'descripcion'
        )
        if not incidencia.exists():
            return False
        return incidencia
    
    @staticmethod
    def createIncidencia(data):
        try:
            usuario = Usuarios.objects.get(id_usuario=data.get('id_usuario'))
            Incidencias.objects.create(
                id_usuario=usuario,
                tipo=data.get('tipo'),
                estado_incidencia=data.get('estado'),
                descripcion=data.get('descripcion'),
            )
            if Incidencias.objects.exists():
                return True
        except Usuarios.DoesNotExist:
            return False
        return False
    
    @staticmethod
    def updateEstadoIncidencia(idIncidencia, data):
        Incidencias.objects.filter(id_incidencia=idIncidencia).update(
            estado_incidencia=data.get('estado')
        )
        if Incidencias.objects.filter(id_incidencia=idIncidencia).exists():
            return True
        return False
    
    @staticmethod
    def deleteIncidencia(idIncidencia):
        Incidencias.objects.filter(id_incidencia=idIncidencia).delete()
        if not Incidencias.objects.filter(id_incidencia=idIncidencia).exists():
            return True
        return False
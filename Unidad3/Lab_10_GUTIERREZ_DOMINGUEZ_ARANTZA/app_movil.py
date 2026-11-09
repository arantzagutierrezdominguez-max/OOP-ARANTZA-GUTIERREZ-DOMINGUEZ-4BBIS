class SuscripcionExpiradaError(Exception):
    """Excepción lanzada al intentar ejecutar operaciones restringidas sin membresía activa."""
    pass

class PuntosInsuficientesError(Exception):
    """Excepción lanzada cuando una transacción supera el saldo de gemas disponible."""
    pass

class PerfilMovil:
    def __init__(self, username: str, gemas: int = 50, racha_dias: int = 1, notificaciones_activas: bool = True):
        if gemas < 0:
            raise ValueError("Las gemas iniciales no pueden ser negativas.")
        self.username = username
        self.gemas = gemas
        self.racha_dias = racha_dias
        self.notificaciones_activas = notificaciones_activas

    def ganar_gemas(self, cantidad: int) -> int:
        """Incrementa el saldo de gemas validando que sea estrictamente positivo[cite: 1, 2]."""
        if cantidad <= 0:
            raise ValueError("La cantidad a ganar debe ser estrictamente positiva.")
        self.gemas += cantidad
        return self.gemas

    def gastar_gemas(self, cantidad: int) -> int:
        """Disminuye el saldo tras verificar disponibilidad y valores positivos."""
        if cantidad <= 0:
            raise ValueError("La cantidad a gastar debe ser estrictamente positiva.")
        if cantidad > self.gemas:
            raise PuntosInsuficientesError("No hay suficientes gemas para realizar la transacción.")
        self.gemas -= cantidad
        return self.gemas

class PerfilPro(PerfilMovil):
    def __init__(self, username: str, gemas: int = 50, racha_dias: int = 1, notificaciones_activas: bool = True, meses_suscripcion: int = 1):
        if meses_suscripcion <= 0:
            raise ValueError("Los meses de suscripción inicial deben ser mayores a cero.")
        super().__init__(username, gemas, racha_dias, notificaciones_activas)
        self.meses_suscripcion = meses_suscripcion
        self.es_pro = True

    def descargar_contenido_offline(suef, self=None) -> str:
        # Nota: Ajustamos el parámetro interno de instancia de manera limpia
        pass

    def descargar_contenido_offline(self) -> str:
        """Evalúa la validez temporal de la suscripción Pro."""
        if self.meses_suscripcion <= 0:
            self.es_pro = False
            raise SuscripcionExpiradaError("La suscripción Pro ha expirado.")
        return "Contenido descargado exitosamente."
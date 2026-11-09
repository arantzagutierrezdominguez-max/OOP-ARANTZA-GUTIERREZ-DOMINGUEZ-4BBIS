import pytest
from app_movil import (
    PerfilMovil,
    PerfilPro,
    SuscripcionExpiradaError,
    PuntosInsuficientesError,
)

# 1. State Isolation: Fixture para proveer instancias estandarizadas[cite: 2]
@pytest.fixture
def perfil_basico():
    return PerfilMovil(username="usuario_test", gemas=50, racha_dias=1, notificaciones_activas=True)

@pytest.fixture
def perfil_pro():
    return PerfilPro(username="usuario_pro", gemas=100, racha_dias=5, notificaciones_activas=True, meses_suscripcion=3)

# 2. Structural Integrity and Assertion Tests[cite: 2]
def test_inicializacion_perfil_movil(perfil_basico):
    assert perfil_basico.username == "usuario_test"
    assert perfil_basico.gemas == 50
    assert perfil_basico.racha_dias == 1
    assert perfil_basico.notificaciones_activas is True

def test_transacciones_gemas(perfil_basico):
    perfil_basico.ganar_gemas(25)
    assert perfil_basico.gemas == 75

    perfil_basico.gastar_gemas(30)
    assert perfil_basico.gemas == 45

# 4. Parameterized Tests (@pytest.mark.parametrize)[cite: 2]
@pytest.mark.parametrize(
    "gemas_iniciales, gemas_ganadas, resultado_esperado",
    [
        (50, 10, 60),
        (0, 100, 100),
        (20, 5, 25),
    ]
)
def test_ganar_gemas_parametrizado(gemas_iniciales, gemas_ganadas, resultado_esperado):
    perfil = PerfilMovil(username="param_user", gemas=gemas_iniciales)
    perfil.ganar_gemas(gemas_ganadas)
    assert perfil.gemas == resultado_esperado

# 3. Exception Validation (pytest.raises)[cite: 2]
def test_excepciones_y_valores_invalidos():
    # Validar gemas iniciales negativas
    with pytest.raises(ValueError):
        PerfilMovil(username="error_user", gemas=-5)

    perfil = PerfilMovil(username="user_ex", gemas=20)
    
    # Validar ganar gemas con valores no positivos
    with pytest.raises(ValueError):
        perfil.ganar_gemas(0)
    with pytest.raises(ValueError):
        perfil.ganar_gemas(-10)

    # Validar gastar gemas con valores no positivos
    with pytest.raises(ValueError):
        perfil.gastar_gemas(0)

    # Validar puntos insuficientes al gastar más de lo disponible
    with pytest.raises(PuntosInsuficientesError):
        perfil.gastar_gemas(50)

# 5. Type and Hierarchy Verification (isinstance)[cite: 2]
def test_herencia_y_perfil_pro(perfil_pro):
    # Verificación de jerarquía
    assert isinstance(perfil_pro, PerfilMovil)
    assert isinstance(perfil_pro, PerfilPro)
    assert perfil_pro.es_pro is True

    # Descarga exitosa con suscripción vigente
    mensaje = perfil_pro.descargar_contenido_offline()
    assert mensaje == "Contenido descargado exitosamente."

    # Simular expiración de suscripción (meses = 0)
    perfil_pro.meses_suscripcion = 0
    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro.descargar_contenido_offline()
    
    # Comprobar cambio de estado a False
    assert perfil_pro.es_pro is False

def test_perfil_pro_meses_invalidos():
    with pytest.raises(ValueError):
        PerfilPro(username="pro_invalido", meses_suscripcion=0)
    with pytest.raises(ValueError):
        PerfilPro(username="pro_invalido", meses_suscripcion=-3)
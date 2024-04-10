
-- Crear tabla 'sm_internet'
CREATE TABLE sm_internet (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    modalidad_pago VARCHAR(50) NOT NULL,
	fecha_create DATE NOT NULL,
    operador VARCHAR(100) NOT NULL,
    tipo_conexion VARCHAR(100) NOT NULL,
    mb INTEGER NOT NULL,
    minutos INTEGER,
    vigencia INTEGER,
    ud_vigencia VARCHAR(255)
);

-- Crear tabla 'sm_prepago'
CREATE TABLE sm_prepago (
    id SERIAL PRIMARY KEY,
    nombre_comercial VARCHAR(100) NOT NULL,
    precio_mensual DECIMAL(10,2) NOT NULL,
    nombre_tarifa_plan VARCHAR(100) NOT NULL,
    tarifa_normal DECIMAL(10,2),
    tarifa_reducida DECIMAL(10,2),
    tarifa_super_reducida DECIMAL(10,2),
    sms_libres INTEGER,
    tarifa_sms_adicional DECIMAL(10,2),
    mb_disponibles INTEGER,
    precio_mb_adicional DECIMAL(10,2),
    fecha_create DATE NOT NULL
);

-- Crear tabla 'sf_internet'
CREATE TABLE sf_internet (
    id SERIAL PRIMARY KEY,
    razon_social VARCHAR(100) NOT NULL,
    nombre_comercial VARCHAR(100) NOT NULL,
    costo_instalacion DECIMAL(10,2),
    tipo_pago VARCHAR(20) NOT NULL,
    otros_beneficios TEXT,
    nombre_tarifa_plan VARCHAR(100) NOT NULL,
    ancho_banda_bajada INTEGER NOT NULL,
    precio_mensual DECIMAL(10,2) NOT NULL,
    ancho_banda_subida INTEGER NOT NULL,
    denominacion_tecnologia VARCHAR(100) NOT NULL,
    departamento VARCHAR(100),
    fecha_create DATE NOT NULL
);

-- Crear tabla 'sf_television'
CREATE TABLE sf_television (
    id SERIAL PRIMARY KEY,
    nombre_comercial VARCHAR(100) NOT NULL,
    razon_social VARCHAR(100) NOT NULL,
    departamento VARCHAR(100),
    nombre_tarifa_plan VARCHAR(100) NOT NULL,
    costo_instalacion DECIMAL(10,2) NOT NULL,
    precio_mensual DECIMAL(10,2) NOT NULL,
    cantidad_canales_digitales INTEGER NOT NULL,
    cantidad_canales_analogicos INTEGER NOT NULL,
    denominacion_tecnologia VARCHAR(100) NOT NULL,
    tipo_pago VARCHAR(20) NOT NULL,
    tarifa_punto_adicional DECIMAL(10,2) NOT NULL,
    observaciones TEXT,
    fecha_create DATE NOT NULL
);


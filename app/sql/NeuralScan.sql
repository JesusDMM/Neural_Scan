CREATE DATABASE NEURAL_SCAN;

USE NEURAL_SCAN;

CREATE TABLE `instituciones` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `correo` varchar(255) UNIQUE NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  `fecha_registro` timestamp NOT NULL
);

CREATE TABLE `paquetes` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `descripcion` text NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `duracion_mes` int NOT NULL
);

CREATE TABLE `metodos_pago` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `id_institucion` int NOT NULL,
  `tipo_pago` enum("tarjeta", "paypal") NOT NULL,
  `numero_tarjeta` varchar(16) DEFAULT null,
  `cvv` varchar(3) DEFAULT null,
  `fecha_expiracion` date DEFAULT null,
  `paypal_email` varchar(255) DEFAULT null
);

CREATE TABLE `membresias` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `id_metodo_pago` int NOT NULL,
  `id_paquete` int NOT NULL,
  `tipo_pago` enum("mensual", "único") NOT NULL,
  `fecha_inicio` timestamp NOT NULL,
  `estado` enum("activa", "cancelada") DEFAULT 'activa',
  `monto` decimal(10,2) NOT NULL
);

CREATE TABLE `pagos` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `id_membresia` int NOT NULL,
  `fecha_pago` timestamp NOT NULL,
  `estado_pago` enum("pendiente", "completado", "cancelado") NOT NULL
);

CREATE TABLE `medicos` (
  `cedula` varchar(19) PRIMARY KEY NOT NULL,
  `id_institucion` int NOT NULL,
  `correo` varchar(255) UNIQUE NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  `nombres` varchar(255) NOT NULL,
  `apellidos` varchar(255) NOT NULL,
  `edad` int,
  `especialidad` varchar(255) NOT NULL
);

CREATE TABLE `pacientes` (
  `curp` varchar(19) PRIMARY KEY NOT NULL ,
  `user_id` int NOT NULL,
  `nombres` varchar(255) NOT NULL,
  `apellidos` varchar(255) NOT NULL,
  `genero` ENUM ('M', 'F') NOT NULL,
  `edad` int NOT NULL,
  `lugar` text NOT NULL
);

CREATE TABLE `paciente_medico` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `cedula` varchar(19) NOT NULL,
  `curp` varchar(19) NOT NULL,
  `fecha` timestamp NOT NULL
);

CREATE TABLE `historial_detecciones` (
  `id_deteccion` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `id_paciente_medico` int NOT NULL,
  `url_imagen` varchar(255) UNIQUE NOT NULL,
  `comentario` text DEFAULT null
);

CREATE TABLE `tumores_detectados` (
  `id_tumor` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `id_deteccion` int NOT NULL,
  `type` ENUM ('Glioma', 'Meningioma', 'Pituitary') NOT NULL,
  `certeza` float NOT NULL,
  `evaluacion` ENUM ('Correcto', 'Incorrecto') DEFAULT null
);

ALTER TABLE `metodos_pago` ADD FOREIGN KEY (`id_institucion`) REFERENCES  `instituciones` (`id`);

ALTER TABLE `membresias` ADD FOREIGN KEY (`id_metodo_pago`) REFERENCES `metodos_pago` (`id`);

ALTER TABLE `membresias` ADD FOREIGN KEY (`id_paquete`) REFERENCES `paquetes` (`id`);

ALTER TABLE `pagos` ADD FOREIGN KEY (`id_membresia`) REFERENCES `membresias` (`id`);

ALTER TABLE `medicos` ADD FOREIGN KEY (`id_institucion`) REFERENCES `instituciones` (`id`);

ALTER TABLE `paciente_medico` ADD FOREIGN KEY (`curp`) REFERENCES `pacientes` (`curp`);

ALTER TABLE `paciente_medico` ADD FOREIGN KEY (`cedula`) REFERENCES `medicos` (`cedula`);

ALTER TABLE `historial_detecciones` ADD FOREIGN KEY (`id_paciente_medico`) REFERENCES `paciente_medico` (`id`);

ALTER TABLE `tumores_detectados` ADD FOREIGN KEY (`id_deteccion`) REFERENCES `historial_detecciones` (`id_deteccion`);

INSERT INTO `instituciones` (nombre, correo, contraseña, fecha_registro)
VALUES ('IMSS', 'imss_mante@imss.com', 'password123', NOW());

INSERT INTO `medicos` (cedula, id_institucion, correo, contraseña, nombres, apellidos, edad, especialidad)
VALUES ('ISC12', 2, 'rodrigo12@imss.com', 'roy', 'Rodirgo', 'Pérez', 40, 'neurólogo');

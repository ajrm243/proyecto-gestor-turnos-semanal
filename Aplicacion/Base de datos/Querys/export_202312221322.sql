-- Disponibilidad definition

CREATE TABLE Disponibilidad (
	ID_Disponibilidad INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Nombre TEXT(64) NOT NULL,
	Descripcion TEXT(128)
);


-- Horario definition

CREATE TABLE Horario (
	ID_Horario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	DiaSemana TEXT CHECK( DiaSemana IN ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Sabado', 'Domingo') ) NOT NULL DEFAULT 'Lunes',
	HoraEntrada INTEGER NOT NULL,
	Prof_1 INTEGER NOT NULL,
	Prof_2 INTEGER NOT NULL,
	Prof_3 INTEGER NOT NULL
, HoraSalida INTEGER NOT NULL);


-- Rol definition

CREATE TABLE Rol (
	ID_Rol INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Nombre TEXT(64) NOT NULL,
	Descripcion TEXT(128)
);


-- Turno definition

CREATE TABLE Turno (
	ID_Turno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Nombre TEXT(64) NOT NULL,
	HoraIngreso INTEGER NOT NULL,
	HoraSalida INTEGER NOT NULL
);


-- Usuario definition

CREATE TABLE Usuario (
	ID_Usuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Username TEXT(64) NOT NULL,
	Password TEXT(128) NOT NULL
);


-- Colaborador definition

CREATE TABLE Colaborador (
	ID_Colaborador INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Nombre TEXT(128) NOT NULL,
	Correo TEXT(128) NOT NULL,
	Telefono TEXT DEFAULT (2256-2222) NOT NULL,
	ID_Rol INTEGER NOT NULL,
	ID_Turno INTEGER NOT NULL,
	ID_Disponibilidad INTEGER NOT NULL,
	Modalidad INTEGER DEFAULT (1) NOT NULL,
	CONSTRAINT Colaborador_FK_3 FOREIGN KEY (ID_Rol) REFERENCES Rol(ID_Rol),
	CONSTRAINT Colaborador_FK_4 FOREIGN KEY (ID_Turno) REFERENCES Turno(ID_Turno),
	CONSTRAINT Colaborador_FK_5 FOREIGN KEY (ID_Disponibilidad) REFERENCES Disponibilidad(ID_Disponibilidad)
);


-- Colaborador_Horario definition

CREATE TABLE Colaborador_Horario (
	ID_Colaborador_Horario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	ID_Horario INTEGER NOT NULL,
	ID_Colaborador INTEGER NOT NULL,
	HorasExtra INTEGER DEFAULT (0) NOT NULL,
	CONSTRAINT Colaborador_Horario_FK FOREIGN KEY (ID_Colaborador) REFERENCES Colaborador(ID_Colaborador),
	CONSTRAINT Colaborador_Horario_FK_1 FOREIGN KEY (ID_Horario) REFERENCES Horario(ID_Horario)
);
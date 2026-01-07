-- Criar tabela clients
CREATE TABLE clients (
--    id INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
	id UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    limite INT NOT NULL,
    saldo INT NOT NULL,
	CHECK (saldo >= limite)
);

-- Criar tabela transactions
CREATE TABLE transactions (
--    id INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
	id UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    tipo CHAR(1) NOT NULL,
    descricao VARCHAR(10) NOT NULL,
    valor INT NOT NULL,
    cliente_id uniqueidentifier NOT NULL,
    realizada_em DATETIME NOT NULL DEFAULT GETDATE()
);
